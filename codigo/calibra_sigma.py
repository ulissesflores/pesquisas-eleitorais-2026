"""Calibra o erro sistemático de um 2º turno: erro do AGREGADO (média dos institutos) por disputa.

Base: pesquisas finais 2012-2022 (codigo/ranking.py). Para cada disputa de 2º turno, erro com sinal
na fatia bipartidária do 1º colocado do resultado, média entre as pesquisas dos últimos 7 e 14 dias.
O desvio-padrão dessas médias entre disputas é o sigma empírico do erro do agregado.

Uso: python3 -I codigo/calibra_sigma.py
"""
import json
import math
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ranking as R  # noqa: E402


def erro_lider(l):
    (p1, r1, _), (p2, r2, _) = l["top2"]
    return 100 * p1 / (p1 + p2) - 100 * r1 / (r1 + r2)


def resumo(xs):
    xs = sorted(xs)
    return {"n_disputas": len(xs), "media_sinal": st.mean(xs), "dp": st.stdev(xs),
            "rmse": math.sqrt(st.mean(x * x for x in xs)), "mediana_abs": st.median(abs(x) for x in xs),
            "p90_abs": sorted(abs(x) for x in xs)[int(0.9 * len(xs))],
            "frac_abs_maior_2": sum(abs(x) > 2 for x in xs) / len(xs)}


if __name__ == "__main__":
    out = {}
    for turno in (1, 2):
        for janela in (7, 14):
            for tipos in (("presidente_BR",), ("governador",), ("prefeito",), ("governador", "prefeito", "presidente_BR")):
                d = defaultdict(list)
                for l in R.linhas:
                    if l["turno"] == turno and l["dias"] <= janela and l["tipo"] in tipos:
                        d[(l["ano"], l["cargo"], l["ue"])].append(erro_lider(l))
                # agregado só quando há >= 2 institutos distintos (simula média de pesquisas)
                ag = [st.mean(v) for k, v in d.items() if len(v) >= 2]
                if len(ag) >= 3:
                    out[f"T{turno}_{janela}d_{'+'.join(tipos)}"] = resumo(ag)
    json.dump(out, open(R.SAIDA / "calibra_sigma.json", "w"), ensure_ascii=False, indent=1)
    for k, v in out.items():
        print(f"{k:45s} " + " ".join(f"{a}={b:.2f}" if isinstance(b, float) else f"{a}={b}" for a, b in v.items()))
