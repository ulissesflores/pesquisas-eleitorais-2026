# Reprodutibilidade

## Dois selos

1. **Derivação reproduzível.** Tudo em `resultados/`, `artigo/artigo-v1.md` e `site/material/` é recalculado por
   `python3 -I run_all.py` a partir de `dados/` e `codigo/`, só com a biblioteca padrão do Python 3.11+. O
   `chain_hash` de `output/provenance.json` sela código, testes, dados declarados e resultados; `run_all.py` termina
   com `python3 -I make_provenance.py --verify`, que recalcula o selo e reprova qualquer divergência. Código e dados
   de entrada entram no selo byte a byte; os resultados numéricos entram arredondados a 6 casas decimais, porque a
   biblioteca matemática de cada sistema operacional difere na última casa binária (medido: macOS x Linux do CI).
2. **Evidência congelada, não re-rodável.** A coleta dos percentuais de cada pesquisa (reportagens e relatórios de
   institutos lidos em 23/10/2026) e o arquivo de registro do TSE daquele dia não podem ser refeitos: o TSE regenera
   o arquivo diariamente e reportagens mudam. Por isso a cópia do zip do TSE fica em `dados/externo/tse/` e cada
   linha de `dados/*.csv` traz a URL de onde o número saiu.

## Trilha 1, leve (segundos)

```bash
python3 -I run_all.py
```

Saída esperada nas últimas linhas: `[ok] test_numeros_publicados.py::test_determinismo` e
`provenance verified: <chain_hash>`.

## Trilha 2, conferência de fora

- Registro das pesquisas: baixe `pesquisa_eleitoral_2026.zip` em https://dadosabertos.tse.jus.br (pacote
  `pesquisas-eleitorais-2026`) e rode `codigo/confere_tse.py`; registros e datas de 23/10 devem bater, ainda que o
  arquivo novo tenha mais registros.
- Base 2012-2022: clone https://github.com/pindograma/ranking_de_institutos e compare `data/` com
  `dados/externo/pindograma_ranking_de_institutos/data/`.

## O que não pode ser re-rodado

- Os percentuais das rodadas de 2026 e das pesquisas finais de 1989-2022 (coleta manual, com URL por linha).
- A capa (`site/material/hero.png`) depende da versão do Pillow e fica fora do selo.

## Limites declarados

A replicação da base do Pindograma reproduz o erro médio por instituto do ranking publicado com correlação de 0,90,
mas cobre cerca de 72% das pesquisas dele; a diferença não foi diagnosticada. As demais ameaças à validade estão na
seção 6 de `artigo/artigo-v1.md`.
