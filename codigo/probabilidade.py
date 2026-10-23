"""Probabilidade de vitória no 2º turno de 2026 e classificação presidencial 1989-2026.

Entradas: resultados/modelo_2t.json (centro), dados/historico_erros.csv (erro das pesquisas finais
presidenciais 1989-2022), dados/rodadas_1t.csv (1º turno de 2026).
Erro sistemático: o erro do AGREGADO (média dos institutos com campo até 7 dias antes) em cada
2º turno presidencial. sigma = raiz do erro quadrático médio; cauda t com (eleições - 1) graus.

Uso: python3 -I codigo/probabilidade.py
"""
import csv
import json
import math
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "resultados"
N = st.NormalDist()
# dos institutos com 20+ pesquisas, os que erraram menos que os rivais na mesma disputa (Tabela 3, valor negativo)
MELHORES_2012_2022 = ("Futura/100% Cidades", "AtlasIntel/Bloomberg", "Datafolha", "CNT/MDA")
# institutos com 20 ou mais pesquisas finais na base 2012-2022 (resultados/ranking_2012_2022.json)
HISTORICO_LONGO = ("Datafolha", "Quaest", "AtlasIntel/Bloomberg", "CNT/MDA", "Ipespe/Abrapel", "Veritá",
                   "Real Time Big Data", "Futura/100% Cidades")


def f(x):
    try:
        return float(str(x).replace(",", "."))
    except (TypeError, ValueError):
        return None


hist = [r for r in csv.DictReader(open(RAIZ / "dados/historico_erros.csv", encoding="utf-8"))
        if f(r["erro_sinal_pp"]) is not None]


def agregado_por_eleicao(turno, dias_max=7):
    """Erro médio entre institutos por ano (pp na fatia de válidos do candidato de direita/PSDB)."""
    por = defaultdict(list)
    for r in hist:
        d = f(r.get("dias_antes_eleicao"))
        if r["turno"].strip() == str(turno) and d is not None and d <= dias_max:
            por[int(r["ano"])].append(f(r["erro_sinal_pp"]))
    return {a: (st.mean(v), len(v)) for a, v in sorted(por.items())}


def p_t(mu, sigma, gl, sims=400_000, seed=5):
    """P(V > 50) com V = mu + sigma * T_gl: preditiva quando sigma é estimado com gl graus de
    liberdade (variância desconhecida). Cauda mais gorda que a normal, nunca mais estreita."""
    rnd = random.Random(seed)
    esc = sigma
    acima = 0
    for _ in range(sims):
        t = rnd.gauss(0, 1) / math.sqrt(rnd.gammavariate(gl / 2, 2) / gl)
        acima += mu + esc * t > 50
    # 4 casas: o erro de Monte Carlo é ~0,0007 com 400 mil sorteios, e k/400000 cai em fronteira de
    # arredondamento da 6ª casa (quebraria o selo entre sistemas operacionais)
    return round(acima / sims, 4)


if __name__ == "__main__":
    m2 = json.load(open(SAIDA / "modelo_2t.json"))
    a2 = agregado_por_eleicao(2)
    a1 = agregado_por_eleicao(1)
    usa = {a: e for a, (e, k) in a2.items() if k >= 2}  # 1989 tem um instituto só
    erros = list(usa.values())
    rms = math.sqrt(st.mean(e * e for e in erros))
    vies, ep_vies = st.mean(erros), st.stdev(erros) / math.sqrt(len(erros))
    pares = [(a1[a][0], usa[a]) for a in usa if a in a1 and a1[a][1] >= 2]
    corr_1t_2t = st.correlation([x for x, _ in pares], [y for _, y in pares]) if len(pares) > 2 else None

    # 1º turno de 2026: erro do agregado nas pesquisas FINAIS (última por instituto), mesma escala do 2º turno
    a1_2026 = json.load(open(SAIDA / "acuracia_1t_2026.json"))
    e1_2026_2p = [l["erro_bipartidario_flavio"] for l in a1_2026["ultima_por_instituto"]]
    e1_2026 = [l["erro_flavio"] for l in a1_2026["ultima_por_instituto"]]

    # Centro de referência = mediana da última rodada de cada instituto: é o mesmo estimador cujo erro
    # histórico calibra sigma (média simples das pesquisas finais), e a tendência desde 15/10 é plana.
    # Os centros com tendência entram como sensibilidade.
    janelas = {k: v["centro_25_10"] for k, v in m2["tendencia_por_janela"].items()}
    ult = [r["v"] for r in m2["ultima_rodada"]]
    rnd = random.Random(17)
    boot = [st.median(rnd.choices(ult, k=len(ult))) for _ in range(5000)]
    centro_ref = st.median(ult)
    sd_centro = st.pstdev(boot)
    vals = sorted(ult)
    sem_fonte_unica = st.median([r["v"] for r in m2["ultima_rodada"] if r["inst"] != "DataTrends"])
    ate7 = st.median([r["v"] for r in m2["ultima_rodada"] if r["dias"] <= 7])
    centros = {"mediana sem a rodada de fonte única (DataTrends)": sem_fonte_unica,
               "mediana só com rodadas até 7 dias antes (regra da calibração)": ate7,
               "mediana sem as 3 maiores para Flávio": st.median(vals[:-3]),
               "mediana sem as 3 maiores e as 3 menores": st.median(vals[3:-3]),
               "mediana dos 4 institutos que erraram menos que os rivais em 2012-2022": st.median(
                   [r["v"] for r in m2["ultima_rodada"] if r["inst"] in MELHORES_2012_2022]),
               "mediana dos institutos com >=20 pesquisas 2012-2022": st.median(
                   [r["v"] for r in m2["ultima_rodada"] if r["inst"] in HISTORICO_LONGO]),
               **{f"tendência + casa, janela desde {k[8:]}/{k[5:7]}": v for k, v in janelas.items()}}
    sigma_tot = math.sqrt(rms ** 2 + sd_centro ** 2)
    gl = len(erros)  # erros com média zero assumida: n graus de liberdade para o RMS

    cenarios = []
    for nome, mu in [("CENTRAL: mediana da última rodada", centro_ref)] + list(centros.items()):
        for rot, b in (("sem viés", 0.0), ("viés histórico do 2º turno", -vies)):
            cenarios.append({"centro": nome, "mu": mu, "ajuste_vies": b, "rotulo_vies": rot,
                             "P_normal": N.cdf((mu + b - 50) / sigma_tot), "P_t": p_t(mu + b, sigma_tot, gl)})
    # cenário da base v0: "o viés do 1º turno se repete"
    rep = -st.mean(e1_2026_2p)  # mesma escala do 2º turno: fatia bipartidária
    cenarios.append({"centro": "CENTRAL", "mu": centro_ref, "ajuste_vies": rep,
                     "rotulo_vies": "viés do 1º turno de 2026 se repete (sem apoio histórico)",
                     "P_normal": N.cdf((centro_ref + rep - 50) / sigma_tot), "P_t": p_t(centro_ref + rep, sigma_tot, gl)})
    sens_sigma = {s: N.cdf((centro_ref - 50) / s) for s in (0.7, 1.0, 1.3, 1.5, 2.0, 2.5, 3.3)}
    # sigma calibrado com pesquisas até 14 dias antes (inclui movimento dos últimos dias)
    a2_14 = {a: e for a, (e, k) in agregado_por_eleicao(2, 14).items() if k >= 2}
    rms14 = math.sqrt(st.mean(e * e for e in a2_14.values()))
    s14 = math.sqrt(rms14 ** 2 + sd_centro ** 2)
    cenarios.append({"centro": "CENTRAL", "mu": centro_ref, "ajuste_vies": 0.0,
                     "rotulo_vies": f"sem viés, sigma calibrado em 14 dias (RMS {rms14:.2f})",
                     "P_normal": N.cdf((centro_ref - 50) / s14), "P_t": p_t(centro_ref, s14, len(a2_14))})

    res = {
        "erro_agregado_2T_por_ano": {a: {"erro": e, "k": k} for a, (e, k) in a2.items()},
        "erro_agregado_1T_por_ano": {a: {"erro": e, "k": k} for a, (e, k) in a1.items()},
        "sigma_rms_2T": rms, "sigma_rms_2T_14dias": rms14, "erro_agregado_2T_14dias": a2_14, "vies_medio_2T_direita": vies, "ep_vies": ep_vies, "n_eleicoes": len(erros),
        "corr_erro_1T_x_2T_mesmo_ano": corr_1t_2t, "pares_1T_2T": pares,
        "erro_agregado_1T_2026_flavio_valido": st.mean(e1_2026), "n_finais_1T_2026": len(e1_2026_2p),
        "erro_agregado_1T_2026_flavio_bipartidario": st.mean(e1_2026_2p), "n_pesquisas_1T_2026": len(e1_2026),
        "centro_ref": centro_ref, "sd_centro": sd_centro, "centros_alternativos": centros, "sigma_total": sigma_tot, "gl_t": gl,
        "cenarios": cenarios, "sensibilidade_sigma_no_centro": sens_sigma,
    }
    json.dump(res, open(SAIDA / "probabilidade.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("cenarios",)}, ensure_ascii=False, indent=1))
    for c in cenarios:
        print(f"{c['centro'][:32]:32s} mu={c['mu']:.2f} {c['rotulo_vies'][:45]:45s} b={c['ajuste_vies']:+.2f} "
              f"P_normal={c['P_normal']:.0%} P_t={c['P_t']:.0%}")
