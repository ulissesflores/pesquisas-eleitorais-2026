"""Selo de proveniência: um chain_hash SHA-256 sobre código, testes, dados declarados e resultados.

Uso:
    python3 -I make_provenance.py --build    # grava output/provenance.json e output/hash-chain.md
    python3 -I make_provenance.py --verify   # recalcula e compara com o selo gravado (exit 1 se divergir)

Fica FORA do selo (informativo): a capa PNG, que depende da versão do Pillow e da plataforma.
"""
import hashlib
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


def sha(p):
    """SHA-256 do conteúdo de um arquivo."""
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
