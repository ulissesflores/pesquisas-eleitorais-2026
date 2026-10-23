<div align="center">

# Pesquisas eleitorais 2026: quem acerta, quem erra e para que lado

**Flávio Bolsonaro é favorito no 2º turno de 25/10/2026, não vencedor: 77% de chance, com 51,0% dos válidos na mediana de 38 rodadas registradas no TSE.**

![license-code](https://img.shields.io/badge/code-GPL--3.0--or--later-blue)
![license-text](https://img.shields.io/badge/text-CC--BY--4.0-lightgrey)
![python](https://img.shields.io/badge/python-3.11%2B-blue)
![tests](https://img.shields.io/badge/tests-10_passing-brightgreen)
![reproducible](https://img.shields.io/badge/reproducible-SHA--256_chain-success)

</div>

> [!IMPORTANT]
> **Achados.** Mediana de 51,0% para Flávio em 38 rodadas de 17 institutos (só a Vox Brasil põe Lula à frente).
> Probabilidade de vitória de 77% (faixa 55%-79%), com erro calibrado nos segundos turnos presidenciais de 2002 a 2022
> (1,25 pp). No 1º turno, as pesquisas subestimaram o candidato de direita em todas as seis eleições de 2002 a 2022 e
> nas 12 pesquisas finais de 2026; no 2º turno, o erro histórico não tem direção (−0,30 ± 0,54 pp).

Artigo: https://ulissesflores.com/artigos/pesquisas-eleitorais-2026 · versão técnica: [`artigo/artigo-v1.md`](artigo/artigo-v1.md)

## O que este repositório acrescenta

1. **Base longa e aberta, com linhagens:** pesquisas finais presidenciais 1989-2026 e 4.974 pesquisas finais de
   presidente, governador e prefeito 2012-2022 (base do Pindograma refeita em código próprio). Ibope e Ipec,
   DataPoder360 e PoderData, Atlas Político e AtlasIntel entram como linhagens.
2. **Teste de persistência:** se a ordem de acurácia e a direção do erro de cada instituto se repetem entre períodos.
3. **Conformidade verificável:** cada rodada de 2026 conferida no dado aberto de registro do TSE (contratante, campo,
   entrevistas, margem, confiança, registro), e previsões registradas antes do resultado em
   [`PREREGISTRATION.md`](PREREGISTRATION.md).

## Em resumo

| Pergunta | Resposta |
| --- | --- |
| Centro do 2º turno 2026 | 51,0% Flávio x 49,0% Lula (mediana da última rodada de 17 institutos) |
| Probabilidade de Flávio | 77% (t de Student, 6 gl); 69% só com institutos de 20+ pesquisas; 55% se a queda do início de outubro continuar |
| O 1º turno de 2026 subestimou Flávio? | Sim, nas 12 pesquisas finais; Lula sem erro com direção (5 sub, 4 sobre, 3 acerto) |
| O 2º turno repete o erro do 1º? | Não na história: correlação −0,61 entre os dois erros (n = 6) |
| Acurácia passada prevê a futura? | Pouco: Spearman 0,06-0,38 no erro da margem |
| Algum instituto erra sempre para o mesmo lado? | Padrões sugestivos (Veritá 0/5 e Paraná 0/4 ciclos a favor do PT), nenhum conclusivo |

## Quick start

```bash
python3 -I run_all.py
```

Saída esperada (final):

```text
[ok] test_numeros_publicados.py::test_determinismo
provenance verified: <chain_hash de output/provenance.json>
```

## O que é e o que não é afirmado

- **Afirmado:** os números das tabelas, recalculáveis a partir de `dados/`; a calibração histórica do erro; a ausência
  de padrão conclusivo de erro direcional por instituto.
- **Não afirmado:** intenção, contratação ou fraude de qualquer instituto (erro sistemático tem causas técnicas); que a
  probabilidade seja frequência de longo prazo (é uma conjectura calibrada com seis eleições).
- **Congelado:** percentuais coletados em 23/10/2026 e o arquivo do TSE daquele dia (ver
  [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)).

## Integridade

```bash
python3 -I make_provenance.py --verify
```

## Estrutura

```text
codigo/       scripts (ordem em run_all.py)
dados/        rodadas e séries coletadas, com URL por linha; externo/ = TSE e Pindograma sem alteração
resultados/   saídas JSON/CSV
artigo/       versão técnica (artigo-v1.md, montada de artigo-v1.src.md)
site/         fonte do artigo do site e material gerado (MDX, datasets dos gráficos, capa)
tests/        números publicados como asserções
docs/laudos/  auditoria adversarial independente
output/       selo de proveniência
```

## Autor

Carlos Ulisses Flores · [ORCID 0000-0002-6034-7765](https://orcid.org/0000-0002-6034-7765) ·
[ulissesflores.com](https://ulissesflores.com) · [Lattes](http://lattes.cnpq.br/6905246706890561)

## Citação

```bibtex
@software{flores_pesquisas_eleitorais_2026,
  author  = {Flores, Carlos Ulisses},
  title   = {Pesquisas eleitorais 2026: acurácia, direção do erro e cenários do 2º turno},
  year    = {2026},
  version = {0.1.0},
  url     = {https://github.com/ulissesflores/pesquisas-eleitorais-2026}
}
```

Sem DOI nesta versão; ver [`CITATION.cff`](CITATION.cff).

## Licença

Código GPL-3.0-or-later ([`LICENSE`](LICENSE)); textos, tabelas e figuras CC-BY-4.0; dados de terceiros sob as
licenças de origem. Detalhes em [`NOTICE`](NOTICE).

## Referências-âncora

Mosteller et al. (1949); Martin, Traugott & Kennedy (2005, doi:10.1093/poq/nfi044); Shirani-Mehr et al. (2018,
doi:10.1080/01621459.2018.1448823); Jennings & Wlezien (2018, doi:10.1038/s41562-018-0315-6); Pindograma (2024).
