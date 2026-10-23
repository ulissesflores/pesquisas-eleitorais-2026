"""Capa sem texto, tirada dos dados (padrão da casa desde 30/08/2026: 1 arquivo serve os 5 idiomas).

Cada ponto é uma rodada de 2º turno de 2026 (x = fim do campo, y = fatia de Flávio nos válidos);
a linha tracejada é o empate (50%); a faixa é a mediana +- 1,25 pp, o erro quadrático médio da
média das pesquisas nos 2º turnos presidenciais 2002-2022. Saída: site/material/hero.png (2400x1260).
Uso: python3 -I codigo/capa.py
"""
import json
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import modelo_2t as M  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
W, H = 2400, 1260
FUNDO, PAINEL, GRADE, OURO, CINZA = "#0f1c2a", "#131a22", "#243241", "#a48f65", "#d4d4d8"

rod = M.carrega()
pr = json.load(open(RAIZ / "resultados/probabilidade.json"))
centro, rms = pr["centro_ref"], pr["sigma_rms_2T"]
x0, x1 = date(2026, 10, 5), date(2026, 10, 25)
y0, y1 = 48.5, 55.8
L, R, T, B = 200, 2200, 170, 1090


def px(d):
    return L + (R - L) * (d - x0).days / (x1 - x0).days


def py(v):
    return B - (B - T) * (v - y0) / (y1 - y0)


img = Image.new("RGB", (W, H), FUNDO)
dr = ImageDraw.Draw(img, "RGBA")
dr.rounded_rectangle((140, 110, 2260, 1150), radius=36, fill=PAINEL)
for v in (49, 50, 51, 52, 53, 54, 55):
    dr.line((L, py(v), R, py(v)), fill=GRADE, width=2)
# faixa do erro histórico do 2º turno em volta da mediana
dr.rectangle((L, py(centro + rms), R, py(centro - rms)), fill=(164, 143, 101, 64))
dr.line((L, py(centro), R, py(centro)), fill=(164, 143, 101, 150), width=4)
# empate em 50%, tracejado
x = L
while x < R:
    dr.line((x, py(50), min(x + 26, R), py(50)), fill=CINZA, width=5)
    x += 44
# rodadas
for r in rod:
    cx, cy = px(r["fim"]), py(r["v"])
    rad = 13 + min(r["n"], 6000) / 600
    cor = OURO if r["v"] >= 50 else CINZA
    dr.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=cor, outline=PAINEL, width=4)
# dia da eleição
dr.line((px(x1) - 2, T, px(x1) - 2, B), fill=(212, 212, 216, 90), width=3)
saida = RAIZ / "site/material/hero.png"
saida.parent.mkdir(parents=True, exist_ok=True)
img.save(saida, optimize=True)
print(saida, img.size, saida.stat().st_size)
