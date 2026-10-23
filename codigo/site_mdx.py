"""Monta site/material/index.pt-br.mdx a partir de site/index.pt-br.src.mdx e resultados/*.json.

Todo número e toda tabela do artigo do site sai daqui; marcador {{X}} sem valor reprova.
Uso: python3 -I codigo/site_mdx.py
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
REPO = "https://github.com/ulissesflores/pesquisas-eleitorais-2026"
# quantis da t de Student com 6 graus de liberdade (tabela padrão): 90% e 97,5%
T6_90, T6_975 = 1.440, 2.447


from tabelas_art10 import br, milhar, tab1, tab2  # noqa: E402


def j(n):
    """Lê um JSON de resultados/."""
    return json.load(open(RES / n, encoding="utf-8"))


m2, pr, a1 = j("modelo_2t.json"), j("probabilidade.json"), j("acuracia_1t_2026.json")
rk, vd, ciclo = j("ranking_2012_2022.json"), j("vies_direcao_2012_2022.json"), j("vies_casa_por_ciclo.json")
lig, tr = j("vies_ligacao_2026.json"), j("transferencia.json")

# cenários
CEN = [("CENTRAL: mediana da última rodada", "sem viés", "Central", "a mediana de todos os institutos"),
       ("mediana dos institutos com >=20 pesquisas 2012-2022", "sem viés", "Só quem tem histórico",
        "só os 8 institutos com 20 ou mais pesquisas finais em 2012-2022"),
       ("mediana dos 4 institutos que erraram menos que os rivais em 2012-2022", "sem viés", "Os mais precisos",
        "só os 4 institutos que erraram menos que os rivais em 2012-2022"),
       ("mediana sem as 3 maiores para Flávio", "sem viés", "Sem os mais altos", "tira as 3 rodadas mais favoráveis a Flávio"),
       ("CENTRAL", "sigma calibrado em 14 dias", "Erro maior", "erro calibrado com pesquisas de até 14 dias"),
       ("tendência + casa, janela desde 15/10", "sem viés", "Estável", "o quadro está parado desde 15/10"),
       ("tendência + casa, janela desde 05/10", "sem viés", "Queda continua", "o recuo de Flávio do início de outubro seguiu até domingo")]
lin = []
for centro, vies, nome, supoe in CEN:
    c = next(c for c in pr["cenarios"] if c["centro"] == centro and vies in c["rotulo_vies"]
             and ("14 dias" in c["rotulo_vies"]) == ("14 dias" in vies))
    lin.append(f"| {nome} | {supoe} | {br(c['mu'])}% | **{round(100 * c['P_t'])}%** |")
cenarios = {c["centro"] + c["rotulo_vies"]: c for c in pr["cenarios"]}
central = next(c for c in pr["cenarios"] if c["centro"].startswith("CENTRAL:") and c["rotulo_vies"] == "sem viés")
repete = next(c for c in pr["cenarios"] if "se repete" in c["rotulo_vies"])
p_todos = [c["P_t"] for c in pr["cenarios"] if c["rotulo_vies"].startswith("sem viés")]

vals = [r["v"] for r in m2["ultima_rodada"]]
s, mu = pr["sigma_total"], pr["centro_ref"]
pc = central["P_t"]
V = {
    "N_RODADAS": m2["n_rodadas"], "N_INST": m2["n_institutos"], "MEDIANA": br(m2["mediana"]), "MEDIANA_LULA": br(100 - m2["mediana"]),
    "MEDIA": br(m2["media"]), "AMPLITUDE": br(max(vals) - min(vals)), "P_CENTRAL": round(100 * pc),
    "P_MIN": round(100 * min(p_todos)), "ANOS": 37,
    "VOX": f"Vox Brasil, {br(min(vals))}% para Flávio",
    "N_FINAIS_1T": a1["n_finais"], "LULA_SUB": a1["lula_sub_sobre_acerto"][0], "LULA_SOBRE": a1["lula_sub_sobre_acerto"][1],
    "LULA_ACERTO": a1["lula_sub_sobre_acerto"][2], "VIES_2T": br(pr["vies_medio_2T_direita"]), "EP_VIES": f"±{br(pr['ep_vies'])}",
    "RMS": br(pr["sigma_rms_2T"], 2), "RMS14": br(pr["sigma_rms_2T_14dias"], 2), "CORR_1T_2T": br(pr["corr_erro_1T_x_2T_mesmo_ano"], 2),
    "N_PESQ_2012": milhar(rk["n_pesquisas"]),
    "PERSIST_EM_MIN": br(min(x["spearman"] for x in rk["persist_rel_em"]), 2),
    "PERSIST_EM_MAX": br(max(x["spearman"] for x in rk["persist_rel_em"]), 2),
    "PERSIST_M3_MAX": br(max(x["spearman"] for x in rk["persist_rel_m3"]), 2),
    "PERSIST_M3_2022": br(next(x["spearman"] for x in rk["persist_rel_m3"] if x["corte"] == 2022), 2),
    "N_PESQ_PT": milhar(vd["pt"]["geral"]["n_pesquisas"]),
    "P_VERITA": f"{round(100 * ciclo['Veritá']['p_sinal_ciclos'])}%", "P_PARANA": f"{round(100 * ciclo['Paraná Pesquisas']['p_sinal_ciclos'])}%",
    "LIG_1T": br(lig["hist_x_1T"]["spearman"], 2), "LIG_2T": br(lig["hist_x_2T"]["spearman"], 2),
    "P_REPETE": round(100 * repete["P_t"]), "TRANSF_QUAEST": br(tr["Quaest 21/10"]["fatia_flavio"]),
    "TRANSF_PODERDATA": br(tr["PoderData/Aya"]["fatia_flavio"]),
    "P_CENTRAL_DEC": br(pc, 2), "BRIER_V": br((1 - pc) ** 2, 3), "BRIER_P": br(pc ** 2, 3),
    "IC80_LO": br(mu - T6_90 * s), "IC80_HI": br(mu + T6_90 * s), "IC95_LO": br(mu - T6_975 * s), "IC95_HI": br(mu + T6_975 * s),
    "ERRO_1T_2P": br(abs(pr["erro_agregado_1T_2026_flavio_bipartidario"])), "REPO": REPO,
    "TABELA_2T": tab2, "TABELA_1T": tab1, "TABELA_CENARIOS": "\n".join(lin),
}
src = (RAIZ / "site/index.pt-br.src.mdx").read_text(encoding="utf-8")
for k, v in V.items():
    src = src.replace("{{" + k + "}}", str(v))
falta = re.findall(r"\{\{[A-Z0-9_]+\}\}", src)
assert not falta, f"marcadores sem valor: {falta}"
out = RAIZ / "site/material/index.pt-br.mdx"
out.write_text(src, encoding="utf-8")
json.dump({k: v for k, v in V.items() if not k.startswith("TABELA")}, open(RAIZ / "site/material/valores.json", "w"),
          ensure_ascii=False, indent=1)
print(out, len(src.split()), "palavras")
