"""Selo de proveniência: um chain_hash SHA-256 sobre código, testes, dados declarados e resultados.

Uso:
    python3 -I make_provenance.py --build    # grava output/provenance.json e output/hash-chain.md
    python3 -I make_provenance.py --verify   # recalcula e compara com o selo gravado (exit 1 se divergir)

Fica FORA do selo (informativo): a capa PNG, que depende da versão do Pillow e da plataforma.
Resultados numéricos (resultados/*.json e *.csv) entram no selo com números arredondados a 6 casas:
a libm de cada sistema (log, exp, erf) difere na última casa binária, e o selo tem de valer em
macOS e Linux. Código e dados de entrada entram byte a byte.
"""
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
OUT = RAIZ / "output"
SELADOS = ["codigo/*.py", "tests/*.py", "run_all.py", "dados/*.csv", "dados/externo/tse/*.zip",
           "dados/externo/pindograma_ranking_de_institutos/data/**/*.csv",
           "dados/externo/pindograma_site_ranking/ranking_2024-09-24.csv",
           "resultados/*.json", "resultados/*.csv", "artigo/artigo-v1.md", "site/material/index.pt-br.mdx",
           "site/material/pesquisas-2026.data.ts"]


def arquivos():
    """Lista ordenada dos arquivos selados (caminho relativo à raiz)."""
    vistos = set()
    for padrao in SELADOS:
        vistos.update(p for p in RAIZ.glob(padrao) if p.is_file())
    return sorted(vistos, key=lambda p: p.relative_to(RAIZ).as_posix())


CASAS = 6


def _arredonda(x):
    """Arredonda floats (recursivo) para a forma canônica do selo."""
    if isinstance(x, float):
        return round(x, CASAS) + 0.0
    if isinstance(x, list):
        return [_arredonda(v) for v in x]
    if isinstance(x, dict):
        return {k: _arredonda(v) for k, v in x.items()}
    return x


def _celula(c):
    """Célula de CSV numérica com ponto decimal vira número arredondado; o resto fica como está."""
    if "." in c:
        try:
            return repr(round(float(c), CASAS) + 0.0)
        except ValueError:
            return c
    return c


def canonico(p):
    """Bytes que entram no selo: resultados numéricos arredondados; demais arquivos, o conteúdo bruto."""
    rel = p.relative_to(RAIZ).as_posix()
    if rel.startswith("resultados/") and p.suffix == ".json":
        dado = _arredonda(json.load(open(p, encoding="utf-8")))
        return json.dumps(dado, ensure_ascii=False, sort_keys=True).encode()
    if rel.startswith("resultados/") and p.suffix == ".csv":
        linhas = csv.reader(io.StringIO(p.read_text(encoding="utf-8")))
        return "\n".join(",".join(_celula(c) for c in ln) for ln in linhas).encode()
    return None


def sha(p):
    """SHA-256 do conteúdo canônico de um arquivo."""
    forma = canonico(p)
    if forma is not None:
        return hashlib.sha256(forma).hexdigest()
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def selo():
    """Calcula o hash de cada arquivo e o chain_hash encadeado (ordem lexicográfica dos caminhos)."""
    itens, cadeia = [], hashlib.sha256()
    for p in arquivos():
        rel, d = p.relative_to(RAIZ).as_posix(), sha(p)
        itens.append({"arquivo": rel, "sha256": d})
        cadeia.update(f"{rel}\0{d}\n".encode())
    return {"chain_hash": cadeia.hexdigest(), "n_arquivos": len(itens), "arquivos": itens}


if __name__ == "__main__":
    atual = selo()
    if "--build" in sys.argv:
        OUT.mkdir(exist_ok=True)
        json.dump(atual, open(OUT / "provenance.json", "w"), ensure_ascii=False, indent=1)
        linhas = ["# Hash chain", "", f"chain_hash: `{atual['chain_hash']}` ({atual['n_arquivos']} arquivos)", "",
                  "| Arquivo | SHA-256 |", "| --- | --- |"] + [f"| `{i['arquivo']}` | `{i['sha256']}` |" for i in atual["arquivos"]]
        (OUT / "hash-chain.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
        print(f"selo gravado: {atual['chain_hash']}")
    else:
        gravado = json.load(open(OUT / "provenance.json"))
        if gravado["chain_hash"] != atual["chain_hash"]:
            antes = {i["arquivo"]: i["sha256"] for i in gravado["arquivos"]}
            agora = {i["arquivo"]: i["sha256"] for i in atual["arquivos"]}
            dif = sorted(k for k in antes.keys() | agora.keys() if antes.get(k) != agora.get(k))
            sys.exit("selo DIVERGE em: " + ", ".join(dif))
        print(f"provenance verified: {atual['chain_hash']}")
