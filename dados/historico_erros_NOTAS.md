# Histórico de erros das pesquisas presidenciais brasileiras, 1989-2022 (notas de coleta)

Coleta em 2026-10-23. Arquivos:

- `dados/historico_erros.csv` (92 linhas: uma por eleição x turno x instituto, última pesquisa de cada instituto)
- `dados/historico_pesquisas_candidatos.csv` (321 linhas: todos os candidatos com >=2% na pesquisa ou no resultado, 1º e 2º turno; medida multipartidária)
- `dados/historico_resultados_oficiais.csv` (resultados em votos válidos, com URL)

## 1. Convenções (ler antes de usar os números)

- **Erro com sinal** = estimativa da pesquisa menos resultado oficial, em votos válidos, para o candidato `cand_dir`. Negativo = a pesquisa subestimou o candidato.
- **Erro na margem** = (válidos do candidato - válidos do adversário na pesquisa) - (mesma diferença no resultado). Adversário = o outro finalista do resultado oficial (1º turno: o outro dos dois mais votados).
- **cand_dir**: 1989 Collor; 1994 e 1998 Fernando Henrique Cardoso (PSDB); 2002 Serra (PSDB); 2006 Alckmin (PSDB); 2010 Serra; 2014 Aécio (PSDB, 1º e 2º turno); 2018 e 2022 Bolsonaro. Em 1994/1998/2002 o PSDB era governo ou candidato do governo: o rótulo é da regra do pedido (candidato do PSDB), não de ideologia. Todos os candidatos >=2% estão no arquivo longo.
- **tipo_origem**: `valido` = o instituto/imprensa divulgou o número em válidos (lido do título da matéria, do slug da URL ou de tabela do instituto); `total_convertido` = calculado por mim. No 2º turno, válidos = A/(A+B). No 1º turno, válidos = A / soma de todos os candidatos listados na pesquisa (+ coluna "outros"), isto é, branco, nulo e indeciso saem do denominador. Coluna `conversao`: `completa` quando a tabela lista todos os candidatos; `parcial` nas pesquisas de 1989-2006 em que só os candidatos >=2% foram coletados (denominador subestimado, valor convertido tende a ficar um pouco alto). As linhas `parcial` (todas de 1º turno antes de 2010) ficam FORA da tabela-resumo, do POOL e do ranking por linhagem; aparecem só nas colunas "todos". No 2º turno com dois candidatos a conversão A/(A+B) é exata (`completa`).
- Pesquisas divulgadas em inteiros (Datafolha, Ibope, Ipec, Quaest) carregam ruído de arredondamento de até cerca de 0,5 a 1,0 pp na conversão. `valido_dir_convertido` está em todas as linhas para comparar com o `valido` divulgado.
- `base_margem` diz qual base entrou no erro de margem (válido divulgado dos dois candidatos, ou conversão dos dois).
- **núcleo** (`nucleo`=1): Datafolha, Ibope/Ipec, Quaest, AtlasIntel, PoderData/DataPoder360, Paraná Pesquisas, CNT/MDA, CNT/Sensus, Vox Populi, Ipespe, Ideia, FSB, Real Time Big Data. É uma classificação minha, definida por institutos com divulgação nacional recorrente; ficam fora do núcleo Veritá, Brasmarket, Equilíbrio Brasil, IFP, Gerp, Futura, Amostra, Brasilis (ainda estão no CSV). Nenhuma linha foi apagada.
- `contratante_registro`: contratante no registro TSE (base Pindograma, 2014 e 2018), para filtrar pesquisas partidárias (ex.: Vox Populi 2018 2º turno de 27/10 foi contratada pela Editora 247 e a de 23/10 pela CUT).
- `dias_antes_eleicao`: dias entre o fim do campo e o dia da eleição. As estatísticas "núcleo <=7d" excluem pesquisas mais antigas (p.ex. DataPoder360 em 18/10/2018, Paraná Pesquisas em 8/10/2014). Linhas com data "nao achado" entram no filtro (Ibope 2006 divulgado em 30/09; Quaest 2022 foi resolvida pelo registro TSE).
- `n`: quando há registro TSE (base aberta do Pindograma), a coluna `n` traz o n do registro e `n_imprensa` traz o outro número quando difere (Datafolha 2014 1º turno: 17.800 no registro, 18.116 na imprensa; Datafolha 2018 1º turno: 17.056 contra 19.552). Não verifiquei qual dos dois é amostra planejada e qual é executada: para ponderar por n, decidir e conferir no PDF de registro. `n_fonte` diz a origem. Campo `nao achado` = 19 linhas.

## 2. Tabela-resumo por ano e turno

Erro de sinal no `cand_dir`, em pontos percentuais de votos válidos. "Erro médio do agregado" = média simples dos institutos do núcleo com campo até 7 dias antes (é o erro de uma média das pesquisas finais sem ponderar por amostra). Nos anos 1989-1998 há 1 a 2 institutos: a linha é ilustrativa, não estatística.

| Ano | Turno | Candidato (dir/oposição) | Resultado válidos (TSE) | k núcleo ≤7d | Erro médio do agregado (pp) | DP entre institutos (pp) | Erro abs. médio (pp) | Erro médio na margem (pp) | k todos (qualquer data) | Erro médio todos (pp) | DP todos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1989 | 1 | Collor | 30.48% | 0 | — | — | — | — | 1 | -0.59 | — |
| 1989 | 2 | Collor | 53.03% | 1 | -1.38 | — | 1.38 | -2.76 | 1 | -1.38 | — |
| 1994 | 1 | FHC | 54.28% | 0 | — | — | — | — | 2 | +0.69 | 0.29 |
| 1998 | 1 | FHC | 53.06% | 1 | +1.94 | — | 1.94 | +3.65 | 2 | +3.82 | 2.65 |
| 2002 | 1 | Serra | 23.20% | 2 | -1.70 | 0.71 | 1.70 | -4.26 | 4 | -1.78 | 0.46 |
| 2002 | 2 | Serra | 38.73% | 4 | -2.50 | 1.29 | 2.50 | -5.01 | 4 | -2.50 | 1.29 |
| 2006 | 1 | Alckmin | 41.64% | 3 | -6.04 | 3.33 | 6.04 | -10.10 | 4 | -5.46 | 2.96 |
| 2006 | 2 | Alckmin | 39.17% | 3 | -0.90 | 1.27 | 0.90 | -1.81 | 3 | -0.90 | 1.27 |
| 2010 | 1 | Serra | 32.61% | 4 | -1.82 | 0.86 | 1.82 | -7.98 | 4 | -1.82 | 0.86 |
| 2010 | 2 | Serra | 43.95% | 4 | -0.41 | 0.75 | 0.72 | -0.82 | 4 | -0.41 | 0.75 |
| 2014 | 1 | Aécio | 33.55% | 4 | -6.90 | 0.53 | 6.90 | -11.08 | 5 | -7.18 | 0.76 |
| 2014 | 2 | Aécio | 48.36% | 5 | +0.34 | 2.48 | 1.94 | +0.68 | 7 | +1.39 | 2.74 |
| 2018 | 1 | Bolsonaro | 46.03% | 8 | -6.86 | 3.38 | 6.86 | -3.97 | 13 | -6.41 | 4.80 |
| 2018 | 2 | Bolsonaro | 55.13% | 8 | +0.97 | 3.44 | 2.69 | +1.94 | 10 | +1.55 | 4.03 |
| 2022 | 1 | Bolsonaro | 43.20% | 10 | -5.03 | 1.84 | 5.03 | -5.63 | 14 | -2.84 | 4.42 |
| 2022 | 2 | Bolsonaro | 49.10% | 8 | -1.43 | 1.19 | 1.54 | -2.85 | 14 | -0.12 | 2.12 |

### 2.1 Agregando as pesquisas individuais (núcleo, campo <=7 dias antes)

| Janela | Turno | k (pesquisas) | Erro médio | DP | RMSE | Erro abs. médio |
|---|---|---|---|---|---|---|
| 1989-2022 | 1 | 32 | -4.99 | 3.07 | 5.83 | 5.11 |
| 1989-2022 | 2 | 33 | -0.54 | 2.32 | 2.35 | 1.83 |
| 2006-2022 | 1 | 29 | -5.45 | 2.77 | 6.10 | 5.45 |
| 2006-2022 | 2 | 28 | -0.23 | 2.34 | 2.31 | 1.76 |
| 2014-2022 | 1 | 22 | -6.04 | 2.49 | 6.51 | 6.04 |
| 2014-2022 | 2 | 21 | -0.09 | 2.66 | 2.60 | 2.07 |

### 2.2 Erro do agregado, uma observação por eleição

- 2º turno (n=7 eleições: 1989, 2002, 2006, 2010, 2014, 2018, 2022): 1989: -1.38, 2002: -2.50, 2006: -0.90, 2010: -0.41, 2014: +0.34, 2018: +0.97, 2022: -1.43. Média -0.76 pp, DP 1.17, erro padrão da média 0.44; RMS 1.32 pp; 5 de 7 negativos.
- 1º turno (7 eleições com núcleo sem conversão parcial; 1989 e 1994 ficam de fora): 1998: +1.94, 2002: -1.70, 2006: -6.04, 2010: -1.82, 2014: -6.90, 2018: -6.86, 2022: -5.03. RMS 4.88 pp. De 2002 em diante (6 eleições), todas negativas: média -4.73, DP 2.40.

Atenção às amostras minúsculas: sete observações de 2º turno não sustentam um intervalo estreito para um σ.

## 3. Respostas às perguntas-chave

**Os erros do 1º turno foram muito maiores que os do 2º?** Sim. Para o candidato de direita/PSDB, o erro absoluto médio do núcleo (pesquisas individuais, campo <=7 dias, sem conversões parciais) foi 5.1 pp no 1º turno e 1.8 pp no 2º (1989-2022), RMSE 5.8 contra 2.35. Em 2006-2022: RMSE 6.1 contra 2.3. O erro do agregado fica em torno de 4.9 pp RMS no 1º e 1.3 pp RMS no 2º. Em 2014, 2018 e 2022 o candidato de oposição (Aécio, Bolsonaro, Bolsonaro) foi subestimado em 5 a 7 pp no 1º turno e ficou entre -1,4 e +1,0 pp no 2º (agregado do núcleo).

**Houve viés persistente de subestimar o candidato de direita/oposição?** Depende do turno.
- 1º turno: sim, de 2002 a 2022 os 6 agregados saem negativos (de -1.7 a -6.9 pp); 2006, 2014, 2018 e 2022 passam de 5 pp. A contraparte é a superestimação dos candidatos do PT e de terceiros: Dilma +6,2 (2010) e +4,2 (2014), Lula +4,1 (2006), Marina +3,2 (2014), Ciro +2,8 (2022), Alckmin +3,2 e Marina +2,5 (2018). Exceção em sentido oposto: FHC superestimado em 1998 (candidato do governo; 1994 só tem linhas de conversão parcial).
- 2º turno: não há viés robusto. Média dos agregados -0.76 pp (erro padrão 0.44), sinal alternando (2014 e 2018 positivos, 2022 negativo). O único sinal fraco é 5 negativos em 7.
- Mecanismos citados na literatura (seção 6), não testados aqui: voto útil de última hora (2014 Marina -> Aécio; 2022 Ciro e Tebet -> Bolsonaro), alocação dos indecisos, abstenção diferencial (Fundação Perseu Abramo), não resposta e subrepresentação de eleitores de direita (hipótese, sem teste), amostras defasadas pelo Censo de 2010 (Gorila).
- Cuidado de medida: em 2022 a Fundação Perseu Abramo mostra que, medido em votos totais (com abstenção), Bolsonaro não foi subestimado; o "viés" aparece na conversão para válidos.

**σ do modelo (2,0 pp).** Para pesquisa individual de 2º turno o RMSE histórico do núcleo é 2.31 (2006-2022, 28 pesquisas) a 2.35 (1989-2022); para a média das pesquisas finais, RMS 1.32 em 7 eleições. Ou seja, 2,0 pp é plausível para erro de média, apertado para pesquisa isolada, e muito apertado para qualquer uso no 1º turno (RMS do agregado 4.9 pp). Se o 2,0 foi estimado só no 1º turno de 2026, vale conferir se aquele erro foi atipicamente pequeno frente ao histórico (não verifiquei os dados de 2026; há uma coluna do Quaest de 06/10/2026 em https://quaest.com.br/pesquisas/ dizendo que as urnas confirmaram a tendência final, lida só por resumo).

## 4. Resultados oficiais (votos válidos)

Arquivo `historico_resultados_oficiais.csv`. 2010-2022: tabelas da Wikipedia pt "Resultados da eleição presidencial no Brasil em ANO" (secundária; cita TSE/Folha), conferidas contra a Wikipedia en. 1989-2006: soma dos dados abertos do TSE feita por subagente (1989-1998: https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_uf/votacao_candidato_uf_1989.zip e arquivos `votacao_candidato_munzona_1994.zip`/`_1998.zip`, conferidos com TRE-SC, Georgetown e UOL) ou compilação UOL/Fernando Rodrigues (2002-2006, marcada `secundaria`). O portal tse.jus.br devolve 403 a robôs: nenhum dos números 2002-2022 foi lido diretamente do TSE nesta sessão. Georgetown PDBA tem 2º turno 2002 errado (61,43); o oficial é 61,27.

## 5. Linhagem de institutos (campo `linhagem`)

| Nome(s) | Linhagem | Fonte |
|---|---|---|
| Ibope (Ibope Opinião, Ibope Inteligência) -> Ipec | Mesma equipe de opinião: em 2021 o direito de uso da marca acabou, a Ibope Inteligência foi encerrada e ex-diretores (Márcia Cavallari) fundaram o Ipec com boa parte dos profissionais e métodos "semelhantes". Registrado como `Ibope->Ipec`. Metodologia semelhante, não idêntica | https://pt.wikipedia.org/wiki/Ipec ; https://pt.wikipedia.org/wiki/IBOPE |
| DataPoder360 -> PoderData | Criada em abril de 2017 como DataPoder360, renomeada PoderData em 5/8/2020 | https://pt.wikipedia.org/wiki/Poder360 |
| Atlas Político / AtlasIntel (em registros de 2022 "Arko Advice/AtlasIntel") | Nome anterior "Atlas Político" (sem data na fonte); Arko Advice aparece como contratante, não como renome | https://pt.wikipedia.org/wiki/AtlasIntel |
| CNT/Sensus (até 2014) e CNT/MDA (2014 em diante) | NÃO é renome: a CNT contratou institutos diferentes. Mantidos como linhagens separadas (`Sensus`, `MDA`). Linhagem MDA/Sensus não verificada em fonte | Itaú (2018) cita só CNT-MDA após 2006; ver seção 6 |
| Datafolha | Sem renome | https://pt.wikipedia.org/wiki/Datafolha |
| Vox Populi | Sem renome documentado (fundada em 1984, Belo Horizonte) | https://pt.wikipedia.org/wiki/Vox_Populi |
| Genial/Quaest, Abrapel/Ipespe, Globo/Datafolha etc. | Prefixo é contratante, não renome. Origem/fundação do Quaest e do Ipespe não verificada | — |
| Paraná Pesquisas | Sem histórico de nome na fonte | https://pt.wikipedia.org/wiki/Paran%C3%A1_Pesquisas |

## 6. Literatura e análises achadas (URL e achado principal)

| Fonte | URL | Achado principal |
|---|---|---|
| Pindograma, "Quatro lições que tiramos do desempenho das pesquisas em 2022" (Daniel Ferreira; a URL traz 2022/09/05, mas o texto traz dados do pleito de outubro e o repositório do Pindograma data o material de 2022-10-05) | https://pindograma.com.br/2022/09/05/desempenho-pesquisas-22.html | Erro médio por candidato das últimas pesquisas presidenciais nacionais: 3,17 (2014), 2,46 (2018), 2,53 (2022). Ipec/Ibope/Datafolha 2,36 / 2,00 / 2,37 contra 3,71 / 2,59 / 2,56 dos demais. Agregador (PollsterGraph) melhor que institutos isolados. Correlação do ranking 2012-2020 com o desempenho de 2022 = 0,03. Não mede viés nem separa turnos |
| Pindograma, ranking de institutos | https://pindograma.com.br/ranking.html | Pesquisas de 2012 a 2022, exclui institutos com menos de 5 pesquisas; avisa que desempenho passado não prediz o futuro |
| Itaú Asset Management (2018), "Pesquisas Eleitorais no Brasil: White Paper" | https://assetfront.arquivosparceiros.cloud.itau.com.br/ISG/Pesquisas_Eleitorais_no_Brasil_White_Paper.pdf | Presidenciais 1994-2014, medidas de Mosteller. Nenhum instituto consistentemente superior; desvios muitas vezes maiores que o sugerido pelas margens de erro; em 2010 e 2014 os desvios nos dois meses antes do 1º turno foram maiores que em ciclos anteriores; o 2º turno difere entre ciclos. FHC 1994 convergiu mais de 20 pp em 4 meses |
| Matheus Tancredo Toledo (NOPPE/Fundação Perseu Abramo), 05/10/2022 | https://fpabramo.org.br/2022/10/05/onde-as-pesquisas-podem-ter-errado | Em válidos, Bolsonaro subestimado em 7,2 (Datafolha), 6,2 (Ipec), 5,2 (Quaest), 2,1 (Atlas). Em votos totais não há subestimação; hipótese de abstenção diferencial. Autoria ligada ao PT, ler com isso em mente |
| Gustavo Maia, Gorila, 17/10/2022 | https://gorila.com.br/blog/pesquisas-eleitorais/ | Tabela do 1º turno 2022 por instituto (erro em Bolsonaro de -2,1 Atlas a -8,8 Ipespe); hipóteses: voto útil de última hora, Censo de 2010 desatualizado, Datafolha sem calibragem por renda, voto envergonhado. Só Atlas (web) e Quaest calibraram por renda |
| Mais Retorno / Reuters, 04/10/2022 | https://maisretorno.com/portal/por-que-os-institutos-de-pesquisa-derraparam-no-1o-turno-das-eleicoes | Pesquisas davam Lula +7 a +17; resultado +5. Hipóteses de analistas: voto envergonhado, ausência de Censo, voto tático, desconfiança. Jornalístico |
| El-Dash (2010), tese IME-USP | http://pollingdata.com.br/menu_pesquisas/Tese_Doutorado_Neale%20-%20pesquisas.pdf | 898 pesquisas Datafolha e Ibope 1989-2004; erro explicado sobretudo por variância e tamanho da amostra; cita guia ABEP: erro médio 3% (totais) e 2% (válidos) em 469 pesquisas de 1982-1998 (via subagente) |
| Plano Político, "Desempenho de Pesquisas" | https://www.planopolitico.com.br/desempenho-de-pesquisas/presidente-2002-t1/ | Painel de erro ponderado por eleição, inclui presidente 2002 e 2006 (valores dependem de JavaScript; não extraídos) |
| Datafolha, "Balanço das eleições 2006" | https://datafolha.folha.uol.com.br/eleicoes/2006/10/1193337-balanco-das-eleicoes-2006.shtml | Autoavaliação do instituto (não independente): diz ter detectado a queda de Lula após o dossiê |
| Figueiredo e Coutinho (2003), Opinião Pública 9(2) | https://www.scielo.br/j/op/a/PrCDsL5LptPxsbGYLjR8RTK/?lang=pt | Conta 70 divulgações em 2002 (Ibope 23, Datafolha 15, Sensus 12, Vox Populi 20); não mede erro |
| Renno (2007), Opinião Pública 13(2) | https://www.redalyc.org/pdf/329/32913202.pdf | Efeito de escândalo no voto de 2006; contexto do erro de 1º turno 2006 (conteúdo não lido a fundo) |
| Mendes e Venturi (Datafolha), Opinião Pública, dez/1994 | https://www.cesop.unicamp.br/vw/1IE*HMDM_MDA_60e3c_ | Análise do Datafolha da sucessão de 1994 (texto não aberto; CESOP fora do ar) |
| Wikipedia pt, AtlasIntel | https://pt.wikipedia.org/wiki/AtlasIntel | Afirma que o Atlas foi dos mais precisos em 2022 e subestimou Bolsonaro menos que os demais (9 pontos projetados contra 5 reais; fonte parcialmente do próprio instituto) |
| Revista Fórum, 12/02/2026 | https://revistaforum.com.br/politica/de-1989-a-2022-pesquisas-acertaram-vencedores-mas-erraram-muita-coisa/ | Jornalístico: nenhum vencedor errado desde 1989, mas o 2º turno e a virada final escapam |

**Não achado** (WebSearch esgotou o teto de 200 por turno; WebFetch seguiu): textos de Jairo Nicolau, ABEP pós-2022, Revista Brasileira de Ciência Política, Estadão e Folha pós-2022. A busca no SciELO devolveu 403. Não declarei achado o que não li.

## 7. Lacunas, riscos e becos

- **Base das pesquisas 2010-2022 = tabelas da Wikipedia (secundária)** com a URL da matéria citada por cada linha; os números das pesquisas finais de Datafolha, Ibope/Ipec, Quaest e Atlas batem com o que a imprensa divulgou. Os arquivos não foram confrontados um a um com os PDFs de registro do TSE. A base aberta do Pindograma (`dados/externo/pindograma_ranking_de_institutos/data/polls/`, derivada do registro TSE) serviu para n, data de início e para achar pesquisas finais ausentes da Wikipedia: Quaest 2022 1º turno (30/09-01/10, n=3.600, BR-02444/2022), CNT/Sensus 2014 (1º e 2º turno), Vox Populi 2018 (1º turno 6/10 e 2º turno 27/10), Veritá e Paraná Pesquisas 2014 2º turno. Isso prova que as tabelas da Wikipedia são incompletas; outras pesquisas finais podem faltar.
- **Cauda longa não incluída**: o registro de 2022 tem dezenas de institutos obscuros com valores absurdos (Lula 72%, por exemplo). Ficaram só institutos da Wikipedia mais os achados acima. A base do Pindograma permite incluí-los.
- **1989-2006**: poucos institutos (Datafolha, Ibope, Vox Populi, Sensus). Faltam Ibope 1989, Gallup/Vox/Sensus/MDA/Brasmarket finais de 1989-1998, n do Ibope e do Vox em 2002, datas do Ibope 1994, 1998 e 2006. Boca de urna (Datafolha 1989 e 1998, Ibope 1998 e 2006) foi coletada pelos subagentes e ficou fora das estatísticas. Discrepâncias de fonte registradas pelos subagentes: Datafolha 1994 (Enéas 6 na Folha e ausente no PDF); Ibope 2006 (Alckmin 38 na Folha, 37 no Congresso em Foco); Sensus 2006 1º turno foi a campo 6 dias antes da eleição.
- 2014 1º turno: Ibope, Vox Populi e MDA de 3-4/10 sem n confirmado (n da imprensa só para Datafolha).
- Pesquisas com campo antigo entram como "última do instituto" (ver `dias_antes_eleicao`).
- Votos válidos publicados lidos de títulos/URLs: aplicada checagem automática contra a conversão (descarta divergência >2 pp). Três descartes: Ipespe 2018 (slug capturou margem), Ibope 2014 2º turno (linhas antigas).
- **Becos**: tse.jus.br e sig.tse.jus.br dão 403; CESOP/Unicamp fora do ar (503); Wayback 429; DuckDuckGo bloqueia robô; SciELO 403; Wikipedia en/pt sem página de pesquisas para 2002 e 2006; PDF do Itaú não rendeu texto via WebFetch (lido com pdftotext).
