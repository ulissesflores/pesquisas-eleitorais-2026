"""Classificação de acurácia dos institutos, 2012-2022, a partir da base aberta do Pindograma.

Replica a junção pesquisa x resultado de pindograma/ranking_de_institutos (GPL-3,
merge_polls_and_election_results.R + pollster_ratings.Rmd) em Python puro e mede,
por pesquisa:
  m3  = Mosteller (1949) medida 3: erro absoluto médio por candidato, em válidos (pp)
  em  = Mosteller medida 5: erro na margem entre os dois primeiros do resultado (pp, com sinal)
  A   = Martin, Traugott & Kennedy (2005) nos dois primeiros: ln[(p1/p2)/(r1/r2)]
O desempenho de cada instituto é relativo aos concorrentes na MESMA disputa (controla a
dificuldade da disputa) e encolhido para a média com peso n/(n+15), como o Pindograma.

Uso: python3 -I codigo/ranking.py   (saídas em resultados/)
"""
import csv
import json
import math
import statistics as st
from collections import defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PG = RAIZ / "dados/externo/pindograma_ranking_de_institutos/data"
SAIDA = RAIZ / "resultados"
SAIDA.mkdir(exist_ok=True)
K_ENCOLHE = 15  # mesmo hiperparâmetro do Pindograma


def f(x):
    if x in (None, "", "NA"):
        return None
    return float(str(x).replace(",", "."))


def d(x):
    return date.fromisoformat(x[:10]) if x and x != "NA" else None


def ler(p):
    with open(p, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ---------- resultados oficiais 2020 e 2022 (válidos, sem 95/96) ----------
votos = {}  # (ano, turno, ue, cargo) -> {numero: votos}
for arq, turno in (("resultados_1t_2020.csv", 1), ("resultados_2t_2020.csv", 2)):
    for r in ler(PG / "resultados" / arq):
        if r["numero"] in ("95", "96"):
            continue
        votos.setdefault((2020, turno, r["codigo_tse"], "11"), {})[r["numero"]] = f(r["votos_validos"])
for r in ler(PG / "resultados/resultados_2022.csv"):
    if r["NR_CANDIDATO"] in ("95", "96"):
        continue
    votos.setdefault((2022, int(r["NR_TURNO"]), r["SG_UF"], r["CD_CARGO"]), {})[r["NR_CANDIDATO"]] = f(r["QT_VOTOS"])
# eleição presidencial nacional 2022 = soma das UFs quando o arquivo não traz a linha 'BR'
if not any(k[2] == "BR" for k in votos if k[0] == 2022):
    agg = defaultdict(lambda: defaultdict(float))
    for (ano, t, _ue, cargo), dic in votos.items():
        if ano == 2022 and cargo == "1":
            for n, v in dic.items():
                agg[t][n] += v
    for t, dic in agg.items():
        votos[(2022, t, "BR", "1")] = dict(dic)

# ---------- empresas: CNPJ -> linhagem ----------
corr = {r["NR_CNPJ_EMPRESA"].strip('"'): r["company_id"] for r in ler(PG / "empresas_multiplos_cnpjs.csv")}
nomes = {r["company_id"].strip('"'): r["pretty_name"] for r in ler(PG / "nomes_empresas.csv")}


def empresa(cnpj):
    cid = corr.get(cnpj, cnpj)
    return cid, nomes.get(cid, cid)


# ---------- pesquisas: agrupa linhas-candidato em pesquisas ----------
def chave_pesq(r):
    return (r["year"], r["turno"], r["NR_IDENTIFICACAO_PESQUISA"], r["NR_CNPJ_EMPRESA"], r["SG_UE"],
            r["polled_UE"], r["CD_CARGO"], r["estimulada"], r.get("vv", ""))


pesquisas = []  # dicts com cand: [(poll_valid, real_pct)]


def adiciona(grupo, real_de):
    """grupo: linhas de um mesmo cenário; real_de(r) -> votos do candidato ou None."""
    r0 = grupo[0]
    if r0["is_complete"] != "TRUE":
        return
    pares = [(f(r["result"]), real_de(r), r["NUMERO_CANDIDATO"]) for r in grupo]
    pares = [(p, v, nr) for p, v, nr in pares if p is not None and v is not None]
    if len(pares) < 2:
        return
    sp, sv = sum(p for p, _, _ in pares), sum(v for _, v, _ in pares)
    if sp <= 0 or sv <= 0:
        return
    pesquisas.append({
        "ano": int(r0["year"]), "turno": int(r0["turno"]), "cargo": r0["CD_CARGO"], "ue": r0["polled_UE"],
        "cnpj": r0["NR_CNPJ_EMPRESA"], "fim": d(r0["DT_FIM_PESQUISA"]),
        "d1": d(r0["first_round_date"]), "d2": d(r0["second_round_date"]),
        "n": f(r0.get("QT_ENTREVISTADOS") or r0.get("QT_ENTREVISTADO")),
        "cand": [(100 * p / sp, 100 * v / sv, nr) for p, v, nr in pares], "sv": sv, "id": r0["NR_IDENTIFICACAO_PESQUISA"],
    })


def processa(linhas, real_de, exige_cobertura):
    grupos = defaultdict(lambda: defaultdict(list))
    for r in linhas:
        grupos[chave_pesq(r)][r["scenario_id"]].append(r)
    for cen in grupos.values():
        if len(cen) != 1:  # o Pindograma descarta pesquisas com vários cenários
            continue
        g = next(iter(cen.values()))
        if exige_cobertura:
            r0 = g[0]
            tot = votos.get((int(r0["year"]), int(r0["turno"]), r0["polled_UE"], r0["CD_CARGO"]))
            if not tot:
                continue
            cobertos = sum(tot.get(r["NUMERO_CANDIDATO"], 0) for r in g)
            if cobertos < 0.90 * sum(tot.values()):
                continue
        adiciona(g, real_de)


# 2012-2018: arquivo já traz o voto real do candidato (QTDE_VOTOS)
processa(ler(PG / "polls/late_polls_2012_2014_2016_2018.csv"), lambda r: f(r["QTDE_VOTOS"]), False)


def real_por_tabela(r):
    tot = votos.get((int(r["year"]), int(r["turno"]), r["polled_UE"], r["CD_CARGO"]))
    return tot.get(r["NUMERO_CANDIDATO"]) if tot else None


processa(ler(PG / "polls/late_polls_2020.csv"), real_por_tabela, True)
processa(ler(PG / "polls/late_polls_2022.csv"), real_por_tabela, True)


# ---------- filtros e medidas ----------
def tipo(p):
    if p["ue"] == "BR":
        return "presidente_BR"
    if p["cargo"] == "1":
        return "presidente_UF"
    if p["cargo"] == "3" and len(p["ue"]) == 2:
        return "governador"
    if p["cargo"] == "11":
        return "prefeito"
    return None


linhas = []
for p in pesquisas:
    t = tipo(p)
    alvo = p["d1"] if p["turno"] == 1 else p["d2"]
    if not t or not p["fim"] or not alvo:
        continue
    dias = abs((alvo - p["fim"]).days)
    if (p["turno"] == 1 and dias > 21) or (p["turno"] == 2 and dias > 14):
        continue
    c = sorted(p["cand"], key=lambda x: -x[1])
    if c[0][1] == 0 or c[1][1] == 0 or c[0][0] <= 0 or c[1][0] <= 0:
        continue
    m3 = st.mean(abs(pv - rv) for pv, rv, _ in p["cand"])
    em = (c[0][0] - c[1][0]) - (c[0][1] - c[1][1])
    A = math.log((c[0][0] / c[1][0]) / (c[0][1] / c[1][1]))
    cid, nome = empresa(p["cnpj"])
    linhas.append({**{k: p[k] for k in ("ano", "turno", "cargo", "ue", "n", "id")}, "tipo": t, "dias": dias,
                   "cid": cid, "nome": nome, "m3": m3, "em": em, "A": A,
                   "top2": [(c[0][0], c[0][1], c[0][2]), (c[1][0], c[1][1], c[1][2])]})

# desempenho relativo na mesma disputa (média dos OUTROS institutos)
por_disputa = defaultdict(list)
for l in linhas:
    por_disputa[(l["ano"], l["turno"], l["cargo"], l["ue"])].append(l)
for grupo in por_disputa.values():
    for l in grupo:
        outros = [o for o in grupo if o["cid"] != l["cid"]]
        l["n_rivais"] = len({o["cid"] for o in outros})
        l["rel_m3"] = l["m3"] - st.mean(o["m3"] for o in outros) if outros else None
        l["rel_em"] = abs(l["em"]) - st.mean(abs(o["em"]) for o in outros) if outros else None


def classifica(ls, campo, k=K_ENCOLHE, nmin=5):
    ls = [l for l in ls if l[campo] is not None]
    media = st.mean(l[campo] for l in ls)
    por = defaultdict(list)
    for l in ls:
        por[(l["cid"], l["nome"])].append(l)
    out = []
    for (cid, nome), v in por.items():
        n = len(v)
        if n < nmin:
            continue
        m = st.mean(x[campo] for x in v)
        out.append({"instituto": nome, "id": cid, "n_pesquisas": n,
                    "n_disputas": len({(x["ano"], x["turno"], x["cargo"], x["ue"]) for x in v}),
                    "anos": f"{min(x['ano'] for x in v)}-{max(x['ano'] for x in v)}",
                    "media": m, "encolhido": media + (m - media) * n / (n + k),
                    "m3_bruto": st.mean(x["m3"] for x in v), "em_abs_bruto": st.mean(abs(x["em"]) for x in v)})
    out.sort(key=lambda r: r["encolhido"])
    return out, media


def spearman(a, b):
    def postos(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for pos, i in enumerate(o):
            r[i] = pos + 1
        return r
    return st.correlation(postos(a), postos(b)) if len(a) > 2 else float("nan")


def persistencia(ls, campo, corte):
    """Correlação de postos entre o desempenho médio antes e depois do ano de corte."""
    a, b = defaultdict(list), defaultdict(list)
    for l in ls:
        if l[campo] is None:
            continue
        (a if l["ano"] < corte else b)[l["cid"]].append(l[campo])
    comuns = [c for c in a if c in b and len(a[c]) >= 5 and len(b[c]) >= 5]
    return {"corte": corte, "n_institutos": len(comuns),
            "spearman": spearman([st.mean(a[c]) for c in comuns], [st.mean(b[c]) for c in comuns])}


if __name__ == "__main__":
    res = {"n_pesquisas": len(linhas), "n_disputas": len(por_disputa),
           "por_tipo": {t: sum(1 for l in linhas if l["tipo"] == t) for t in sorted({l["tipo"] for l in linhas})},
           "por_ano": {a: sum(1 for l in linhas if l["ano"] == a) for a in sorted({l["ano"] for l in linhas})}}
    for campo in ("rel_m3", "rel_em"):
        rk, media = classifica(linhas, campo)
        res[f"ranking_{campo}"] = rk
        res[f"persist_{campo}"] = [persistencia(linhas, campo, c) for c in (2016, 2018, 2020, 2022)]
    # 2º turno apenas (mais próximo do problema de 25/10)
    rk2, _ = classifica([l for l in linhas if l["turno"] == 2], "rel_em", nmin=3)
    res["ranking_rel_em_2turno"] = rk2
    # validação da replicação contra o ranking publicado pelo Pindograma (24/09/2024)
    pub = {r["company_id"]: r for r in csv.DictReader(open(
        RAIZ / "dados/externo/pindograma_site_ranking/ranking_2024-09-24.csv", encoding="utf-8"))}
    par = [(r["m3_bruto"], float(pub[r["id"]]["avg"]), r["n_pesquisas"], int(pub[r["id"]]["n"]))
           for r in res["ranking_rel_m3"] if r["id"] in pub]
    res["validacao_pindograma"] = {
        "institutos_casados": len(par), "corr_erro_medio": st.correlation([a for a, _, _, _ in par], [b for _, b, _, _ in par]),
        "corr_n_pesquisas": st.correlation([c for _, _, c, _ in par], [d for _, _, _, d in par]),
        "cobertura_pesquisas": sum(c for _, _, c, _ in par) / sum(d for _, _, _, d in par)}
    json.dump(res, open(SAIDA / "ranking_2012_2022.json", "w"), ensure_ascii=False, indent=1, default=str)
    with open(SAIDA / "pesquisas_avaliadas_2012_2022.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=[k for k in linhas[0] if k != "top2"], extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    print(json.dumps({k: v for k, v in res.items() if not k.startswith("ranking")}, ensure_ascii=False, indent=1))
    alvos = ("Datafolha", "Quaest", "AtlasIntel", "Ipec", "Paraná", "PoderData", "Real Time", "Futura", "Gerp",
             "Veritá", "Palver", "Nexus", "MDA", "França", "Ipespe", "Vox Populi", "Ideia")
    for campo in ("rel_em", "rel_m3"):
        rk = res[f"ranking_{campo}"]
        print(f"\n== {campo}: {len(rk)} institutos com >=5 pesquisas ==")
        for i, r in enumerate(rk, 1):
            if i <= 10 or i > len(rk) - 10 or any(a in r["instituto"] for a in alvos):
                print(f"{i:3d} {r['instituto'][:32]:32s} n={r['n_pesquisas']:4d} disp={r['n_disputas']:4d} "
                      f"{r['anos']} enc={r['encolhido']:+.2f} bruto={r['media']:+.2f} m3={r['m3_bruto']:.2f} |em|={r['em_abs_bruto']:.2f}")
