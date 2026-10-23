"""Tabelas com os dados do art. 10 da Res. TSE 23.600 (instituto, contratante, campo, entrevistas,
margem, confiança, registro), usadas no artigo do site e na versão técnica.

Contratante, campo, entrevistas, confiança e registro vêm do dado aberto do TSE (confere_tse.ficha);
a margem é a divulgada pelo instituto quando conferida (dados/rodadas_2t_confianca.csv), senão a do
plano amostral registrado.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import confere_tse as T  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"


def j(n):
    """Lê um JSON de resultados/."""
    return json.load(open(RES / n, encoding="utf-8"))


def br(x, nd=1, sinal=False):
    if round(x, nd) == 0:
        x = 0.0
    s = f"{x:+.{nd}f}" if sinal and x != 0 else f"{x:.{nd}f}"
    return s.replace(".", ",").replace("-", "−")


def milhar(n):
    return f"{int(n):,}".replace(",", ".")


def data_br(iso):
    return f"{iso[8:10]}/{iso[5:7]}"


def contratante(lista):
    return "; ".join(c.title().replace(" S.A.", " S.A.").replace(" Ltda", " Ltda") for c in lista) or "-"


EXIBE = {"AtlasIntel/Bloomberg": "AtlasIntel", "Ipespe/Abrapel": "Ipespe", "PoderData/Aya": "PoderData",
         "BTG/Nexus": "Nexus", "CNT/MDA": "MDA", "Meio/Ideia": "Ideia", "Indexa/Broadcast": "Indexa",
         "Futura/100% Cidades": "Futura"}

m2, a1 = j("modelo_2t.json"), j("acuracia_1t_2026.json")
marg_pub = {r["registro_tse"]: r["margem"] for r in csv.DictReader(open(RAIZ / "dados/rodadas_2t_confianca.csv", encoding="utf-8"))}

# tabela do 2º turno (art. 10 da Res. TSE 23.600)
lin = ["| Instituto | Contratante (registro TSE) | Campo | Entrevistas | Margem | Confiança | Registro | Flávio | Lula |",
       "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in m2["ultima_rodada"]:
    f = T.ficha(r["reg"])
    marg = (marg_pub.get(r["reg"]) or f["margem"] or "").replace(".", ",")
    lin.append(f"| {EXIBE.get(r['inst'], r['inst'])} | {contratante(f['contratantes'])} | {data_br(f['inicio'])} a {data_br(f['fim'])} | "
               f"{milhar(f['n'])} | ±{marg} pp | {f['confianca']} | {f['registro']} | {br(r['v'])}% | {br(100 - r['v'])}% |")
tab2 = ("**Rodada mais recente de cada instituto até 23/10** (votos válidos; quando o instituto divulgou só votos totais, "
        "o válido é calculado dividindo cada candidato pela soma dos dois). Contratante, campo, entrevistas, confiança e "
        "registro: dado aberto do TSE.\n\n" + "\n".join(lin) + "\n\nNomes de parceiros de divulgação (Bloomberg, Aya, BTG, "
        "CNT, Meio, Broadcast, Abrapel, 100% Cidades) aparecem só quando são contratantes no registro do TSE.")

# tabela do 1º turno
lin = ["| Instituto | Contratante (registro TSE) | Campo | Entrevistas | Margem | Confiança | Registro | Flávio | Lula | Erro na margem |",
       "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for l in a1["ultima_por_instituto"]:
    ini, fim = l["campo"].split(" a ")
    lin.append(f"| {l['instituto']} | {contratante(l['contratantes'])} | {data_br(ini)} a {data_br(fim)} | {milhar(l['n'])} | "
               f"±{l['margem']} pp | {l['confianca']} | {l['registro']} | {br(l['flavio'])}% | {br(l['lula'])}% | {br(l['m5'],1,True)} |")
tab1 = ("**Pesquisa final de cada instituto no 1º turno** (votos válidos; resultado do TSE: Flávio 47,03%, Lula 45,16%). "
        "\"Erro na margem\" é a diferença entre a vantagem de Flávio na pesquisa e nas urnas (+1,87): negativo subestimou "
        "Flávio. Ordem: do menor ao maior erro.\n\n" + "\n".join(lin) +
        "\n\nNotas de origem: Gerp e Nexus pelos válidos que os próprios institutos publicaram; Instituto França recalculado dos "
        "totais (o instituto não publica válidos); Palver não divulga válidos, e os percentuais são os publicados; os decimais "
        "da Veritá vêm da compilação do Times Brasil/CNBC, e o instituto divulgou 47 e 45 inteiros.")

