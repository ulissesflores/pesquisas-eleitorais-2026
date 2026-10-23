"""Classificação presidencial 1989-2026 por linhagem de instituto (nomes antigos e novos juntos).

Medida: erro com sinal na fatia de votos válidos do candidato de direita/PSDB na última pesquisa
de cada instituto (dados/historico_erros.csv, 1989-2022) e de Flávio no 1º turno de 2026
(dados/rodadas_1t.csv; resultado TSE 47,03). |erro| mede acerto; o sinal mede a direção.
Encolhimento para a média com peso n/(n+3): com poucas eleições por instituto, sorte pesa muito.

Uso: python3 -I codigo/ranking_presidencial.py
"""
import csv
import json
import math
import statistics as st
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "resultados"
K = 3
DIAS_MAX = 7    # mesma janela da calibração de sigma (codigo/probabilidade.py)
EMPATE = 0.5    # |erro| <= 0,5 pp é arredondamento de número inteiro, não direção

# rótulo de 2026 -> linhagem usada em historico_erros.csv
LINHAGEM_2026 = {"Quaest": "Quaest (Genial/Quaest)", "AtlasIntel": "Atlas Político->AtlasIntel",
                 "PoderData": "DataPoder360->PoderData", "MDA": "MDA", "Nexus": "Nexus", "Veritá": "Veritá",
                 "Gerp": "Gerp", "Datafolha": "Datafolha", "Palver": "Palver", "Futura": "Futura",
                 "Instituto França": "Instituto França", "Real Time Big Data": "Real Time Big Data"}


def f(x):
    try:
        return float(str(x).replace(",", "."))
    except (TypeError, ValueError):
        return None


def binom_bilateral(k, n):
    pk = [math.comb(n, i) / 2 ** n for i in range(n + 1)]
    return min(1.0, sum(p for p in pk if p <= pk[k] + 1e-12))


linhas = []
for r in csv.DictReader(open(RAIZ / "dados/historico_erros.csv", encoding="utf-8")):
    e, dias = f(r["erro_sinal_pp"]), f(r.get("dias_antes_eleicao"))
    if e is not None and dias is not None and dias <= DIAS_MAX:
        linhas.append({"ano": int(r["ano"]), "turno": int(r["turno"]), "linhagem": r["linhagem"].strip(),
                       "nome": r["instituto"].strip(), "erro": e})
ult = {}
for r in csv.DictReader(open(RAIZ / "dados/rodadas_1t.csv", encoding="utf-8")):
    fl = f(r["flavio"])
    if fl is None:
        continue
    base = next((v for k, v in LINHAGEM_2026.items() if r["instituto"].startswith(k)), None)
    if base and (base not in ult or r["campo_fim"] >= ult[base]["fim"]):
        ult[base] = {"ano": 2026, "turno": 1, "linhagem": base, "nome": r["instituto"].split(" 0")[0],
                     "erro": fl - 47.03, "fim": r["campo_fim"]}
linhas += list(ult.values())


def relativo(ls):
    """|erro| menos o |erro| médio dos OUTROS institutos no mesmo ano e turno (controla a dificuldade)."""
    grupo = defaultdict(list)
    for l in ls:
        grupo[(l["ano"], l["turno"])].append(l)
    for g in grupo.values():
        for l in g:
            outros = [abs(o["erro"]) for o in g if o is not l]
            l["rel"] = abs(l["erro"]) - st.mean(outros) if outros else None


def tabela(ls, nmin=2):
    media = st.mean(abs(l["erro"]) for l in ls)
    por = defaultdict(list)
    for l in ls:
        por[l["linhagem"]].append(l)
    out = []
    for lin, v in por.items():
        if len(v) < nmin:
            continue
        n = len(v)
        m = st.mean(abs(x["erro"]) for x in v)
        pos = sum(1 for x in v if x["erro"] > EMPATE)
        neg = sum(1 for x in v if x["erro"] < -EMPATE)
        rels = [x["rel"] for x in v if x.get("rel") is not None]
        out.append({"linhagem": lin, "nomes": sorted({x["nome"] for x in v}), "n": n,
                    "rel_medio": st.mean(rels) if rels else None,
                    "eleicoes": sorted({f"{x['ano']}/{x['turno']}T" for x in v}),
                    "erro_abs_medio": m, "erro_abs_encolhido": media + (m - media) * n / (n + K),
                    "vies_medio_pro_direita": st.mean(x["erro"] for x in v),
                    "n_pro_direita": pos, "n_pro_esquerda": neg, "n_empate": n - pos - neg,
                    "p_sinal": binom_bilateral(min(pos, neg), pos + neg) if pos + neg else None})
    out.sort(key=lambda d: d["erro_abs_encolhido"])
    return out, media


if __name__ == "__main__":
    relativo(linhas)
    res = {}
    for rot, filtro in (("todos", lambda l: True), ("2turno", lambda l: l["turno"] == 2),
                        ("1turno", lambda l: l["turno"] == 1)):
        tab, media = tabela([l for l in linhas if filtro(l)])
        res[rot] = {"media_geral_abs": media, "tabela": tab}
    json.dump(res, open(SAIDA / "ranking_presidencial_1989_2026.json", "w"), ensure_ascii=False, indent=1)
    for rot, r in res.items():
        print(f"\n== {rot}: erro absoluto médio geral {r['media_geral_abs']:.2f} pp")
        for i, d in enumerate(r["tabela"], 1):
            print(f"{i:2d} {d['linhagem'][:28]:28s} n={d['n']:2d} |e|={d['erro_abs_medio']:.2f} enc={d['erro_abs_encolhido']:.2f} "
                  f"viés={d['vies_medio_pro_direita']:+.2f} dir/esq={d['n_pro_direita']}/{d['n_pro_esquerda']} "
                  f"p={d['p_sinal']:.2f} {','.join(d['eleicoes'])[:70]}")
