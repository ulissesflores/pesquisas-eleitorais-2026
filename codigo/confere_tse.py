"""Confere cada rodada de dados/rodadas_2t.csv contra o dado aberto de registro do TSE.

Fonte: https://cdn.tse.jus.br/estatistica/sead/odsele/pesquisa_eleitoral/pesquisa_eleitoral_2026.zip
(e pesquisa_contratante_2026.zip), extraídos em dados/externo/tse/.
Checa: registro existe, cargo Presidente, empresa, datas de campo, n, e se a data de
divulgação permitida (DT_DIVULGACAO) já passou na data de corte.

Uso: python3 -I codigo/confere_tse.py [AAAA-MM-DD de corte, padrão 2026-10-23]
"""
import csv
import io
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TSE = RAIZ / "dados/externo/tse"
CORTE = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date(2026, 10, 23)


def ler_tse(arquivo_zip, membro):
    """Lê um CSV do TSE (latin-1, separador ;) direto do zip oficial, sem extrair."""
    with zipfile.ZipFile(TSE / arquivo_zip) as z, z.open(membro) as fh:
        return list(csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1"), delimiter=";"))


reg = {r["NR_PROTOCOLO_REGISTRO"]: r for r in ler_tse("pesquisa_eleitoral_2026.zip", "pesquisa_eleitoral_2026_BRASIL.csv")}
contr = {}
for r in ler_tse("pesquisa_contratante_2026.zip", "pesquisa_contratante_2026_BRASIL.csv"):
    nome = r.get("NM_CONTRATANTE", "").strip()
    if nome and nome not in contr.setdefault(r["NR_PROTOCOLO_REGISTRO"], []):
        contr[r["NR_PROTOCOLO_REGISTRO"]].append(nome)


def chave(registro):
    """'BR-07926/2026 (...)' -> 'BR079262026' (primeiro registro do texto) ou None."""
    m = re.search(r"BR-?(\d{5})/?(2026)", registro or "")
    return f"BR{m.group(1)}{m.group(2)}" if m else None


def confianca(t):
    """Nível de confiança declarado no plano amostral/metodologia registrados no TSE (ex. '95%')."""
    txt = f"{t.get('DS_PLANO_AMOSTRAL', '')} {t.get('DS_METODOLOGIA_PESQUISA', '')}"
    m = (re.search(r"confian[çc]a[^.%]{0,60}?(\d{2}(?:[.,]\d+)?)\s?%", txt, re.I)
         or re.search(r"(\d{2}(?:[.,]\d+)?)\s?%\s+de\s+confian[çc]a", txt, re.I))
    return f"{m.group(1)}%" if m else None


def margem(t):
    """Margem de erro declarada no plano amostral registrado no TSE (pontos percentuais)."""
    txt = f"{t.get('DS_PLANO_AMOSTRAL', '')} {t.get('DS_METODOLOGIA_PESQUISA', '')}"
    m = re.search(r"margem[^0-9]{0,200}?(\d{1,2}(?:[.,]\d+)?)\s*(?:\([a-z ]+\)\s*)?(?:p\.?\s?p|ponto)", txt, re.I)
    return m.group(1).replace(".", ",") if m else None


def ficha(registro):
    """Dados do art. 10 que o TSE tem para um registro (contratante, campo, n, confiança, liberação)."""
    t = reg.get(chave(registro))
    if not t:
        return None
    return {"registro": f"BR-{chave(registro)[2:7]}/2026", "empresa": t["NM_EMPRESA_FANTASIA"] or t["NM_EMPRESA"],
            "contratantes": contr.get(t["NR_PROTOCOLO_REGISTRO"], []), "inicio": t["DT_INICIO_PESQUISA"][:10],
            "fim": t["DT_FIM_PESQUISA"][:10], "n": int(t["QT_ENTREVISTADO"]), "confianca": confianca(t),
            "margem": margem(t),
            "dt_registro": t["DT_REGISTRO"][:10], "dt_divulgacao": t["DT_DIVULGACAO"][:10]}



def main():
    saida = []
    for r in csv.DictReader(open(RAIZ / "dados/rodadas_2t.csv", encoding="utf-8")):
        k = chave(r["registro_tse"])
        t = reg.get(k)
        linha = {"instituto": r["instituto"], "registro": r["registro_tse"], "campo_fim_csv": r["campo_fim"], "n_csv": r["n"]}
        if not t:
            linha["status"] = "REGISTRO NAO ENCONTRADO"
        else:
            div = date.fromisoformat(t["DT_DIVULGACAO"][:10])
            fim = t["DT_FIM_PESQUISA"][:10]
            prob = []
            if t["DS_CARGO"] != "Presidente":
                prob.append(f"cargo={t['DS_CARGO']}")
            if fim != r["campo_fim"]:
                prob.append(f"campo_fim TSE={fim}")
            if r["n"].strip().isdigit() and int(r["n"]) != int(t["QT_ENTREVISTADO"]):
                prob.append(f"n TSE={t['QT_ENTREVISTADO']}")
            linha.update({
                "empresa_tse": t["NM_EMPRESA_FANTASIA"] or t["NM_EMPRESA"], "dt_registro": t["DT_REGISTRO"][:10],
                "campo_tse": f"{t['DT_INICIO_PESQUISA'][:10]} a {fim}", "n_tse": t["QT_ENTREVISTADO"],
                "dt_divulgacao_permitida": div.isoformat(), "liberada_no_corte": div <= CORTE,
                "propria": t["ST_PESQUISA_PROPRIA"], "contratante": " | ".join(contr.get(k, [])),
                "confianca_tse": confianca(t) or "", "margem_tse": margem(t) or "",
                "status": "OK" if not prob else "DIVERGE: " + "; ".join(prob),
            })
        saida.append(linha)
    campos = list(dict.fromkeys(k for l in sorted(saida, key=len, reverse=True) for k in l))
    with open(RAIZ / "dados/rodadas_2t_conferidas_tse.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(saida)
    for l in saida:
        print(f"{l['instituto'][:20]:20s} {l['registro']:15s} {l['status'][:40]:40s} lib={l.get('dt_divulgacao_permitida','-')} "
              f"reg={l.get('dt_registro','-')} conf={l.get('confianca_tse','-')} contr={l.get('contratante','')[:40]}")


if __name__ == "__main__":
    main()
