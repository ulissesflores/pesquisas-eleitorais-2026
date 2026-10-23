# Rankings e avaliações publicados de acurácia de institutos brasileiros

Coletado em 2026-10-23. Regra: campo não achado = "não achado"; todo número tem URL. Nenhum arquivo baixado foi executado (só lido como dado). Este arquivo complementa `dados/subnacional_erros.csv` (a presidencial 1989-2022 está com outro agente).

## 1. Resumo executivo

| Fonte | Janela | Métrica | Líder | Cauda | Peso como evidência |
| --- | --- | --- | --- | --- | --- |
| Pindograma 2024 (197 institutos) | 2012-2022 (banco bruto 2012-2018: 6.062 pesquisas; o ranking usa só pesquisas de reta final) | erro percentual médio ajustado, prior encolhido | Amostragem, Futura, Ipec/Ibope, AtlasIntel (nota A) | Gerp, Instituto França (B-) | Alto: método e código abertos; mas o próprio Pindograma mediu correlação 0,03 entre nota 2012-2020 e desempenho 2022 |
| BTG Pactual (via Revista Fórum) | presidenciais desde 2002 | proximidade das pesquisas de reta final | MDA, Datafolha, Ipec/Ibope, Quaest, Paraná Pesquisas | Futura, Veritá, PoderData, Ipespe, Sensus | Médio: só posições, sem fórmula nem n |
| PollsterGraph (via Diário do Pará) | não informada | nota composta e erro médio | Datafolha (3,2), AtlasIntel (3,4) | Quaest em 67º (8,8) | Baixo: janela e n não informados, página bloqueada (403) |
| ElectioLab | 2018 e 2022 | desvio absoluto médio convertido em score | Gerp (100%, n=20), Datafolha 92%, Ipec 88% | Veritá 65% | Baixo: score 100% para n=0 a 6 |
| Hub Político 2026 | 1º turno 2026, 425 últimas pesquisas | erro na margem, válidos | Datafolha 5,7%, Quaest 6,5%, AtlasIntel 8,0% | Paraná Pesquisas 8,8% | Alto para 2026 1T: método claro e datado 05/10/2026 |
| AtlasIntel "mais preciso" | 2019-2026, 102 "acertos" | média de erro por pleito, comparação só com concorrentes do mesmo pleito | AtlasIntel (autodeclarado) | n/a | Baixo: autopublicado, sem método verificável |

Conclusão que o artigo pode sustentar: nenhum ranking publicado é estável nem independente do critério. Datafolha, Ipec/Ibope e MDA aparecem no topo em janelas longas de presidencial (BTG); AtlasIntel e Futura sobem no Pindograma porque a nota pondera erro relativo ao campo e cobre governador/prefeito; Quaest oscila de 3º a 67º conforme a fonte. Passado prevê mal o futuro (Pindograma: 0,03).

## 2. Fichas por fonte

### 2.1 Pindograma (principal e reprodutível)

- Ranking 2020 (método): https://pindograma.com.br/2020/09/07/ranking.html
  - Janela: 2012-2018 (6.062 pesquisas no banco). 1º turno até 21 dias antes, 2º turno até 14 dias.
  - Métrica: erro médio ajustado = desvio-padrão das diferenças assinadas candidato a candidato (votos válidos). Regressão por tipo, escopo, turno, antecedência, amostra, UF e % de indecisos; mistura com erro relativo aos concorrentes; 30 pesquisas "neutras" de encolhimento; seis faixas A, B+, B, B-, C, D (regra de Sturges).
- Mudanças 2022: https://pindograma.com.br/2022/06/24/rankingat.html
  - Troca o desvio-padrão por média dos erros absolutos (intuitiva); encolhimento cai de 30 para 15; adiciona 171 pesquisas de 2º turno 2020.
- Desempenho 2022: https://pindograma.com.br/2022/09/05/desempenho-pesquisas-22.html
  - Última pesquisa de cada instituto até 7 dias antes. Erro médio por candidato: presidente nacional 2,46 pp (2018) e 2,53 pp (2022); governador 3,65 (2018) e 3,53 (2022). Ipec/Ibope+Datafolha vs resto, vantagem: presidente 1,35 pp (2014), 0,59 (2018), 0,19 (2022); governador 0,63, 0,88, 0,19. Agregador bateu o Ipec em 19 de 22 estados; a nota 2012-2020 correlaciona 0,03 com 2022. Código e dados: https://github.com/pindograma/materias/blob/master/2022-10-05-desempenho-pesquisas-22/Pesquisas.Rmd
- Ranking vigente (atualizado 24/09/2024): https://pindograma.com.br/ranking.html. Janela 2012-2022, mínimo 5 pesquisas. Dados da tabela baixados de https://github.com/pindograma/pindograma.github.io/blob/HEAD/assets/ranking_data_4.js (commit "update pollster ratings", 24/09/2024), 197 institutos, 9 com nota A. Ordem por `pred_pm_adj` (menor = melhor):

| Posição | Instituto (nome na fonte) | Nota | Índice final | Erro % médio | Pesquisas |
| --- | --- | --- | --- | --- | --- |
| 1 | Instituto Amostragem | A | -1,022 | 3,396 | 43 |
| 2 | Futura | A | -0,752 | 3,295 | 72 |
| 5 | Ipec (antigo Ibope) | A | -0,606 | 3,336 | 1089 |
| 8 | AtlasIntel | A | -0,576 | 2,601 | 79 |
| 12 | MDA | B+ | -0,425 | 3,924 | 29 |
| 13 | Paraná Pesquisas | B+ | -0,421 | 3,325 | 126 |
| 14 | Datafolha | B+ | -0,395 | 3,157 | 190 |
| 46 | Quaest | B | 0,013 | 3,440 | 31 |
| 54 | Real Time Big Data | B | 0,066 | 4,000 | 158 |
| 70 | Ipespe | B | 0,173 | 4,222 | 58 |
| 104 | PoderData | B | 0,367 | 3,303 | 9 |
| 113 | Veritá | B | 0,441 | 4,853 | 155 |
| 129 | Instituto França | B- | 0,588 | 5,097 | 26 |
| 149 | Gerp | B- | 0,844 | 5,953 | 11 |

  Não consta (nome não achado na tabela): Palver, Nexus. A tabela publicada não cobre eleições de 2024 (janela até 2022); não achado atualização pós-2024 municipal.
- Código do cálculo (2024): https://github.com/pindograma/ranking_de_institutos, arquivo `pollster_ratings.Rmd`: ponderação por ano 0,93^(2022-ano); média e prior por registro em CONRE/ABEP; encolhimento n/(n+15); faixas por histograma.

### 2.2 BTG Pactual (via Revista Fórum, 26/03/2026)

- URL: https://revistaforum.com.br/noticias/quais-pesquisas-mais-acertaram-eleicoes-presidenciais-segundo-btg/
- Janela: presidenciais desde 2002, reta final de 1º e 2º turnos. Fórmula, denominador e n não informados (a matéria só traz posições).
- Geral: topo MDA, Datafolha, Ipec/Ibope, Quaest, Paraná Pesquisas; cauda Futura, Veritá, PoderData, Ipespe, Sensus.
- 2º turno: topo MDA, Quaest, Datafolha, Futura, Ipec/Ibope; cauda Veritá, Ipespe, PoderData, Atlas, Sensus.
- 1º turno: topo MDA, Atlas, Paraná Pesquisas, Ipec/Ibope, Datafolha; cauda Vox Populi, PoderData, Sensus, Futura, Ipespe.
- Relatório original do BTG: não achado (só a reprodução jornalística).

### 2.3 AtlasIntel "mais preciso"

- Alegação (A Tarde, 03/06/2026): https://atarde.com.br/atlasatarde/atlasintel-foi-o-instituto-mais-preciso-em-102-eleicoes-ao-redor-do-mundo-nos-ultimos-7-anos-1391022
  - "Mais preciso" não é definido; a métrica citada é erro médio, só para o 1º turno colombiano de 2026; "102" é contagem de "acertos" (o título diz eleições); anexo "histórico de resultados" vazio na página; seção "AtlasIntel/A TARDE" sugere parceria comercial. Tratar como autodeclarado.
- Silver Bulletin (fev/2025): https://www.cnnbrasil.com.br/politica/atlasintel-fica-em-1o-lugar-em-ranking-de-institutos-de-pesquisa-nos-eua/ : nota A+ e 1º lugar entre "centenas" de institutos que pesquisaram eleições dos EUA; é desempenho em eleição americana, não brasileira.
- Comparativo municipal 2º turno 2024 (autopublicado): https://www.atlasintel.org/media/comparativo-pesquisas-municipais-2o-turno-2024 : afirma menor erro médio em BH, Curitiba, Aracaju, Goiânia, Belém; reconhece que em Fortaleza, Natal e Palmas outros ficaram mais perto. Sem tabela por instituto (só imagens). Nossos dados do CSV batem nas capitais comuns (Atlas Curitiba -0,14 pp, Goiânia -0,03 pp), mas em BH (-0,51) o Datafolha (-0,39) e o Futura (+0,06) ficaram mais perto na nossa conta e em Belém o Veritá (+1,14) ficou mais perto que o Atlas (+2,54); a alegação de "menor erro" depende do critério (erro médio da pesquisa inteira, não só do vencedor).
- 2022: https://pindograma.com.br/2022/09/05/desempenho-pesquisas-22.html : Atlas mais preciso que o agregador em 7 de 10 estados, pior no Paraná, Rio e na presidencial.

### 2.4 PollsterGraph (via Diário do Pará, 03/10/2026)

- URL: https://diariodopara.com.br/eleicoes-2026/datafolha-lidera-ranking-de-pesquisas-atlasintel-vem-em-2o-e-quaest-em-67o/ (site https://pollstergraph.com/ranking devolveu 403 ao fetch; não verificado diretamente).
- Fatores: número de pesquisas, desempenho comparativo, desempenho objetivo, erro médio. Janela, eleições cobertas e total de institutos: não informados.
- Posições citadas: 1 Datafolha (A+, 29 pesquisas, erro médio 3,2), 2 AtlasIntel (A+, 8, 3,4), 6 MDA (A+, 6, 3,6), 11 Paraná Pesquisas (A, 71, 3,9), 12 Real Time Big Data (A, 67, 4,6), 14 Futura (A, 29, 3,9), 67 Quaest (B-, 6, 8,8).
- Nota de cautela: 4pp.com.br diz que o PollsterGraph usa viés de timing e não o acerto de véspera como base de correção.

### 2.5 ElectioLab

- URL: https://electiolab.com/institutos
- Janela 2018 e 2022; eleições recentes e cargos majoritários pesam mais; denominador e n não definidos. 69 institutos. Scores: Gerp 100% (20), Datafolha 92% (122), Ipec 88% (6), Quaest 85% (233), PoderData 80% (238), Atlas 78% (131), Ipespe 77% (3), MDA/CNT 75% (6), Real Time Big Data 72% (199), Paraná Pesquisas 70% (65), Nexus 70% (25), Futura Inteligência 68% (4), Veritá 65% (50).
- Defeito: dezenas de institutos com n=0 e score 70% ou 100% (padrão), logo ranking não utilizável sem filtro de n.

### 2.6 Hub Político, precisão 2026 (1º turno de 05/10/2026)

- URL: https://hubpolitico.com.br/inteligencia/relatorios/eleicao-2026/precisao-dos-institutos
- Métrica: erro na margem (vantagem do classificado sobre o primeiro fora, pesquisa menos urna), em votos válidos. Inclui a última pesquisa de cada instituto, campo até 30 dias antes, cenário principal, registrada no TSE. Ranking geral exige 5 disputas e cobertura de 80% das últimas pesquisas. 425 pesquisas, 82 institutos, 55 disputas (1 presidente, 27 governos, 27 Senado); totalização TSE de 05/10/2026 12h51.
- Ranqueados: Datafolha 5,7% (10 de 15 vencedores), Neokemp 6,1%, Quaest 6,5%, AtlasIntel 8,0%, Real Time Big Data 8,1%, Paraná Pesquisas 8,8%. Fora do ranking por cobertura: DataTrends 5,1%, Instituto França 6,0%, Futura 6,1%, Veritá 6,5%, Gerp 9,5%. Poucas disputas: PoderData 4,8% (3), Ipespe 7,0% (2), Nexus 7,1% (1), MDA 7,6% (1), Palver 2,2% (1).
- Observação: é 2026 e usa só o 1º turno; em 23/10/2026 o 2º turno (25/10/2026) ainda não ocorreu.

### 2.7 Times Brasil, ranking das pesquisas do 1º turno 2026 (19/10/2026)

- URL: https://timesbrasil.com.br/eleicoes-2026/decisao-2026-ranking-das-pesquisas-eleitorais-mostra-diferencas-entre-as-estimativas-dos-institutos-e-o-resultado-das-urnas/
- 17 pesquisas; soma das diferenças absolutas em cinco grupos (Flávio Bolsonaro 47,0%, Lula 45,2%, Cury 2,9%, Renan Santos 2,2%, demais 2,7%); menor é melhor: Veritá 0,2; Quaest (3/10) 4,0; Gerp (3/10) 6,0; PoderData e AtlasIntel (3/10) 8,4; Palver e AtlasIntel (29/9) 9,6; Futura 9,8; Datafolha (3/10) 10,4; MDA 10,6; Instituto França 15,6; Real Time Big Data 16,4; Nexus 18,2. Datas de várias pesquisas não informadas.
- Conflito entre rankings do mesmo 1º turno: Veritá é 1º aqui e 4º em margem no Hub Político (6,5%, cobertura 70%); a métrica soma erro por candidato, não erro na margem. Veritá teve pesquisas suspensas pela Justiça Eleitoral em 14 estados em 2026 (https://www.jornalopcao.com.br/ultimas-noticias/justica-eleitoral-suspende-pesquisas-do-verita-em-14-estados-e-aponta-falhas-na-metodologia-857197/, 403 ao fetch, lido apenas no resultado de busca).

### 2.8 Outros, com ressalvas

- 4pp, ranking 2022 por erro no voto válido de Lula, 1º e 2º turno: https://4pp.com.br/ranking.php : Paraná Pesquisas 1,8, MDA 1,9, AtlasIntel 2,3, Futura 3,0, Gerp 3,1, PoderData 3,6, Quaest 3,8, Datafolha 4,5, Veritá 4,6, Ipec 5,5, Ipespe 5,6, Brasmarket 9,0. Sem denominador nem n; valores divergentes de outras fontes (ex.: Paraná Pesquisas no 2T 0,5 aqui vs 0,8 em noticiário): usar só como indício.
- Correio do Estado (24/09/2026), ranking do 1º turno presidencial de 2022 em 12 institutos: https://correiodoestado.com.br/politica/saiba-quais-os-institutos-de-pesquisas-que-mais-erraram-e-acertaram-no/406324/ : ordem inconsistente com o critério e sinais trocados; NÃO usar.
- Gramacho (2013), Opinião Pública 19(1): https://www.scielo.br/j/op/a/Qg95LjqPvrBJf37kCZYrjnM/ : 156 pesquisas de 2010 (presidente e 27 governadores), erro MM3 médio 3,6 pp; Ibope 3,2 (65 pesquisas), Datafolha 3,8 (36); diferença entre institutos não significativa; erro maior com antecedência, no 1º turno, em disputas pouco competitivas e em governador. Única análise acadêmica revisada por pares achada; janela só 2010.
- Nexo (17/08/2022), "As pesquisas eleitorais erram mais em favor da esquerda?": https://pp.nexojornal.com.br/opiniao/2022/08/17/as-pesquisas-eleitorais-erram-mais-em-favor-da-esquerda : o fetch retornou só o título; números (49,70% de 250 estimativas Datafolha/Ibope 2002-2018 fora da margem) vêm de snippet de busca, NÃO verificado.
- Congresso em Foco/Gazeta do Povo/Metrópoles 2022: apuração jornalística de erros de 2022 sem ranking (ex.: 1º turno erros de 13 a 23,5 pp em estados, Metrópoles https://www.metropoles.com/colunas/guilherme-amado/institutos-de-pesquisa-erraram-de-13-a-235-pontos-no-1o-turno-em-2022), sem método replicável.
- Poder360: não achado ranking próprio; é a fonte de dados do banco do Pindograma (https://pindograma.com.br/2020/09/07/ranking.html). Estadão, Folha, JOTA: não achado ranking de acurácia próprio (busca extendida sem resultado).

## 3. Datasets públicos baixados

Todos em `dados/externo/` (somente leitura como dado; nada executado).

| Pasta | Origem | Conteúdo | Licença |
| --- | --- | --- | --- |
| `pindograma_ranking_de_institutos/` | https://github.com/pindograma/ranking_de_institutos (commit c04d197c, 23/09/2024) | `data/polls/late_polls_*` (2012-2018, 2020, 2022; pesquisas finais com resultado por candidato), `data/resultados/*` (TSE 2020 e 2022), `nomes_empresas.csv`, `empresas_multiplos_cnpjs.csv`, `pollster_ratings.Rmd` | código GPL-3.0; dados ODbL 1.0 (README do repo `pesquisas`) |
| `pindograma_site_ranking/` | https://github.com/pindograma/pindograma.github.io (assets/ranking_data*.js, ranking.html) | tabelas do ranking publicado em 4 versões; `ranking_2024-09-24.csv` derivado do JS vigente | idem |

Não baixado por tamanho/risco: repo `pesquisas` (data/manual-data, dezenas de MB; só necessário para refazer o banco) e `materias` (replicações de matérias). Observação: o dataset termina em 2022; não há 2024.

## 4. Linhagens e renomes (com fonte)

| Instituto | Linhagem confirmada | Fonte |
| --- | --- | --- |
| Ibope Inteligência -> Ipec | Marca Ibope deixa de ser usada ao fim de jan/2021 (fim da licença com a Kantar); Márcia Cavallari, CEO do Ibope Inteligência, e executivos abrem Inteligência, Pesquisa e Consultoria LTDA (Ipec) sob outro CNPJ, com a mesma capacidade operacional. Ipsos anunciou a compra do Ipec em fev/2025. O Pindograma agrupa os dois CNPJs (40735589000190 e 68802370000186) sob "Ipec (antigo Ibope)". | https://www.meioemensagem.com.br/midia/marca-ibope-inteligencia-deixa-de-ser-usada ; https://www.metropoles.com/negocios/gigante-francesa-de-pesquisas-anuncia-compra-do-ipec-antigo-ibope (só snippet de busca) ; `empresas_multiplos_cnpjs.csv` |
| DataPoder360 -> PoderData | Divisão de pesquisas do jornal Poder360, lançada em 2017 como DataPoder360, renomeada PoderData em 05/08/2020. Mesmo CNPJ 29550908000150 no Pindograma. | https://www.poder360.com.br/economia/divisao-de-pesquisas-do-poder360-agora-e-poderdata/ |
| PoderData/Aya (2026) | NÃO é mudança de instituto: Aya Bancah (banca digital) é parceira de divulgação; o PoderData faz a pesquisa com recursos próprios (URA telefônico, 2.400 entrevistas, TSE BR-07845/2026). | https://www.poder360.com.br/poderdata/leia-os-resultados-da-pesquisa-poderdata-aya-para-presidente/ |
| Futura | Instituto "Futura Inteligência" (Futura Consultoria e Assessoria Ltda., fundação 1992 segundo a Gazeta do Povo), ligado ao ecossistema Apex/100% Cidades (Fernando Cinelli, 100% Cidades Participações Ltda.). Em 2026 as pesquisas saem como "Futura/Apex" (também "Apex/Futura"); em 2024 como "Futura/100% Cidades". Dois CNPJs agrupados no Pindograma. Não é troca de nome por sucessão: são marcas/parcerias do mesmo instituto. | https://www.gazetadopovo.com.br/ideias/quem-sao-os-donos-dos-principais-institutos-de-pesquisa-brasil/ ; https://www.cnnbrasil.com.br/eleicoes/futura-apex-flavio-e-lula-empatam-tecnicamente-no-2o-turno/ |
| Gerp | "Gerp Mercadologia", fundador e presidente Gabriel Pazos, fundado em 1983 (Gazeta do Povo); dois CNPJs agrupados no Pindograma. Sem renome achado. | https://www.gazetadopovo.com.br/ideias/quem-sao-os-donos-dos-principais-institutos-de-pesquisa-brasil/ |
| Veritá | Fundado em 1995 por Orlei Moreira; gestão de Adriano Silveira (Gazeta do Povo). O Pindograma lista "Veritá" e "Veritate" (CNPJ 05255333000185) como empresas distintas; não achado vínculo. Notícia de 2026 cita o proprietário como Adriano Silvoni (grafia diferente da Gazeta; não conciliado). | Gazeta do Povo (link acima) ; Jornal Opção (link 2.7) |
| MDA | Opera como CNT/MDA; parceira da CNT desde 2012. | Gazeta do Povo (link acima) |
| Quaest | "Genial/Quaest" em 2018-2022 (nome no CSV: "Genial/Quaest" em coluna linhagem). Fundador Felipe Nunes, 2016. | Gazeta do Povo (link acima); renome Genial/Quaest: não verificado em fonte nesta rodada |
| Palver, Nexus, Instituto França, Ipespe, Real Time Big Data, Paraná Pesquisas, AtlasIntel | Sem renome achado. Real Time Big Data tem dois CNPJs no Pindograma (22345021000181, 29842579000111). | `empresas_multiplos_cnpjs.csv` |

## 5. `subnacional_erros.csv`: método e limites

- Origem: 88 linhas (governador 2018 e 2022, prefeito de capital 2020) extraídas do dataset aberto do Pindograma acima (script `codigo/subnacional_extrai.py`); 30 linhas de prefeito 2024 coletadas à mão (Wikipédia pt das eleições municipais 2024 que cita as pesquisas; Datafolha SP, Futura Goiânia e Atlas Goiânia direto da imprensa citada na coluna `url`).
- `cand_A` = vencedor da disputa. `erro_sinal_pp` = válido de A na pesquisa menos válido de A no resultado (positivo = superestimou o vencedor). `erro_margem_pp` = |margem pesquisa - margem resultado| (no 2º turno = 2 x |erro de A|).
- "Válido" na pesquisa = A/(A+B) sobre os números divulgados. Para o dataset do Pindograma, valores inteiros arredondados dão ruído de até 0,5 pp (ex.: Datafolha SP 2022 divulgou 53% válidos; recomputado a partir de 46 x 42 dá 52,27%). Em 2024 a coluna `url` traz `base=valido_divulgado` (o instituto já divulgou válidos) ou `base=normalizado` (normalizei a pesquisa de votos totais da tabela). A base não é a mesma entre linhas: comparar com cautela entre fontes.
- Janela: 1º turno <= 21 dias antes, 2º turno <= 14 dias (regra do Pindograma). Linhas "1 (decidida no 1T)" são disputas encerradas no 1º turno (válido de A entre os candidatos da pesquisa; menos comparáveis com a presidencial de 2º turno).
- Cobertura incompleta do dataset: Quaest tem só 5 linhas de 2º turno e PoderData, Palver, Nexus, MDA e Instituto França têm ZERO linhas (não achado nas disputas pedidas). Checagem 2022: o dataset só traz Quaest no 2T de governador do Amazonas; a tabela da Wikipédia em inglês do 2T de SP 2022 (https://en.wikipedia.org/wiki/2022_S%C3%A3o_Paulo_state_election) não lista Quaest nem PoderData (lista Ipec, Datafolha, Atlas, Paraná, Real Time Big Data, Modalmais/Futura, Badra, Brasmarket), e as tabelas de BA e PE 2022 só têm Quaest/Genial em pesquisas de maio-julho. Como a contagem de linhas reflete cobertura e não acurácia, ranking por instituto derivado deste CSV deve usar n por instituto e não média simples.
- Conferência cruzada SP 2T 2022: Ipec (26-29/10, 46x42), Atlas (26-29/10, 51,2x46,3), Paraná (23-27/10, 52,2x36,9) e Real Time Big Data (24-25/10, 50x39) da Wikipédia batem com as linhas do dataset (52,27; 52,51; 58,59; 56,18). O Datafolha aparece na Wikipédia com datas 17-19/10 (provável erro de data da tabela); o valor 46x42 coincide com a linha do dataset (campo_fim 29/10). Capitais 2024 decididas no 1º turno (RJ, Porto Alegre, Recife, Salvador) e BH/Fortaleza/Curitiba/Goiânia/Belém/SP no 2º turno: só os 6 de 2º turno foram coletados.
- Ruído de rótulo: o dataset marca `Ibope` e `Ipec (antigo Ibope)` pelo mesmo `company_id`; no CSV usei `Ibope` para 2018/2020 e `Ipec` para 2022.
- Verificação pontual contra imprensa: Datafolha SP 2018 (França 51 x Doria 49 válidos, batendo com 49,41 do dataset), Datafolha SP 2022 (53 x 47 divulgado contra 52,27 do dataset), Datafolha SP 2024 (57 x 43). Os demais não foram reverificados contra o PDF original.

## 6. Becos

- PollsterGraph direto: 403. Ranking de acurácia próprio de Poder360, Estadão, Folha, JOTA: não achado. Relatório BTG original: não achado. Nexo 2022: corpo da página não carregou. Wikipédia Goiânia 2024 sem tabela de pesquisas (usado Atlas e Futura pela imprensa). 4pp e Correio do Estado: inconsistentes.
