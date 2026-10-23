"""Acurácia das pesquisas finais do 1º turno de 2026, calculada aqui (não usa o D do Times Brasil).

Valores: válidos publicados pelo próprio instituto quando existem (Gerp e Nexus corrigidos abaixo; o
Times deduziu outros); Instituto França só publicou totais e entra recalculado dos totais; Palver não
publica válidos (marcado). Medidas, todas sobre Flávio e Lula para serem comparáveis entre institutos:
  m3 = Mosteller 3 em dois candidatos (média de |erro| de Flávio e Lula)
  m5 = Mosteller 5, erro na margem Flávio-Lula; A = Martin-Traugott-Kennedy
Registro, campo, n, contratante e confiança vêm do dado aberto do TSE (codigo/confere_tse.py).

Uso: python3 -I codigo/acuracia_1t_2026.py
"""
import csv
import json
import math
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import confere_tse as T  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
ELEICAO = date(2026, 10, 4)
REAL = {"flavio": 47.03, "lula": 45.16}
# válidos publicados pelo instituto (dados/verificacao_fontes.md, linhas 99 e 103)
PUBLICADO = {"Gerp 03/10": {"flavio": 46.0, "lula": 44.0, "registro": "BR-00509/2026",
                            "origem": "válidos publicados pelo instituto (relatório Gerp, campo 30/9-2/10)"},
             "Nexus (BTG)": {"flavio": 39.0, "lula": 44.0, "origem": "válidos publicados pelo instituto (BTG/Nexus)"}}
ORIGEM = {"Instituto França": "recalculado dos totais publicados (o instituto não publica válidos)",
          "Palver": "percentuais publicados pelo instituto, que não divulga válidos",
          "Veritá": "válidos com decimais só na compilação do Times Brasil; o instituto divulgou 47/45 inteiros"}


def f(x):
    try:
        return float(str(x).replace(",", "."))
    except (TypeError, ValueError):
        return None


linhas = []
for r in csv.DictReader(open(RAIZ / "dados/rodadas_1t.csv", encoding="utf-8")):
    rot = r["instituto"].strip()
    pub = PUBLICADO.get(rot, {})
    fl, lu = pub.get("flavio", f(r["flavio"])), pub.get("lula", f(r["lula"]))
    ficha = T.ficha(pub.get("registro", r["registro_tse"]))
    if fl is None or lu is None or ficha is None:
        continue
    if " ou " in r["registro_tse"] and "registro" not in pub:
        continue  # registro ambíguo e não resolvido: fora
    inst = rot.split(" 0")[0].split(" 2")[0].split(" (")[0].strip()
    fim = date.fromisoformat(ficha["fim"])
    linhas.append({
        "instituto": inst, "registro": ficha["registro"], "campo": f"{ficha['inicio']} a {ficha['fim']}",
        "dias_antes": (ELEICAO - fim).days, "n": ficha["n"], "confianca": ficha["confianca"],
        "contratantes": ficha["contratantes"], "margem": ficha["margem"],
        "origem": pub.get("origem") or ORIGEM.get(inst) or "válidos publicados (conferido em dados/verificacao_fontes.md)",
        "flavio": fl, "lula": lu, "erro_flavio": fl - REAL["flavio"], "erro_lula": lu - REAL["lula"],
        "m3": (abs(fl - REAL["flavio"]) + abs(lu - REAL["lula"])) / 2,
        "m5": (fl - lu) - (REAL["flavio"] - REAL["lula"]),
        "A": math.log((fl / lu) / (REAL["flavio"] / REAL["lula"])),
        "erro_bipartidario_flavio": 100 * fl / (fl + lu) - 100 * REAL["flavio"] / (REAL["flavio"] + REAL["lula"]),
    })
ultima = {}
for l in sorted(linhas, key=lambda l: l["campo"][-10:]):
    ultima[l["instituto"]] = l
fim = sorted(ultima.values(), key=lambda l: abs(l["m5"]))
res = {"ultima_por_instituto": fim, "todas": linhas,
       "n_finais": len(fim),
       "flavio_abaixo": sum(l["erro_flavio"] < 0 for l in fim),
       "flavio_abaixo_mais_de_meio_ponto": sum(l["erro_flavio"] < -0.5 for l in fim),
       "lula_sub_sobre_acerto": [sum(l["erro_lula"] < -0.5 for l in fim), sum(l["erro_lula"] > 0.5 for l in fim),
                                 sum(abs(l["erro_lula"]) <= 0.5 for l in fim)],
       "erro_bipartidario_medio_finais": sum(l["erro_bipartidario_flavio"] for l in fim) / len(fim)}
json.dump(res, open(RAIZ / "resultados/acuracia_1t_2026.json", "w"), ensure_ascii=False, indent=1)
for l in fim:
    print(f"{l['instituto'][:18]:18s} {l['registro']} {l['campo']} d={l['dias_antes']:2d} n={l['n']:5d} conf={l['confianca']} "
          f"F={l['flavio']:.1f} L={l['lula']:.1f} m3={l['m3']:.2f} m5={l['m5']:+.2f}")
print({k: v for k, v in res.items() if k not in ("ultima_por_instituto", "todas")})
