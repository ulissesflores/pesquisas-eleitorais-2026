"""Agregado do 2º turno de 2026 (Flávio x Lula) e probabilidade de vitória.

Entrada: dados/rodadas_2t.csv (uma linha por rodada, com registro TSE).
Estimadores do centro (fatia de Flávio nos válidos):
  1. mediana e média da última rodada de cada instituto
  2. média ponderada por recência (meia-vida de 4 dias) e por raiz de n
  3. tendência linear comum + efeito fixo de instituto (house effect), projetada para 25/10
Probabilidade: P(V > 50), V ~ centro + viés + erro, com erro sistemático calibrado no histórico
(dados/historico_erros.csv) e cauda normal e t de Student.

Uso: python3 -I codigo/modelo_2t.py
"""
import csv
import json
import math
import random
import statistics as st
from collections import defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "resultados"
SAIDA.mkdir(exist_ok=True)
ELEICAO = date(2026, 10, 25)
N = st.NormalDist()
# Rodadas fora do agregado, com motivo (citadas no artigo, mas sem entrar no centro)
EXCLUIR = {"Alfa Inteligencia": "registro BR-08496/2026 tem n = 1.200 no TSE, mas a reportagem atribui n = 2.700, "
                                "que é o do BR-00820/2026: atribuição do resultado ao registro em conflito"}


def f(x):
    try:
        return float(str(x).replace(",", ".").replace("%", "").strip())
    except (TypeError, ValueError):
        return None


def carrega():
    rod = []
    for r in csv.DictReader(open(RAIZ / "dados/rodadas_2t.csv", encoding="utf-8")):
        fv, lv = f(r["flavio_valido"]), f(r["lula_valido"])
        ft, lt = f(r["flavio_total"]), f(r["lula_total"])
        if ft and lt:  # recalcula válidos a partir dos totais (mais casas que o arredondado divulgado)
            v, origem = 100 * ft / (ft + lt), "total"
        elif fv and lv:
            v, origem = 100 * fv / (fv + lv), "valido"
        else:
            continue
        fim = date.fromisoformat(r["campo_fim"])
        if r["instituto"].strip() in EXCLUIR:
            continue
        rod.append({"inst": r["instituto"].strip(), "fim": fim, "dias": (ELEICAO - fim).days, "v": v,
                    "origem": origem, "n": f(r["n"]) or 1000, "reg": r["registro_tse"], "modo": r["modo"]})
    return rod


def ultima_por_instituto(rod):
    u = {}
    for r in sorted(rod, key=lambda r: r["fim"]):
        u[r["inst"]] = r
    return list(u.values())


def mmq(X, y):
    """Mínimos quadrados por equações normais (eliminação de Gauss); X lista de linhas."""
    k = len(X[0])
    A = [[sum(X[i][a] * X[i][b] for i in range(len(X))) for b in range(k)] for a in range(k)]
    c = [sum(X[i][a] * y[i] for i in range(len(X))) for a in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(A[r][col]))
        A[col], A[piv], c[col], c[piv] = A[piv], A[col], c[piv], c[col]
        for r in range(k):
            if r != col and A[col][col]:
                fat = A[r][col] / A[col][col]
                A[r] = [A[r][j] - fat * A[col][j] for j in range(k)]
                c[r] -= fat * c[col]
    return [c[i] / A[i][i] for i in range(k)]


def tendencia_com_casa(rod):
    """v = a + b*dias_antes + efeito_instituto (soma zero). Retorna (centro em 25/10, b, efeitos)."""
    insts = sorted({r["inst"] for r in rod})
    ref = insts[-1]
    X, y = [], []
    for r in rod:
        linha = [1.0, -r["dias"]]  # b > 0 = Flávio subindo ao longo do tempo
        for i in insts[:-1]:
            linha.append(1.0 if r["inst"] == i else (-1.0 if r["inst"] == ref else 0.0))
        X.append(linha)
        y.append(r["v"])
    beta = mmq(X, y)
    efeitos = dict(zip(insts[:-1], beta[2:], strict=True))
    efeitos[ref] = -sum(beta[2:])
    resid = [y[i] - sum(X[i][j] * beta[j] for j in range(len(beta))) for i in range(len(y))]
    return beta[0], beta[1], efeitos, st.pstdev(resid)


def bootstrap_institutos(rod, reps=2000, seed=11):
    """Reamostra institutos (não rodadas) para a incerteza do centro com tendência."""
    rnd = random.Random(seed)
    por = defaultdict(list)
    for r in rod:
        por[r["inst"]].append(r)
    nomes = list(por)
    centros = []
    for _ in range(reps):
        amostra = []
        for j, nm in enumerate(rnd.choices(nomes, k=len(nomes))):
            amostra += [{**r, "inst": f"{nm}#{j}"} for r in por[nm]]
        if len({r["fim"] for r in amostra}) < 3:
            continue
        try:
            centros.append(tendencia_com_casa(amostra)[0])
        except ZeroDivisionError:
            continue
    centros.sort()
    return centros[int(0.025 * len(centros))], centros[int(0.975 * len(centros))], st.pstdev(centros)


def p_normal(mu, sigma):
    return N.cdf((mu - 50) / sigma)


def p_t(mu, sigma, gl=4, sims=200_000, seed=3):
    rnd = random.Random(seed)
    esc = sigma / math.sqrt(gl / (gl - 2))
    return sum(mu + esc * rnd.gauss(0, 1) / math.sqrt(rnd.gammavariate(gl / 2, 2) / gl) > 50
               for _ in range(sims)) / sims


if __name__ == "__main__":
    rod = carrega()
    ult = ultima_por_instituto(rod)
    vs = [r["v"] for r in ult]
    w = [0.5 ** (r["dias"] / 4) * math.sqrt(r["n"]) for r in ult]
    centro_t, inclin, casas, sd_res = tendencia_com_casa(rod)
    lo, hi, sd_boot = bootstrap_institutos(rod)
    res = {
        "n_rodadas": len(rod), "n_institutos": len(ult), "excluidas": EXCLUIR,
        "ultima_rodada": sorted([{k: r[k] for k in ("inst", "fim", "dias", "v", "origem", "reg")} for r in ult],
                                key=lambda r: -r["v"]),
        "mediana": st.median(vs), "media": st.mean(vs), "dp_entre_institutos": st.stdev(vs),
        "media_recencia_n": sum(a * b for a, b in zip(vs, w, strict=True)) / sum(w),
        "tendencia": {"centro_25_10": centro_t, "pp_por_dia": inclin, "dp_residuo": sd_res,
                      "ic95_bootstrap_institutos": [lo, hi], "dp_bootstrap": sd_boot},
        # sensibilidade da tendência à janela (a queda pode ser só ressaca do 1º turno)
        "tendencia_por_janela": {
            ini: dict(zip(("centro_25_10", "pp_por_dia"), tendencia_com_casa(
                [r for r in rod if r["fim"] >= date.fromisoformat(ini)])[:2], strict=True))
            for ini in ("2026-10-05", "2026-10-12", "2026-10-15", "2026-10-18")
        },
        "efeito_casa": dict(sorted(casas.items(), key=lambda kv: kv[1])),
        "institutos_com_lula_a_frente": [r["inst"] for r in ult if r["v"] < 50],
    }
    json.dump(res, open(SAIDA / "modelo_2t.json", "w"), ensure_ascii=False, indent=1, default=str)
    print(json.dumps(res, ensure_ascii=False, indent=1, default=str))
