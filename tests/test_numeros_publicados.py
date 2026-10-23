"""Todo número citado no artigo do site e na versão técnica é uma asserção aqui.

Se um dado ou um script mudar e o número publicado deixar de bater, o teste quebra antes do texto.
Roda com `python3 -I run_all.py` (sem pytest) ou com `pytest`.
"""
import csv
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
sys.path.insert(0, str(RAIZ / "codigo"))


def j(nome):
    """Lê um JSON de resultados/."""
    return json.load(open(RES / nome, encoding="utf-8"))


def perto(a, b, tol):
    """Compara dois números com tolerância absoluta e mensagem legível."""
    assert abs(a - b) <= tol, f"{a} != {b} (tol {tol})"


def test_segundo_turno_2026():
    """Agregado: 38 rodadas de 17 institutos, mediana 51,0, só a Vox Brasil com Lula à frente."""
    m = j("modelo_2t.json")
    assert (m["n_rodadas"], m["n_institutos"]) == (38, 17)
    perto(m["mediana"], 51.00, 0.005)
    perto(m["dp_entre_institutos"], 0.76, 0.005)
    assert m["institutos_com_lula_a_frente"] == ["Vox Brasil"]
    assert "Alfa Inteligencia" in m["excluidas"]


def test_probabilidade():
    """Cenário central 77% (t, 6 gl); faixa 55%-79%; erro histórico do 2º turno 1,25 pp."""
    p = j("probabilidade.json")
    perto(p["sigma_rms_2T"], 1.25, 0.005)
    perto(p["sigma_rms_2T_14dias"], 1.41, 0.005)
    perto(p["vies_medio_2T_direita"], -0.30, 0.005)
    perto(p["ep_vies"], 0.54, 0.005)
    perto(p["corr_erro_1T_x_2T_mesmo_ano"], -0.61, 0.005)
    assert p["n_eleicoes"] == 6
    central = next(c for c in p["cenarios"] if c["centro"].startswith("CENTRAL:") and c["rotulo_vies"] == "sem viés")
    perto(central["P_t"], 0.77, 0.005)
    perto(central["P_normal"], 0.79, 0.005)
    sem_vies = [c["P_t"] for c in p["cenarios"] if c["rotulo_vies"] == "sem viés"]
    perto(min(sem_vies), 0.55, 0.005)
    perto(max(sem_vies), 0.79, 0.005)


def test_primeiro_turno_2026():
    """12 pesquisas finais abaixo de Flávio; Lula 5 sub, 4 sobre, 3 acerto; erro bipartidário -1,9."""
    a = j("acuracia_1t_2026.json")
    assert (a["n_finais"], a["flavio_abaixo"], a["flavio_abaixo_mais_de_meio_ponto"]) == (12, 12, 10)
    assert a["lula_sub_sobre_acerto"] == [5, 4, 3]
    perto(a["erro_bipartidario_medio_finais"], -1.89, 0.005)
    for l in a["ultima_por_instituto"]:
        assert l["confianca"] and l["margem"] and l["registro"].startswith("BR-"), l["instituto"]


def test_historia_1989_2022():
    """1º turno subestima a direita nas 6 eleições de 2002 a 2022."""
    p = j("probabilidade.json")
    um = {int(a): v for a, v in p["erro_agregado_1T_por_ano"].items() if v["k"] >= 2}
    assert sorted(um) == [2002, 2006, 2010, 2014, 2018, 2022]
    assert all(v["erro"] < 0 for v in um.values())
    assert sum(v["erro"] < -5 for v in um.values()) == 3


def test_ranking_e_persistencia():
    """Base 2012-2022: 4.974 pesquisas; replicação do Pindograma; persistência fraca na margem."""
    r = j("ranking_2012_2022.json")
    assert (r["n_pesquisas"], r["n_disputas"]) == (4974, 2220)
    perto(r["validacao_pindograma"]["corr_erro_medio"], 0.90, 0.005)
    perto(r["validacao_pindograma"]["cobertura_pesquisas"], 0.72, 0.005)
    em = [x["spearman"] for x in r["persist_rel_em"]]
    m3 = [x["spearman"] for x in r["persist_rel_m3"]]
    perto(min(em), 0.06, 0.005)
    perto(max(em), 0.38, 0.005)
    perto(max(m3), 0.70, 0.005)
    perto(m3[-1], 0.20, 0.005)


def test_vies_com_direcao():
    """Veritá 0/5 e Paraná 0/4 ciclos a favor do PT; AtlasIntel com sinais opostos; nada conclusivo."""
    c = j("vies_casa_por_ciclo.json")
    assert (c["Veritá"]["anos_pro_PT"], c["Veritá"]["anos_total"]) == (0, 5)
    assert (c["Paraná Pesquisas"]["anos_pro_PT"], c["Paraná Pesquisas"]["anos_total"]) == (0, 4)
    assert (c["AtlasIntel"]["anos_pro_PT"], c["AtlasIntel"]["anos_total"]) == (1, 2)
    perto(c["Veritá"]["p_sinal_ciclos"], 0.0625, 1e-9)
    lig = j("vies_ligacao_2026.json")
    perto(lig["hist_x_1T"]["spearman"], 0.18, 0.005)
    perto(lig["hist_x_2T"]["spearman"], -0.25, 0.005)


def test_transferencia():
    """Transferência: 51,5% (Quaest) e 52,1% (PoderData/Aya)."""
    t = j("transferencia.json")
    perto(t["Quaest 21/10"]["fatia_flavio"], 51.47, 0.005)
    perto(t["PoderData/Aya"]["fatia_flavio"], 52.10, 0.005)


def test_conformidade_tse():
    """Toda rodada do agregado existe no TSE, estava liberada no corte e tem confiança registrada."""
    conf = {r["registro"]: r for r in csv.DictReader(open(RAIZ / "dados/rodadas_2t_conferidas_tse.csv", encoding="utf-8"))}
    for r in j("modelo_2t.json")["ultima_rodada"]:
        c = conf[r["reg"]]
        assert c["liberada_no_corte"] == "True", r["reg"]
        assert c["dt_registro"] <= "2026-10-17", r["reg"]
        assert c["confianca_tse"], r["reg"]


def test_texto_do_site():
    """Os valores escritos no artigo do site saem do código (site/material/valores.json)."""
    v = json.load(open(RAIZ / "site/material/valores.json", encoding="utf-8"))
    assert (v["MEDIANA"], v["P_CENTRAL"], v["P_MIN"], v["RMS"]) == ("51,0", 77, 55, "1,25")
    assert (v["IC80_LO"], v["IC80_HI"], v["IC95_LO"], v["IC95_HI"]) == ("49,2", "52,8", "47,9", "54,1")
    mdx = (RAIZ / "site/material/index.pt-br.mdx").read_text(encoding="utf-8")
    assert "{{" not in mdx and "mediante solicitação" not in mdx
    assert "title: 'As pesquisas erram contra a direita há 24 anos. No 2º turno, não" in mdx


def test_determinismo():
    """A probabilidade por simulação t é determinística (semente fixa)."""
    import probabilidade as P

    assert P.p_t(51.0, 1.26, 6, sims=20000) == P.p_t(51.0, 1.26, 6, sims=20000)
