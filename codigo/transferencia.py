"""Transferência dos votos dos eliminados no 1º turno de 2026 (hipótese estrutural, não evidência
independente do agregado: as taxas saem das mesmas amostras das pesquisas de 2º turno).

Premissas: quem votou em Flávio ou Lula repete; comparecimento igual; o resto de cada eliminado vai
para branco, nulo ou abstenção. Taxas: Quaest 21/10 e PoderData/Aya (dados/verificacao_fontes.md, item 4).
Uso: python3 -I codigo/transferencia.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
F0, L0 = 56_104_503, 53_879_538  # TSE, 1º turno
VOTOS = {"Cury": 3_448_569, "Renan": 2_675_887, "Caiado": 2_605_148, "Zema": 326_488, "Demais": 260_655}
TAXAS = {
    "Quaest 21/10": {"Cury": (.33, .48), "Renan": (.51, .25), "Caiado": (.57, .21), "Zema": (.72, .10), "Demais": (.15, .55)},
    "PoderData/Aya": {"Cury": (.56, .27), "Renan": (.48, .25), "Caiado": (.57, .19), "Zema": (.72, .10), "Demais": (.15, .55)},
}
NOTA = "Zema: só PoderData/Aya; Demais: suposição do autor (15% Flávio, 55% Lula), igual nos dois cenários"

res = {"nota": NOTA}
for nome, tx in TAXAS.items():
    gf = sum(VOTOS[k] * tx[k][0] for k in VOTOS)
    gl = sum(VOTOS[k] * tx[k][1] for k in VOTOS)
    res[nome] = {"ganho_flavio": gf, "ganho_lula": gl, "fatia_flavio": 100 * (F0 + gf) / (F0 + gf + L0 + gl)}
json.dump(res, open(RAIZ / "resultados/transferencia.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
