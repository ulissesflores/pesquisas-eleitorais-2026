"""Gera os datasets dos gráficos do artigo no site (formato `CountryBarsDataset` de
`data/artigos-charts.ts` do ulissesflores.com) a partir de resultados/*.json.

Nenhum número é digitado à mão. Saída: site/material/pesquisas-2026.data.ts
Uso: python3 -I codigo/site_charts.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
OUT = RAIZ / "site/material"
OUT.mkdir(parents=True, exist_ok=True)
OURO, CINZA = "#a48f65", "#d4d4d8"  # paleta da casa (comentário de data/artigos-charts.ts)


def j(n):
    return json.load(open(RES / n, encoding="utf-8"))


def br(x, nd=1, sinal=False):
    if round(x, nd) == 0:
        x = 0.0  # evita "−0,0"
    s = f"{x:+.{nd}f}" if sinal and x != 0 else f"{x:.{nd}f}"
    return s.replace(".", ",").replace("-", "−")


NOMES = {"Ibope->Ipec": "Ibope/Ipec", "Paraná Pesquisas": "Paraná Pesquisas", "DataPoder360->PoderData": "PoderData",
         "Atlas Político->AtlasIntel": "AtlasIntel", "Quaest (Genial/Quaest)": "Quaest",
         "Ipec (antigo Ibope)": "Ibope/Ipec", "Real Time Big Data": "Real Time Big Data"}

ds = {}
pr = j("probabilidade.json")

# 1. erro do agregado por eleição, 1º x 2º turno (só anos com 2+ institutos)
g1, g2 = [], []
for ano, v in pr["erro_agregado_1T_por_ano"].items():
    if v["k"] >= 2 and int(ano) >= 2002:
        g1.append({"name": ano, "value": round(abs(v["erro"]), 2), "valueLabel": f"{br(v['erro'],1,True)} pp"})
for ano, v in pr["erro_agregado_2T_por_ano"].items():
    if v["k"] >= 2:
        g2.append({"name": ano, "value": round(abs(v["erro"]), 2), "valueLabel": f"{br(v['erro'],1,True)} pp"})
ds["pesquisas-2026-erro-1t-2t"] = {"max": 8, "groups": [
    {"label": "1º turno · erro da média das pesquisas finais", "color": OURO, "items": g1},
    {"label": "2º turno · erro da média das pesquisas finais", "color": CINZA, "items": g2}]}

# 2. acerto no 2º turno presidencial por linhagem
rp = sorted(j("ranking_presidencial_1989_2026.json")["2turno"]["tabela"], key=lambda d: d["erro_abs_medio"])
ds["pesquisas-2026-acerto-2t"] = {"max": 3.5, "groups": [{
    "label": "Erro médio no 2º turno presidencial (pp) · eleições", "color": OURO,
    "items": [{"name": NOMES.get(d["linhagem"], d["linhagem"]), "value": round(d["erro_abs_medio"], 2),
               "valueLabel": f"{br(d['erro_abs_medio'])} · {d['n']}", "emphasis": i < 3}
              for i, d in enumerate(rp)]}]}

# 3. efeito de casa na fatia do PT, 2012-2022, institutos com 2+ ciclos
casa = {d["instituto"]: d for d in j("vies_direcao_2012_2022.json")["pt"]["institutos"]}
ciclo = j("vies_casa_por_ciclo.json")
abaixo, acima = [], []
for nome, c in ciclo.items():
    d = casa.get(nome)
    if not d or c["anos_total"] < 2 or d["casa"] is None:
        continue
    item = {"name": NOMES.get(nome, nome), "value": round(abs(d["casa"]), 2),
            "valueLabel": f"{br(d['casa'],1,True)} · {c['anos_pro_PT']}/{c['anos_total']}",
            "emphasis": c["anos_pro_PT"] in (0, c["anos_total"])}
    (abaixo if d["casa"] < 0 else acima).append(item)
abaixo.sort(key=lambda x: -x["value"])
acima.sort(key=lambda x: -x["value"])
ds["pesquisas-2026-casa-pt"] = {"max": 5, "groups": [
    {"label": "Abaixo dos rivais na fatia do PT (pp · ciclos a favor)", "color": CINZA, "items": abaixo},
    {"label": "Acima dos rivais na fatia do PT (pp · ciclos a favor)", "color": OURO, "items": acima}]}

# 4. cenários para 25/10
ROT = [("CENTRAL: mediana da última rodada", "sem viés", "Central: mediana"),
       ("mediana dos institutos com >=20 pesquisas 2012-2022", "sem viés", "Só quem tem 20+"),
       ("mediana dos 4 institutos que erraram menos que os rivais em 2012-2022", "sem viés", "Os 4 mais precisos"),
       ("mediana sem as 3 maiores para Flávio", "sem viés", "Sem os 3 mais altos"),
       ("CENTRAL", "sigma calibrado em 14 dias", "Erro de 14 dias"),
       ("tendência + casa, janela desde 15/10", "sem viés", "Estável desde 15/10"),
       ("tendência + casa, janela desde 05/10", "sem viés", "Queda continua")]
cen = []
for centro, vies, nome in ROT:
    c = next(c for c in pr["cenarios"] if c["centro"] == centro and (vies in c["rotulo_vies"]) and ("14 dias" in c["rotulo_vies"]) == ("14 dias" in vies))
    cen.append({"name": nome, "value": round(100 * c["P_t"]), "valueLabel": f"{round(100 * c['P_t'])}%",
                "emphasis": nome.startswith("Central")})
ds["pesquisas-2026-cenarios"] = {"max": 100, "groups": [
    {"label": "Probabilidade de Flávio vencer, por cenário", "color": OURO, "items": cen}]}

ts = ("/**\n * Datasets do artigo `pesquisas-eleitorais-2026` (CountryBarsChart).\n"
      " * PROCEDÊNCIA: gerado por codigo/site_charts.py a partir de resultados/*.json do repositório\n"
      " * companion (pesquisas finais presidenciais 1989-2026, base Pindograma 2012-2022, rodadas de\n"
      " * 2º turno 2026 com registro conferido no dado aberto do TSE). Não editar à mão.\n */\n")
for k, v in ds.items():
    ts += f"  '{k}': {json.dumps(v, ensure_ascii=False, indent=2)},\n"
(OUT / "pesquisas-2026.data.ts").write_text(ts, encoding="utf-8")
json.dump(ds, open(OUT / "pesquisas-2026.data.json", "w"), ensure_ascii=False, indent=1)
for k, v in ds.items():
    print(k, [(i["name"], i["valueLabel"]) for g in v["groups"] for i in g["items"]])
