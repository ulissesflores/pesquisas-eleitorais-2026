"""Viés com direção: algum instituto erra sempre para o mesmo lado?

Usa as pesquisas finais 2012-2022 de codigo/ranking.py (base Pindograma). Em cada pesquisa,
nos dois primeiros colocados do resultado:
  pt   = erro com sinal na fatia bipartidária do candidato do PT (13), quando ele está entre os
         dois primeiros e o outro não é do PT. Positivo = pesquisa superestimou o PT.
  esq  = idem para o candidato de esquerda contra um de fora da esquerda (bloco abaixo).
Para cada instituto: viés médio bruto, viés relativo aos rivais na MESMA disputa (efeito de casa),
fração de pesquisas que erraram para o mesmo lado e teste binomial do sinal.
Persistência: correlação de postos do efeito de casa entre períodos.
Ligação com 2026: efeito de casa histórico pró-PT x efeito de casa no 2º turno de 2026.

Uso: python3 -I codigo/vies.py
"""
import json
import math
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ranking as R  # noqa: E402

# Bloco de esquerda pelo número do partido. Classificação de referência: Bolognesi, Ribeiro &
# Codato (2023), Dados 66(2). PT, PSOL, PCdoB, PSB, PDT, Rede, PV, PSTU, PCO, PCB, UP, PPL.
ESQ = {13, 50, 65, 40, 12, 18, 43, 16, 29, 21, 80, 54}
PT = 13


def partido(nr):
    try:
        return int(str(nr)[:2])
    except ValueError:
        return None


def erro_bipartidario(l, eh_alvo):
    """Erro com sinal (pp) na fatia do candidato-alvo entre os dois primeiros; None se não se aplica."""
    (p1, r1, n1), (p2, r2, n2) = l["top2"]
    a1, a2 = eh_alvo(partido(n1)), eh_alvo(partido(n2))
    if a1 == a2:
        return None
    pa, ra = (p1, r1) if a1 else (p2, r2)
    return 100 * pa / (p1 + p2) - 100 * ra / (r1 + r2)


def binom_bilateral(k, n):
    """P-valor bilateral exato do teste do sinal (p = 0,5)."""
    pk = [math.comb(n, i) / 2 ** n for i in range(n + 1)]
    obs = pk[k]
    return min(1.0, sum(p for p in pk if p <= obs + 1e-12))


def analisa(campo, eh_alvo, nmin=8):
    ls = []
    for l in R.linhas:
        e = erro_bipartidario(l, eh_alvo)
        if e is not None:
            ls.append({**l, campo: e})
    disputa = defaultdict(list)
    for l in ls:
        disputa[(l["ano"], l["turno"], l["cargo"], l["ue"])].append(l)
    for g in disputa.values():
        for l in g:
            outros = [o[campo] for o in g if o["cid"] != l["cid"]]
            l["rel"] = l[campo] - st.mean(outros) if outros else None
    geral = {
        "n_pesquisas": len(ls), "vies_medio_industria": st.mean(l[campo] for l in ls),
        "por_ano_tipo": {f"{a}-{t}": round(st.mean(x[campo] for x in ls if x["ano"] == a and x["tipo"] == t), 2)
                         for a in sorted({x["ano"] for x in ls}) for t in ("presidente_BR", "governador", "prefeito")
                         if sum(1 for x in ls if x["ano"] == a and x["tipo"] == t) >= 5},
        "por_turno": {t: round(st.mean(x[campo] for x in ls if x["turno"] == t), 2) for t in (1, 2)},
    }
    por = defaultdict(list)
    for l in ls:
        por[(l["cid"], l["nome"])].append(l)
    rel_todos = [l["rel"] for l in ls if l["rel"] is not None]
    mu_rel = st.mean(rel_todos)
    inst = []
    for (cid, nome), v in por.items():
        rels = [x["rel"] for x in v if x["rel"] is not None]
        if len(v) < nmin:
            continue
        acima = sum(1 for x in v if x[campo] > 0)
        k_rel = sum(1 for r in rels if r > 0)
        inst.append({
            "instituto": nome, "id": cid, "n": len(v), "anos": f"{min(x['ano'] for x in v)}-{max(x['ano'] for x in v)}",
            "vies_bruto": st.mean(x[campo] for x in v),
            "pct_superestimou": acima / len(v), "p_sinal_bruto": binom_bilateral(acima, len(v)),
            "casa": st.mean(rels) if rels else None,
            "casa_encolhida": (mu_rel + (st.mean(rels) - mu_rel) * len(rels) / (len(rels) + R.K_ENCOLHE)) if rels else None,
            "n_rel": len(rels), "pct_casa_mesmo_lado": (k_rel / len(rels)) if rels else None,
            "p_sinal_casa": binom_bilateral(k_rel, len(rels)) if rels else None,
        })
    inst.sort(key=lambda d: d["casa_encolhida"] if d["casa_encolhida"] is not None else 0)
    # persistência do efeito de casa
    pers = []
    for corte in (2016, 2018, 2020):
        a, b = defaultdict(list), defaultdict(list)
        for l in ls:
            if l["rel"] is not None:
                (a if l["ano"] < corte else b)[l["cid"]].append(l["rel"])
        com = [c for c in a if c in b and len(a[c]) >= 4 and len(b[c]) >= 4]
        if len(com) > 3:
            pers.append({"corte": corte, "n_institutos": len(com),
                         "spearman": R.spearman([st.mean(a[c]) for c in com], [st.mean(b[c]) for c in com])})
    return {"geral": geral, "institutos": inst, "persistencia_casa": pers}


if __name__ == "__main__":
    res = {"pt": analisa("pt", lambda p: p == PT), "esquerda": analisa("esq", lambda p: p in ESQ)}
    json.dump(res, open(R.SAIDA / "vies_direcao_2012_2022.json", "w"), ensure_ascii=False, indent=1)
    for nome, r in res.items():
        print(f"\n===== {nome}: {json.dumps(r['geral'], ensure_ascii=False)}")
        print("persistência do efeito de casa:", r["persistencia_casa"])
        for d in r["institutos"]:
            if d["n"] >= 15 or abs(d["casa_encolhida"] or 0) > 1:
                print(f"{d['instituto'][:30]:30s} n={d['n']:4d} {d['anos']} bruto={d['vies_bruto']:+.2f} "
                      f"super={d['pct_superestimou']:.0%} p={d['p_sinal_bruto']:.3f} | casa={d['casa'] if d['casa'] is None else round(d['casa'],2)} "
                      f"enc={d['casa_encolhida'] if d['casa_encolhida'] is None else round(d['casa_encolhida'],2)} "
                      f"mesmo_lado={d['pct_casa_mesmo_lado'] if d['pct_casa_mesmo_lado'] is None else round(d['pct_casa_mesmo_lado'],2)} "
                      f"p={d['p_sinal_casa'] if d['p_sinal_casa'] is None else round(d['p_sinal_casa'],3)}")


# ---------- ligação com 2026 ----------
# nome nas rodadas de 2026 -> nome na base Pindograma (mesma empresa/linhagem)
MAPA_2026 = {"Veritá": "Veritá", "Quaest": "Quaest", "Gerp": "Gerp", "PoderData": "PoderData",
             "AtlasIntel": "AtlasIntel", "Palver": "Palver", "Futura": "Futura", "Datafolha": "Datafolha",
             "MDA": "MDA", "Instituto França": "Instituto França", "Real Time Big Data": "Real Time Big Data",
             "Nexus": "Nexus", "Ipespe": "Ipespe", "Vox Brasil": None, "DataTrends": None, "Alfa": None,
             "Indexa": None, "Ideia": "Ideia Big Data"}
FLAVIO_2P_1T = 100 * 47.03 / (47.03 + 45.16)  # fatia bipartidária de Flávio no 1º turno (TSE)


def nome_base(inst):
    for k, v in MAPA_2026.items():
        if inst.startswith(k) or k in inst:
            return v
    return None


def ligacao_2026(hist):
    """Compara o efeito de casa histórico pró-PT com (a) o erro de 2026 no 1º turno e (b) o efeito de
    casa no 2º turno de 2026 (resultados/modelo_2t.json). Sinal: positivo = pró-Lula/PT em tudo."""
    import csv
    casa_hist = {d["instituto"]: d for d in hist["institutos"]}
    # todos com n >= 5 para a ligação (o filtro de impressão usa 8)
    t1 = {}
    for r in csv.DictReader(open(R.RAIZ / "dados/rodadas_1t.csv", encoding="utf-8")):
        try:
            fl, lu = R.f(r["flavio"]), R.f(r["lula"])
        except ValueError:  # "nao achado"
            continue
        if fl and lu:
            nm = r["instituto"].split(" 0")[0].split(" 2")[0].split(" (")[0].strip()
            t1.setdefault(nm, []).append(-(100 * fl / (fl + lu) - FLAVIO_2P_1T))  # pró-Lula positivo
    m2 = json.load(open(R.SAIDA / "modelo_2t.json"))["efeito_casa"]
    linhas = []
    def chave(k):  # "CNT/MDA" -> "MDA", "BTG/Nexus" -> "Nexus", "Meio/Ideia" -> "Ideia"
        partes = k.split("/")
        return next((p for p in partes if nome_base(p)), partes[0]).strip()
    m2 = {chave(k): v for k, v in m2.items()}
    for nm in sorted(set(t1) | set(m2)):
        base = nome_base(nm)
        h = casa_hist.get(base) if base else None
        e2 = -m2[nm] if nm in m2 else None
        linhas.append({"instituto_2026": nm, "base_historica": base,
                       "casa_hist_pro_PT": h["casa"] if h else None, "n_hist": h["n"] if h else 0,
                       "erro_1T_2026_pro_Lula": st.mean(t1[nm]) if nm in t1 else None,
                       "casa_2T_2026_pro_Lula": e2})
    def corr(a, b):
        par = [(l[a], l[b]) for l in linhas if l[a] is not None and l[b] is not None]
        return {"n": len(par), "spearman": R.spearman([x for x, _ in par], [y for _, y in par]) if len(par) > 3 else None}
    return {"tabela": linhas,
            "hist_x_1T": corr("casa_hist_pro_PT", "erro_1T_2026_pro_Lula"),
            "hist_x_2T": corr("casa_hist_pro_PT", "casa_2T_2026_pro_Lula"),
            "1T_x_2T": corr("erro_1T_2026_pro_Lula", "casa_2T_2026_pro_Lula")}


def por_ciclo(nomes):
    """Efeito de casa pró-PT médio por ano eleitoral: conta em quantos ciclos o instituto inclinou
    para o mesmo lado (pesquisas de um ciclo compartilham o erro; o ciclo é a unidade conservadora)."""
    ls = [{**l, "pt": e} for l in R.linhas if (e := erro_bipartidario(l, lambda p: p == PT)) is not None]
    disp = defaultdict(list)
    for l in ls:
        disp[(l["ano"], l["turno"], l["cargo"], l["ue"])].append(l)
    por = defaultdict(lambda: defaultdict(list))
    for g in disp.values():
        for l in g:
            outros = [x["pt"] for x in g if x["cid"] != l["cid"]]
            if outros:
                por[l["nome"]][l["ano"]].append(l["pt"] - st.mean(outros))
    out = {}
    for nome in nomes:
        anos = {a: st.mean(v) for a, v in sorted(por[nome].items())}
        k = sum(v > 0 for v in anos.values())
        out[nome] = {"por_ano": anos, "anos_pro_PT": k, "anos_total": len(anos),
                     "p_sinal_ciclos": binom_bilateral(min(k, len(anos) - k), len(anos)) if anos else None}
    return out


if __name__ == "__main__":
    json.dump(por_ciclo(("AtlasIntel", "Vox Populi", "Ipec (antigo Ibope)", "Datafolha", "Quaest", "Veritá",
                         "Paraná Pesquisas", "Brasmarket", "Real Time Big Data", "Futura", "MDA", "Ipespe")),
              open(R.SAIDA / "vies_casa_por_ciclo.json", "w"), ensure_ascii=False, indent=1)
    res_pt = analisa("pt", lambda p: p == PT, nmin=5)
    lig = ligacao_2026(res_pt)
    json.dump(lig, open(R.SAIDA / "vies_ligacao_2026.json", "w"), ensure_ascii=False, indent=1)
    print("\n===== ligação com 2026 (positivo = pró-Lula/PT)")
    for l in lig["tabela"]:
        print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in l.items()})
    print({k: v for k, v in lig.items() if k != "tabela"})
