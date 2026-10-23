"""Entry-point único: recalcula tudo, roda os testes dos números publicados e confere o selo.

Uso:
    python3 -I run_all.py            # resultados -> testes -> verificação do selo de proveniência
    python3 -I run_all.py --selar    # idem, mas regrava o selo (só depois de mudar dado ou código)

Sem dependências fora da biblioteca padrão. A capa (codigo/capa.py) precisa de Pillow e é opcional.
"""
import importlib
import runpy
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
# ordem de dependência: cada etapa lê o que as anteriores gravaram em resultados/
ETAPAS = ["confere_tse", "ranking", "calibra_sigma", "acuracia_1t_2026", "modelo_2t", "vies", "probabilidade",
          "ranking_presidencial", "transferencia", "tabelas", "site_charts", "site_mdx"]


def rodar_etapas():
    """Executa cada script de codigo/ como processo isolado, na ordem de dependência."""
    for e in ETAPAS:
        r = subprocess.run([sys.executable, "-I", str(RAIZ / "codigo" / f"{e}.py")], capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"[falhou] {e}\n{r.stderr[-2000:]}")
        print(f"[ok] {e}")
    if importlib.util.find_spec("PIL"):
        subprocess.run([sys.executable, "-I", str(RAIZ / "codigo" / "capa.py")], check=True, capture_output=True)
        print("[ok] capa")
    else:
        print("[pulado] capa (Pillow não instalado; opcional)")


def rodar_testes():
    """Roda tests/test_*.py sem depender de pytest (o CI também roda com pytest)."""
    falhas = 0
    for arq in sorted((RAIZ / "tests").glob("test_*.py")):
        mod = runpy.run_path(str(arq))
        for nome, fn in mod.items():
            if nome.startswith("test_") and callable(fn):
                try:
                    fn()
                    print(f"[ok] {arq.name}::{nome}")
                except AssertionError as erro:
                    falhas += 1
                    print(f"[FALHOU] {arq.name}::{nome}: {erro}")
    if falhas:
        sys.exit(f"{falhas} teste(s) falharam")


if __name__ == "__main__":
    rodar_etapas()
    rodar_testes()
    modo = "--build" if "--selar" in sys.argv else "--verify"
    sys.exit(subprocess.run([sys.executable, "-I", str(RAIZ / "make_provenance.py"), modo]).returncode)
