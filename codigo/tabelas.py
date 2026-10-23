"""Gera as tabelas do artigo (Markdown) a partir de resultados/*.json e dados/*.csv.

Nenhum número das tabelas é digitado à mão: rode depois dos outros scripts.
Uso: python3 -I codigo/tabelas.py   -> artigo/tabelas_geradas.md
"""
import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
OUT = RAIZ / "artigo"
OUT.mkdir(exist_ok=True)


def j(nome):
    return json.load(open(RES / nome, encoding="utf-8"))


def br(x, nd=2, sinal=False):
    if x is None:
        return "-"
    s = f"{x:+.{nd}f}" if sinal else f"{x:.{nd}f}"
    return s.replace(".", ",")


def pct(x):
    return f"{round(100 * x)}%"


partes = []

# T1: acurácia do 1º turno de 2026
a1 = j("acuracia_1t_2026.json")["ultima_por_instituto"]
t = ["| Instituto | Fim do campo | Flávio | Lula | Erro Flávio | Erro Lula | Mosteller 3 | Erro na margem (M5) | A (MTK) |",
     "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for l in a1:
    t.append(f"| {l['instituto']} | {l['campo'][-2:]}/{l['campo'][-5:-3]} | {br(l['flavio'],1)} | {br(l['lula'],1)} | "
             f"{br(l['erro_flavio'],2,True)} | {br(l['erro_lula'],2,True)} | {br(l['m3'])} | {br(l['m5'],2,True)} | {br(l['A'],3,True)} |")
partes.append(("T1. Pesquisas finais do 1º turno de 2026 (votos válidos; resultado TSE: Flávio 47,03, Lula 45,16), "
               "ordenadas pelo erro absoluto na margem", t))

# T2: ranking presidencial 1989-2026, um quadro por turno (escalas diferentes: 1º turno é fatia de todos os
# válidos com muitos candidatos; 2º turno é disputa de dois)
rp = j("ranking_presidencial_1989_2026.json")
for chave, letra, titulo in (("1turno", "a", "1º turno"), ("2turno", "b", "2º turno")):
    t = ["| Posição | Linhagem (nomes usados) | Pesquisas finais | Erro absoluto médio | Encolhido | Relativo aos rivais do mesmo ano | Viés médio (+ = pró-direita) | Erraram pró-direita / pró-esquerda | p do sinal |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, d in enumerate(rp[chave]["tabela"], 1):
        t.append(f"| {i} | {d['linhagem']} ({', '.join(d['nomes'])}) | {d['n']} | {br(d['erro_abs_medio'])} | "
                 f"{br(d['erro_abs_encolhido'])} | {br(d['rel_medio'],2,True)} | {br(d['vies_medio_pro_direita'],2,True)} | "
                 f"{d['n_pro_direita']} / {d['n_pro_esquerda']} | {br(d['p_sinal'])} |")
    partes.append((f"T2{letra}. Classificação presidencial 1989-2026 por linhagem, {titulo} (erro na fatia de válidos do "
                   f"candidato de direita/PSDB; média geral {br(rp[chave]['media_geral_abs'])} pp; ordem pelo erro encolhido)", t))

# T3: ranking 2012-2022 (todas as disputas), institutos com >= 20 pesquisas
rk = j("ranking_2012_2022.json")
lst = [d for d in rk["ranking_rel_em"] if d["n_pesquisas"] >= 20]
t = ["| Posição | Instituto | Pesquisas | Disputas | Anos | Erro na margem relativo aos rivais (encolhido) | Erro absoluto na margem | Mosteller 3 |",
     "| --- | --- | --- | --- | --- | --- | --- | --- |"]
for i, d in enumerate(lst, 1):
    t.append(f"| {i} | {d['instituto']} | {d['n_pesquisas']} | {d['n_disputas']} | {d['anos']} | {br(d['encolhido'],2,True)} | "
             f"{br(d['em_abs_bruto'])} | {br(d['m3_bruto'])} |")
partes.append(("T3. Classificação 2012-2022, todas as disputas (presidente, governador, prefeito), institutos com 20 ou mais "
               "pesquisas finais. Negativo = errou menos que os rivais na mesma disputa", t))

# T4: persistência
t = ["| Ano de corte | Institutos | Spearman, erro médio por candidato (M3) | Spearman, erro na margem (M5) |",
     "| --- | --- | --- | --- |"]
for a, b in zip(rk["persist_rel_m3"], rk["persist_rel_em"], strict=True):
    t.append(f"| {a['corte']} | {a['n_institutos']} | {br(a['spearman'])} | {br(b['spearman'])} |")
partes.append(("T4. Acerto antes do corte prevê acerto depois? Correlação de postos entre períodos (institutos com 5 ou mais "
               "pesquisas em cada lado)", t))

# T5: viés com direção (PT), por ciclo
vd = j("vies_direcao_2012_2022.json")["pt"]
ciclo = j("vies_casa_por_ciclo.json")
t = ["| Instituto | Pesquisas | Anos | Viés bruto pró-PT | Efeito de casa pró-PT (vs. rivais) | Encolhido | Pesquisas do mesmo lado | Ciclos pró-PT / ciclos |",
     "| --- | --- | --- | --- | --- | --- | --- | --- |"]
for d in vd["institutos"]:
    if d["instituto"] in ciclo:
        c = ciclo[d["instituto"]]
        t.append(f"| {d['instituto']} | {d['n']} | {d['anos']} | {br(d['vies_bruto'],2,True)} | {br(d['casa'],2,True)} | "
                 f"{br(d['casa_encolhida'],2,True)} | {pct(d['pct_casa_mesmo_lado']) if d['pct_casa_mesmo_lado'] is not None else '-'} | "
                 f"{c['anos_pro_PT']} / {c['anos_total']} |")
g = vd["geral"]
partes.append((f"T5. Viés com direção, 2012-2022: erro com sinal na fatia bipartidária do candidato do PT ({g['n_pesquisas']} pesquisas; "
               f"indústria: {br(g['por_turno']['1'],2,True)} pp no 1º turno, {br(g['por_turno']['2'],2,True)} pp no 2º)", t))

# T6: 2º turno 2026, última rodada com conformidade
m2 = j("modelo_2t.json")
conf = {r["registro"]: r for r in csv.DictReader(open(RAIZ / "dados/rodadas_2t_conferidas_tse.csv", encoding="utf-8"))}
cf = {}
p_conf = RAIZ / "dados/rodadas_2t_confianca.csv"
if p_conf.exists():
    for r in csv.DictReader(open(p_conf, encoding="utf-8")):
        if r["registro_tse"] not in cf or "não" in cf[r["registro_tse"]].get("confianca", "não"):
            cf[r["registro_tse"]] = r
rod = {r["registro_tse"]: r for r in csv.DictReader(open(RAIZ / "dados/rodadas_2t.csv", encoding="utf-8"))}
t = ["| Instituto | Contratante (TSE) | Campo | Entrevistas (TSE) | Margem | Confiança | Registro | Flávio (válidos) | Efeito de casa |",
     "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in m2["ultima_rodada"]:
    c, x, k = conf.get(r["reg"], {}), rod.get(r["reg"], {}), cf.get(r["reg"], {})
    casa = m2["efeito_casa"].get(r["inst"])
    campo = c.get("campo_tse", "-")
    if " a " in campo:
        ini, fim = campo.split(" a ")
        campo = f"{ini[8:10]}/{ini[5:7]} a {fim[8:10]}/{fim[5:7]}"
    marg = (k.get("margem") or x.get("margem", "-")).replace(".", ",")
    n_tse = f"{int(c['n_tse']):,}".replace(",", ".") if c.get("n_tse", "").isdigit() else "-"
    t.append(f"| {r['inst']} | {c.get('contratante','-').split(' | ')[0].title()} | {campo} | {n_tse} | "
             f"±{marg} pp | {k.get('confianca','não conferido')} | {r['reg']} | {br(r['v'])} | {br(casa,2,True)} |")
partes.append((f"T6. 2º turno de 2026: rodada mais recente de cada instituto até 23/10 (registro conferido no dado aberto do TSE "
               f"gerado em 23/10/2026 05:46). Mediana {br(m2['mediana'])}, média {br(m2['media'])}. Fora do agregado: "
               + "; ".join(f"{k}, {v}" for k, v in m2.get("excluidas", {}).items()), t))

# T7: probabilidade
pr = j("probabilidade.json")
t = ["| Centro (fatia de Flávio) | Valor | Ajuste de viés | P normal | P t (6 gl) |", "| --- | --- | --- | --- | --- |"]
for c in pr["cenarios"]:
    t.append(f"| {c['centro']} | {br(c['mu'])} | {c['rotulo_vies']} ({br(c['ajuste_vies'],2,True)}) | {pct(c['P_normal'])} | {pct(c['P_t'])} |")
partes.append((f"T7. Probabilidade de vitória de Flávio. Erro sistemático calibrado nos 2º turnos presidenciais 2002-2022 "
               f"(RMS {br(pr['sigma_rms_2T'])} pp; sigma total {br(pr['sigma_total'])} pp)", t))

# tabelas curtas embutidas no corpo do texto
hist_rows = []
for ano in sorted(set(pr["erro_agregado_1T_por_ano"]) | set(pr["erro_agregado_2T_por_ano"]), key=int):
    a, b = pr["erro_agregado_1T_por_ano"].get(ano), pr["erro_agregado_2T_por_ano"].get(ano)
    hist_rows.append(f"| {ano} | {br(a['erro'],2,True) if a else '-'} | {a['k'] if a else '-'} | "
                     f"{br(b['erro'],2,True) if b else '-'} | {b['k'] if b else '-'} |")
sig_rows = [f"| {br(float(k),1)} | {pct(v)} |" for k, v in pr["sensibilidade_sigma_no_centro"].items()]
embutidas = {"HIST": hist_rows, "SIGMA": sig_rows}

txt = "# Tabelas geradas por codigo/tabelas.py\n\nNão editar à mão: rode `python3 -I codigo/tabelas.py`.\n"
for titulo, linhas in partes:
    txt += f"\n## {titulo}\n\n" + "\n".join(linhas) + "\n"
(OUT / "tabelas_geradas.md").write_text(txt, encoding="utf-8")

# monta o artigo: troca <!-- TABELA X --> pela tabela gerada
src = (OUT / "artigo-v1.src.md").read_text(encoding="utf-8")
# Tabelas 1 e 6 com os dados do art. 10 da Res. TSE 23.600 (mesmas do artigo do site)
import sys  # noqa: E402
sys.path.insert(0, str(RAIZ / "codigo"))
from tabelas_art10 import tab1, tab2  # noqa: E402
src = src.replace("<!-- TABELA T1 -->", "**Tabela 1.** " + tab1).replace("<!-- TABELA T6 -->", "**Tabela 6.** " + tab2)
src = src.replace("{{CASA_VERITA}}", br(-m2["efeito_casa"]["Veritá"] * -1, 2, True))
for titulo, linhas in partes:
    cod = titulo.split(".")[0]
    src = src.replace(f"<!-- TABELA {cod} -->", f"**Tabela {cod[1:]}.** {titulo.split('. ', 1)[1]}.\n\n" + "\n".join(linhas))
for cod, linhas in embutidas.items():
    src = src.replace(f"<!-- TABELA {cod} -->", "\n".join(linhas))
assert "<!-- TABELA" not in src, "marcador sem tabela"
(OUT / "artigo-v1.md").write_text(src, encoding="utf-8")
print(txt[:3000])
