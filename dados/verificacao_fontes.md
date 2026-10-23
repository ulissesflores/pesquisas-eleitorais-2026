# Verificação de fontes do documento base (auditoria pré-publicação)

Documento auditado: `fonte/base-metodologica-v0-2026-10-23.md`
Data da auditoria: 2026-10-23. Companheiro: `dados/rodadas_1t.csv`.

> [!IMPORTANT]
> Registro no TSE: o PesqEle (`pesqele-divulgacao.tse.jus.br`) devolve 403 (Akamai) para `curl`/WebFetch, mas o **dado aberto do TSE funcionou**: `https://cdn.tse.jus.br/estatistica/sead/odsele/pesquisa_eleitoral/pesquisa_eleitoral_2026.zip` (+ `pesquisa_pagante_2026.zip`, `pesquisa_contratante_2026.zip`), gerado em 23/10/2026 05:46, 3.648 registros. Conferi **[li, TSE]** cada `BR-xxxxx/2026` citado (empresa, cargo, campo, n, pesquisa própria S/N, custo, pagante). Ver seção "Registro TSE (dados abertos)" no fim. A API de resultados do TSE também funcionou (item 1).
> Legenda de confiança: **[li]** = li o HTML/PDF bruto eu mesmo; **[sub]** = relatado por subagente que leu a fonte, não reverificado; **[fetch]** = só resumo do WebFetch.
> A cota de WebSearch da sessão esgotou no fim; nada foi buscado depois disso.

## Item 1. Resultado oficial do 1º turno (TSE)

Fonte primária **[li]**: `https://resultados.tse.jus.br/oficial/ele2026/6257/dados/br/br-c0001-e006257-u.json` (eleição 6257 = Presidente 1º turno, ciclo ele2026; `tf`=s totalização final; 499.248 de 499.248 seções = 100,00%; carimbo 05/10/2026 12:51:47). O índice dos ciclos está em `https://resultados.tse.jus.br/oficial/comum/config/ele-c.json`. A página `https://resultados.tse.jus.br/oficial/app/index.html` é uma SPA sem conteúdo estático; os caminhos `dados-simplificados/.../-r.json` dão 404 em 2026 (e em 2022); o arquivo `-u.json` é o que serve o resultado.

| Afirmação do documento | Valor achado | Fonte (URL) | Veredito |
| --- | --- | --- | --- |
| Votos válidos totais 119.300.788 | 119.300.788 (soma dos 12 candidatos = `vv`; 95,23% do comparecimento) | URL TSE acima | CONFIRMADO |
| Flávio 56.104.503 / 47,03% | 56.104.503 / 47,03 (47,0278) | idem | CONFIRMADO |
| Lula 53.879.538 / 45,16% | 53.879.538 / 45,16 (45,1581) | idem | CONFIRMADO |
| Cury 3.448.569 / 2,89% | 3.448.569 / 2,89 | idem | CONFIRMADO |
| Renan 2.675.887 / 2,24% | 2.675.887 / 2,24 | idem | CONFIRMADO |
| Caiado 2.605.148 / 2,18% | 2.605.148 / 2,18 | idem | CONFIRMADO |
| Zema 326.488 / 0,27% | 326.488 / 0,27 | idem | CONFIRMADO |
| Demais ~260.655 / ~0,22% | exatos 260.655 = Samara 122.911 + Hertz 43.103 + Clariana 40.043 + Edmilson 22.693 + Grassi 16.881 + Rui 15.024 (0,2185%) | idem | CONFIRMADO (trocar "~" por o valor exato) |
| Diferença 2.224.965 votos | 56.104.503 - 53.879.538 = 2.224.965 | cálculo sobre o TSE | CONFIRMADO |
| Eliminados somam 9.316.747 | 3.448.569+2.675.887+2.605.148+326.488+260.655 = 9.316.747 | cálculo sobre o TSE | CONFIRMADO |
| Abstenção "cerca de 33 milhões", 21,08% | 33.469.244 (21,0836%); eleitorado apto 158.745.502; comparecimento 125.275.835 (78,92%) | URL TSE acima | CONFIRMADO (33,47 mi; "cerca de 33" subestima, escrever 33,5 mi) |
| Brancos e nulos (pedido de registrar) | brancos 2.300.798 (1,84% do comparecimento); nulos 3.674.249 (2,93%) [`tvn` = `vn` 3.669.003 + `vnt` 5.246 (nulo técnico); `vansj` (sub judice) = 0] | URL TSE acima | CONFIRMADO (documento não cita; vale incluir) |
| Margem Flávio +1,87 pp | 47,0278 - 45,1581 = 1,87 | cálculo sobre o TSE | CONFIRMADO |
| "Demais 2,7%" (grupo do Times) | Times agrega Caiado+Zema+demais = 3.192.291 = 2,676% | cálculo sobre o TSE | CONFIRMADO, mas o grupo "demais" do Times NÃO é o "Demais" da tabela do documento (que tem Caiado e Zema à parte); explicitar |
| Fonte citada: portaldeprefeitura / Correio do Estado | números idênticos; fonte secundária | URLs do documento | Trocar pela URL TSE na publicação |

## Item 2. Ranking Times Brasil/CNBC (17 pesquisas)

Fonte **[li]** (HTML bruto): `https://timesbrasil.com.br/eleicoes-2026/decisao-2026-ranking-das-pesquisas-eleitorais-mostra-diferencas-entre-as-estimativas-dos-institutos-e-o-resultado-das-urnas/` (19/10/2026, atualizado depois).

**Metodologia de D do Times (texto do artigo):** soma das diferenças absolutas, em pontos percentuais, entre a estimativa e o resultado, em **5 grupos**: Flávio, Lula, Cury, Renan e "demais candidatos". Referências, em **votos válidos** arredondados a 1 casa: 47,0 / 45,2 / 2,9 / 2,2 / 2,7 (soma 100,0). Não há denominador diferente por pesquisa: o artigo não diz como cada estimativa foi convertida.

**Resposta total x válido (o ponto crítico):**

| Afirmação | Achado | Fonte | Veredito |
| --- | --- | --- | --- |
| "Datafolha 42/45 e Nexus 38,9/44,2 parecem totais" | **Não são totais.** Datafolha 03/10: 42/45 são **válidos publicados pelo Datafolha** (Lula 45, Flávio 42, Caiado 4, Renan 3, Cury 3, Zema 1; os totais publicados foram Lula 42, Flávio 40). A soma 87 é só porque 13% estão com os outros (Caiado, Renan, Cury, Zema, resto). Nexus 38,9/44,2/5,3/4,2/7,4 soma 100,0: são **válidos normalizados pelo Times** (totais inteiros F37 L42 Cury5 Renan4 outros7, divididos por 95 = soma dos candidatos). A soma 83,1 é só Flávio+Lula | G1 Datafolha **[li]** `https://g1.globo.com/politica/eleicoes/2026/pesquisa-eleitoral/noticia/2026/10/03/datafolha-presidente-3-outubro.ghtml`; Nexus **[sub]** (PDF BTG no CSV) | DIVERGE da suspeita: a base do ranking é válidos |
| Base é válida para todas as 17 | Sim, mas a procedência varia: (a) válidos publicados pelo instituto: Datafolha (03/10 e 01/10), Quaest 03/10, AtlasIntel (ambas), PoderData, MDA, Futura, RTBD, Gerp 29/09 (inteiros); (b) **deduzidos pelo Times dos totais**: Nexus, França, Gerp 03/10 (45,7/43,6 vs 46/44 publicados), Quaest 28/09 (40/46; a Quaest não publicou válidos nessa rodada); (c) Palver não publica válidos (conjunto único, soma ~99); (d) Veritá e DataTrends: não achado | CSV + relatórios dos institutos **[sub]**; D recalculado por mim em Datafolha 03/10 (10,4 com demais residual=7), Nexus (18,2), França (15,6), PoderData (8,4), Quaest 03/10 (4,0), AtlasIntel 03/10 (8,4) | CONFIRMADO |
| "demais" do Times | É **resíduo** (100 - os outros 4 grupos), inclui Caiado, Zema e a folga de arredondamento. Quem publica inteiros leva o arredondamento como erro. Datafolha 03/10 com demais publicado (Caiado4+Zema1=5): D=8,4, não 10,4 | cálculo próprio **[li]** | Alerta metodológico |
| D 16,4 do Real Time Big Data | **Não reproduz.** Com os válidos publicados (F41 L46 Cury3 Renan5 demais5) D = 12,0 (calculei). O Times usa 41/46, que batem com o RTBD; o erro está no D ou em base não identificada. Mudaria a posição 16º para ~11º-12º | PDF RTBD **[sub]** + cálculo próprio | DIVERGE (D do Times) |
| D 6,0 da Gerp 03/10 | Com os válidos inteiros publicados (46/44/4/3/2/1) D = 4,8, continua 3º. O documento usa 45,7/43,6 (dedução do Times) como "estimado" | PDF Gerp **[sub]** + cálculo próprio | DIVERGE (procedência) |
| Quaest 03/10 45/46 | Válidos publicados; mas a Quaest usa modelo de eleitor provável: a normalização simples dos totais (F38 L40...) daria L46,0 / F43,7 e outro D | G1/CNN **[sub]** | Ressalva |

Linhas do ranking (D e posição conferidos contra o artigo; valores por candidato e registros no CSV):

| Pos. | Instituto (data) | D Times | Flávio / Lula (Times ou instituto) | Lula subestimado? (erro vs 45,16) | Estimativa no artigo? |
| --- | --- | --- | --- | --- | --- |
| 1 | Veritá | 0,2 | 47,0 / 45,2 | não (+0,04) | sim (F/L) |
| 2 | Quaest 03/10 | 4,0 | 45,0 / 46,0 | não, superestimado (+0,84) | sim |
| 3 | Gerp 03/10 | 6,0 | 45,7 / 43,6 | **sim** (-1,56) | sim |
| 4 | PoderData | 8,4 | 43,0 / 45,0 | ~exato (-0,16) | sim |
| 4 | AtlasIntel 03/10 | 8,4 | 44,1 / 47,0 | não (+1,84) | sim |
| 6 | AtlasIntel 29/09 | 9,6 | 43,1 / 46,2 (instituto) | não (+1,04) | não, vem do instituto |
| 6 | Palver | 9,6 | 47 / 43 (instituto) | **sim** (-2,16) | não |
| 8 | Futura | 9,8 | 44,8 / 42,6 (instituto) | **sim** (-2,56) | não |
| 9 | Datafolha 03/10 | 10,4 | 42 / 45 (válidos Datafolha) | ~exato (-0,16) | não (o documento cita 42/45, vem do G1) |
| 9 | DataTrends | 10,4 | nada achado | nada achado | não |
| 11 | MDA | 10,6 | 42,1 / 47,8 (instituto) | não (+2,64) | não |
| 12 | Gerp 29/09 | 12,4 | 44 / 42 (instituto) | **sim** (-3,16) | não |
| 13 | Datafolha 01/10 | 14,4 | 40 / 45 | ~exato (-0,16) | sim |
| 14 | Quaest 28/09 | 15,0 | 40 / 46 | não (+0,84) | sim |
| 15 | Instituto França | 15,6 | 40,5 / 43,9 | **sim** (-1,26) | sim |
| 16 | Real Time Big Data | 16,4 | 41 / 46 | não (+0,84) | sim |
| 17 | Nexus | 18,2 | 38,9 / 44,2 | **sim** (-0,96) | sim |

**Lula também foi subestimado?** Não de forma sistemática: dos 16 com dado, 6 subestimaram Lula (Gerp x2, Palver, Futura, França, Nexus), 6 superestimaram (Quaest x2, AtlasIntel x2, MDA, RTBD) e 4 acertaram dentro de 0,2 pp (Veritá, PoderData, Datafolha x2). O Times diz apenas que "variaram nos dois sentidos". Ou seja, o erro é concentrado em Flávio (todos os 16 dados abaixo de 47,03, exceto Veritá e Palver), não "pró-Lula" simétrico. O documento fala em "viés pró-Lula"; o dado sustenta "viés contra Flávio", não "a favor de Lula".

| Afirmação do documento sobre o ranking | Valor achado | Fonte | Veredito |
| --- | --- | --- | --- |
| 17 pesquisas, "última semana (28/09 a 03/10)" | 17 linhas conferem. Mas vários campos terminam antes de 28/09 (Quaest 28/09 campo 24-27/9; Nexus 25-27/9; AtlasIntel 29/09 23-28/9; Gerp 29/09 24-28/9; RTBD 26-30/9): a janela é de **divulgação**, não de campo | Times + relatórios **[sub]** | Ressalva |
| Posições e D da tabela | Todas as linhas D/posição do documento batem com o Times | Times **[li]** | CONFIRMADO |
| 15 de 17 abaixo de 47,0; só Veritá e Palver acertaram | idem texto do Times | Times **[li]** | CONFIRMADO |
| Quaest D 15,0 -> 4,0; Datafolha 14,4 -> 10,4 | idem | Times **[li]** | CONFIRMADO |
| Estimativas Flávio/Lula da tabela (Veritá, Quaest, Gerp, PoderData, Atlas, França, RTBD, Nexus) | todas batem com o texto do Times | Times **[li]** | CONFIRMADO |
| Datafolha "42 / 45... arredondado a inteiros no original" | O Times **não** traz Datafolha 03/10; 42/45 vêm do G1 (válidos publicados, inteiros) | G1 **[li]** | CONFIRMADO, mas fonte da linha é G1, não Times |
| E_m 2,9 (Quaest), 0,2 (Gerp), 3,9, 4,8, 4,9, 5,3, 6,9, 7,2 | recalculados com os valores do Times: batem | cálculo próprio | CONFIRMADO |
| Veritá D 0,2 e "acertou" | só o Times traz 47,0/45,2; **fonte primária da Veritá 1º turno não achada** (data, n, registro). Outras fontes dizem só 47/45 inteiros | Revista Fórum **[li]** `https://revistaforum.com.br/politica/verita-aproximou-resultado-1o-turno-lula/` | NÃO ACHADO (primária) |
| "Corpus: 17 pesquisas" inclui DataTrends | nenhuma pesquisa DataTrends achada | busca | NÃO ACHADO |

## Item 3. Votos válidos do próprio instituto e registro (pesquisas finais do 1º turno)

Todos os registros abaixo vêm de relatórios/matérias, não do PesqEle (403). Ipec e Paraná Pesquisas: nenhuma pesquisa nacional de 1º turno na última semana achada (lista do Poder360 com 14 pesquisas); NÃO ACHADO.

| Instituto (rodada) | Válidos do instituto (F / L / outros) | Totais publicados | Campo, n | Registro | Fonte (URL) | Veredito |
| --- | --- | --- | --- | --- | --- | --- |
| Datafolha 03/10 | F42 L45 Caiado4 Renan3 Cury3 Zema1 | L42 F40 | 03/10 (G1), n 4.006 | BR-01708/2026 | `https://g1.globo.com/politica/eleicoes/2026/pesquisa-eleitoral/noticia/2026/10/03/datafolha-presidente-3-outubro.ghtml` **[li]** | CONFIRMADO |
| Datafolha 01/10 | F40 L45 Cury4 Caiado3 Renan3 Zema1 | L42 F38 | 29/9-1/10, n 2.506 | BR-08039/2026 | `https://www1.folha.uol.com.br/poder/2026/10/datafolha-lula-tem-45-e-flavio-bolsonaro-40-em-votos-validos-no-1o-turno.shtml` **[sub]** | CONFIRMADO |
| Quaest 03/10 | F45 L46 Cury3 Renan3 Caiado3 | L40 F38 | 2-3/10, n 3.702 | BR-02197/2026 | `https://g1.globo.com/politica/eleicoes/2026/pesquisa-eleitoral/noticia/2026/10/03/quaest-presidente-3-outubro.ghtml` **[sub]** | CONFIRMADO |
| Quaest 28/09 | não publicou válidos (nada achado) | L39 F34 | 24-27/9, n 2.004 | BR-06520/2026 | `https://www.cnnbrasil.com.br/eleicoes/quaest-lula-tem-39-das-intencoes-de-voto-no-1o-turno-flavio-34/` **[sub]** | NÃO ACHADO (válidos) |
| AtlasIntel 03/10 | F44,1 L47,0 Renan4,6 Cury2,1 Caiado1,4 outros0,9 | F43,8 L46,7 | 27/9-2/10, n 4.945 | BR-00999/2026 | `https://static.poder360.com.br/uploads/2026/10/Pesquisa-Atlas_Bloomberg-Nacional-261003.pdf` **[sub]** | CONFIRMADO |
| AtlasIntel 29/09 | F43,1 L46,2 Renan5,3 Cury2,1 Caiado1,8 | F42,2 L45,3 | 23-28/9, n 5.005 | BR-04391/2026 | `https://static.poder360.com.br/uploads/2026/09/atlasintelnacionalpresidencia-29set2026.pdf` **[sub]** | CONFIRMADO |
| Veritá | F47 L45 (inteiros); Cury2,8 Renan2,2 | não achado | **TSE: campo 26/9-2/10, n 40.500, divulgação 3/10, própria=S, custo R$ 200.000** (identificação por n/campo; ver nota) | **BR-04522/2026** (TSE); o BR-01234/2026 da A Crítica **não existe** no dado aberto do TSE | `https://exame.com/brasil/como-o-verita-cravou-resultado-do-1o-turno-das-eleicoes-de-2026-fundador-explica/` **[sub]** | NÃO ACHADO (relatório com decimais); registro identificado no TSE |
| Gerp 03/10 | F46 L44 Cury4 Caiado3 Renan2 Samara1 (inteiros, base 2.300) | F43 L41 | 30/9-2/10, n 2.400 | BR-00509/2026 | `https://static.poder360.com.br/uploads/2026/10/presidente-gerp-nacional-outubro-1.pdf` **[sub]** | CONFIRMADO |
| PoderData | F43 L45 Cury4 (Renan3 Caiado3 lidos de gráfico) | L42 F41 | 30/9-2/10, n 4.000 | BR-03519/2026 | `https://static.poder360.com.br/uploads/2026/10/Relatorio-PoderData-Eleitoral-3out26-2.pdf` **[sub]** | CONFIRMADO |
| Real Time Big Data | F41 L46 Renan5 Cury3 Caiado3 Zema1 outros1 | L43 F39 | 26-30/9, n 2.000 | BR-09503/2026 | `https://static.poder360.com.br/uploads/2026/10/Presidencial-BR-09503-2026-Out26.pdf` **[sub]** | CONFIRMADO |
| Palver | não publica | F47 L43 Renan7 Cury1 Caiado1 | 30/9-3/10, n 5.000 | BR-00198/2026 | `https://exame.com/brasil/pesquisa-palver-para-presidente-flavio-bolsonaro-tem-47-e-lula-43-no-1o-turno/` **[sub]** | CONFIRMADO (sem válidos) |
| Nexus (BTG) | L44 F39 Cury5 Caiado5 Renan4 Zema1 Samara1 | L42 F37 | 25-27/9, n 2.000 | BR-07557/2026 | PDF BTG (URL no CSV) **[sub]** | CONFIRMADO |
| Ipec | nada achado | - | - | - | - | NÃO ACHADO |
| Paraná Pesquisas | nada achado | - | - | - | - | NÃO ACHADO |

## Item 4. Transferência de votos

| Afirmação do documento | Valor achado | Fonte (URL) | Veredito |
| --- | --- | --- | --- |
| Quaest 21/10: Cury 33% Flávio / 48% Lula | 33 / 48; 16% nulo/branco/não vai votar; 3% indecisos. Campo 17-20/10, n 2.154, BR-08535/2026 | `https://www.dgabc.com.br/Noticia/4353964/quaest-48-dos-eleitores-de-augusto-cury-migram-para-lula-e-33-para-flavio` **[li]** | CONFIRMADO |
| Quaest 21/10: Renan 51 / 25 | 51 / 25; 24% branco/nulo | idem **[li]** | CONFIRMADO |
| Quaest 21/10: Caiado 57 / 21 | 57 / 21; 22% nulo/branco/não vai votar | idem **[li]** | CONFIRMADO |
| Base das taxas | base = eleitores de cada candidato no 1º turno, sobre **totais** (inclui branco/nulo/abstenção e NS). n da subamostra por candidato **não divulgado** em nenhuma matéria | dgabc **[li]** | Ressalva; o n de 2.154 no documento é o da Quaest (correto aqui) |
| Quaest 14/10: Cury 34 Lula / 30 Flávio, 30% branco/nulo/abst. | 34 Lula / 30 Flávio / 30 branco-nulo-abst / 6 NS; campo 10-13/10, n 2.154, BR-08729/2026. O dgabc de 21/10 confirma o "30%" da semana anterior e os números de 14/10 de Renan (40/14/43) e Caiado (42/23/33) | `https://www.oliberal.com/politica/quaest-34-dos-eleitores-de-cury-migram-para-lula-no-2-turno-e-30-para-flavio-1.1182658` **[fetch/sub]** | CONFIRMADO |
| PoderData/Aya: Zema 72 Flávio / 10 Lula | 72 / 10 (15% branco/nulo, 3% NS). Campo 5-7/10, n 3.000, BR-08134/2026, ±1,8 pp. **n de Zema não divulgado**: com ~1% do 1º turno são dezenas de entrevistas (inferência) | PDF **[li]** `https://static.poder360.com.br/uploads/2026/10/Relatorio-PoderData-Eleitoral-8out26-final.pdf` (tabela p. 10); matéria citada: `https://www.correiodamanha.com.br/politica/2026/10/325589-pesquisa-poderdata-aya-aponta-flavio-bolsonaro-com-53-dos-votos-validos-no-segundo-turno-contra-47-de-lula.html` | CONFIRMADO |
| PoderData: não-votantes 42 Flávio / 34 Lula | 42 / 34 / 19 branco-nulo / 5 NS | mesmo PDF **[li]** | CONFIRMADO |
| Datafolha 08/10: 46 Flávio / 32 Lula sobre os 4 eliminados | 46 / 32 / 15 branco-nulo; campo 6-7/10, n 2.520, BR-02949/2026 (registro só no dgabc); total geral 49x45, válidos 52x48 | `https://www.metropoles.com/brasil/datafolha-46-dos-votos-de-renan-caiado-zema-e-cury-migram-para-flavio`; `https://www.dgabc.com.br/Noticia/4351747/46-dos-eleitores-de-cury-renan-santos-caiado-e-zema-migram-para-flavio-aonta-datafolha` **[sub]** | CONFIRMADO (por candidato: não achado). Cuidado com CartaCapital (Zema 60/Caiado 54/Renan 48): é outra pesquisa (18-20/08) |
| "Saldo ~1,3 milhão" com Datafolha | 9.056.092 (4 eliminados) x (46-32)% = 1,27 mi; mais "demais" ~1,3 mi | cálculo próprio | CONFIRMADO |

> [!WARNING]
> **Achado que o documento não declara:** o PoderData 5-7/10 também dá taxas para Cury (56 Flávio / 27 Lula), Renan (48 / 25) e Caiado (57 / 19), muito diferentes da Quaest (Cury 33 / 48). Com as taxas do PoderData no lugar das da Quaest (mantendo Zema e "demais"), a transferência dá **Flávio 52,1%** (calculei: gap ~4,93 mi) em vez de 51,47%. A divergência entre institutos sobre Cury (56 x 33 para Flávio) é maior que o erro de subamostra declarado; o documento deveria mostrá-la na sensibilidade.

## Item 5. Rodadas de 2º turno citadas

Dados de rodadas (campo, n, registro, totais) **[sub]** salvo onde marcado **[li]**; PesqEle 403.

| Afirmação do documento | Valor achado | Fonte (URL) | Veredito |
| --- | --- | --- | --- |
| Veritá 21/10: 50,7 | 50,7 x 49,3 válidos (matéria não rotula, soma 100: inferência); totais 49,7 x 48,2 (Quenty); campo 15-19/10; n 15.554; ±1 pp; BR-06396/2026 **[li]** (Fórum); recursos próprios **[li]** | `https://midiamax.com.br/brasil/2026/flavio-bolsonaro-tem-507-intencoes-voto-lula-493-diz-verita/`; `https://revistaforum.com.br/politica/verita-aproximou-resultado-1o-turno-lula/` | CONFIRMADO. Estranho: a rodada de 12-16/10 tem o mesmo n 15.554 |
| Quaest 21/10: 45x44 | 45 x 44 **totais** (brancos/nulos/abstenção 9, indecisos 2) **[li]**; campo 17-20/10; n 2.154; ±2; BR-08535/2026 **[li]**; Globo | `https://www.correio24horas.com.br/eleicoes/quaest-flavio-bolsonaro-tem-45-e-lula-44-no-segundo-turno-1026`; `https://www.dgabc.com.br/Noticia/4353964/quaest-48-dos-eleitores-de-augusto-cury-migram-para-lula-e-33-para-flavio` | CONFIRMADO (totais). Válido 50,56 = 45/89 **deduzido pelo documento**; Quaest não publicou válidos em 21/10 (não achado) |
| Gerp 21/10: 53 | 53 x 47 válidos; totais 50 x 45; campo 19-21/10; n 2.400 (telefone); ±2; BR-03835/2026; recursos próprios | `https://www.poder360.com.br/poder-eleicoes-2026/flavio-tem-53-dos-votos-validos-contra-47-de-lula-diz-gerp/` | CONFIRMADO |
| PoderData/Aya 19/10: 52 | 52 x 48 válidos; totais 49 x 46; campo 16-18/10; n 3.000; ±1,8; BR-02586/2026; contratante não informado. O 53x47 do Correio da Manhã é **outra rodada** (5-7/10, totais 49x44) | `https://sbtnews.sbt.com.br/noticia/eleicoes/poder-data-aya-flavio-tem-52-e-lula-48-no-segundo-turno` | CONFIRMADO |
| AtlasIntel 19/10: 51,1 | 51,1 x 48,9 **válidos**; totais 49,8 x 47,6; campo 13-18/10; n 4.998 (internet); ±1; BR-02418/2026; Bloomberg. Cuidado: em 9/10 o **total** de Flávio também foi 51,1 | `https://investnews.com.br/?p=882811` | CONFIRMADO |
| Futura 16/10: 50,8 | 50,8 x 49,2 válidos; totais 49,0 x 47,5; campo 14-15/10; n 2.000 CATI; ±2,2; BR-03764/2026; recursos próprios (só busca, PDF não confirma). **Existem rodadas posteriores:** 19/10 (50,4) e 21/10 (51,1; BR-06614/2026) | PDF `https://static.poder360.com.br/uploads/2026/10/Relatorio_BR_Out_2_V2_ComTexto_Final.pdf` | CONFIRMADO o valor, **DIVERGE** do uso como "rodada mais recente" |
| Datafolha 20-22/10, n 2.154 ou 2.520? | **n = 2.520** **[li]** (CNN: "ouviu 2.520 pessoas, entre os dias 20 e 22 de outubro", BR-09709/2026, Folha+Globo, ±2). O 2.154 do Metrópoles é o n da **Quaest** (17-20/10). Valores: **válidos 50 x 50**; totais 47 x 46 (brancos/nulos 5, indecisos 2, Terra) | `https://www.cnnbrasil.com.br/eleicoes/datafolha-flavio-e-lula-empatam-em-50-de-votos-validos-no-2o-turno/` **[li]** | DIVERGE (n=2.154 está errado; é 2.520). A nota de "inconsistência de fonte" do documento se resolve |
| Datafolha válido 50,54 (código `"Datafolha": 50.54`) | O instituto divulgou 50 x 50. 50,54 = 47/(47+46), calculado sobre totais já arredondados; só o Metrópoles (resumo de WebFetch, HTML vazio no curl) o traz | idem + Metrópoles `https://www.metropoles.com/brasil/datafolha-flavio-bolsonaro-lula-22-10` **[fetch]** | DIVERGE (rotular como deduzido ou usar 50,0) |
| RTBD 20/10: 52 | 52 x 48 válidos; totais 48 x 45 (só resumo); campo 15-19/10; n 2.000; ±2; BR-02952/2026 (CNN). Há outra rodada divulgada 23/10 (campo 19-22/10, BR-09670/2026), também 52 x 48 | `https://www.correio24horas.com.br/eleicoes/flavio-tem-52-dos-votos-validos-e-lula-48-aponta-real-time-big-data-1026` (paywall) | CONFIRMADO |
| "Rodada mais recente de cada instituto, 07 a 22/10"; "Palver, Nexus, MDA e França sem rodada recente" | **Registro TSE mostra rodadas mais novas que as usadas:** PoderData 22/10 (51 x 49, lida; BR-07926); Futura 19/10 (BR-06715), 21/10 (51,1; BR-06614); BTG/Nexus 13/10 (BR-07997; 52 x 48, lida) e 19/10 (BR-04499; valor 50,3 x 49,7 visto em busca, não confirmado); Palver 15/10 (BR-08028) e 21/10 (BR-04612), valores não coletados; MDA 16/10 (BR-00652), valor não coletado; RTBD 23/10 (BR-09670, 52 x 48); Vox (23/10, BR-03259; CNN: Lula 50,6) e Alfa (20/10 e 23/10; CNN: Flávio 52); Veritá 23/10 (BR-06070, após o corte); Datafolha 22/10 é a mais nova. Nexus 13/10 lida: `https://tribunadejundiai.com.br/politica/eleicoes-2026/pesquisa-btg-nexus-flavio-bolsonaro-lula-segundo-turno/` **[li]** | registros: dado aberto TSE **[li]**; CNN: `https://www.cnnbrasil.com.br/eleicoes/vox-lula-tem-506-dos-votos-validos-no-2o-turno-flavio-494/` | DIVERGE (corpus defasado; as médias 51,34/50,95 precisam ser refeitas) |

## Item 6. Séries de tendência

| Série no documento | Valores achados (Flávio, válidos) | Fonte (URL) | Veredito |
| --- | --- | --- | --- |
| Datafolha 52 -> 51 -> 50,5 | 52 (08/10) -> 51 (15/10; totais 47x45) -> **50** (22/10). O 50,5 é deduzido (47/93 = 50,54), não publicado | CNN `https://www.cnnbrasil.com.br/eleicoes/datafolha-flavio-e-lula-empatam-em-50-de-votos-validos-no-2o-turno/` **[li]**; 08/10 e 15/10 **[sub]** | CONFIRMADO o sentido; DIVERGE o valor final (50, não 50,5) |
| AtlasIntel 52,8 -> 51,1 | 52,8 (09/10, campo 3-8/10, n 5.026, BR-03663/2026) -> 51,1 (19/10) | `https://euqueroinvestir.com/economia/eleicoes-2026-flavio-bolsonaro-tem-511-no-2o-turno-aponta-atlas-bloomberg` **[fetch]**; InvestNews acima | CONFIRMADO |
| Quaest 51 -> 50,6 | 51 (14/10, publicado; totais 46x44, campo 10-13/10, BR-08729/2026) -> 50,56 (21/10, **deduzido** de 45/89; 14/10 pelo mesmo cálculo daria 51,1) | Bloomberg Línea **[fetch]**; dgabc **[li]** | CONFIRMADO o sentido; métodos misturados (51 publicado, 50,6 calculado) |
| Veritá 51,1 -> 50,7 | 51,1 (divulgada 17/10, campo 12-16/10, BR-01107/2026; Bahia Notícias 51,07 x 48,93) -> 50,7 (21/10) | `https://www.bahianoticias.com.br/noticia/322563-pesquisa-verita-aponta-flavio-vencendo-com-511-e-lula-ficando-em-489-na-simulacao-de-segundo-turno` **[fetch]** | CONFIRMADO |
| Gerp 52 -> 53 (exceção) | 55 (13/10, campo 8-12/10, n 2.400, totais 53x44) -> 52 (16/10, campo 14-16/10, BR-05187/2026) -> 53 (21/10). O 52->53 está certo, mas **omite a rodada de 13/10 (55)**: a série é queda forte e depois alta leve | `https://comprerural.com/gerp-flavio-bolsonaro-tem-55-dos-votos-validos-contra-45-de-lula/`; `https://midiamax.com.br/brasil/2026/flavio-tem-52-votos-validos-2o-turno-lula-48-aponta-gerp/` **[sub]** | DIVERGE (série incompleta; "exceção" fica mais fraca) |
| PoderData (não citada no documento) | Válidos de Flávio: 53 (08/10, campo 5-7/10) -> 51 (13/10) -> 50 (16/10) -> 52 (19/10, campo 16-18/10) -> **51 (22/10, campo 19-21/10, n 4.000, ±1,6, BR-07926/2026)**. Manchetes do índice PoderData **[li]**; 22/10 lida na matéria. Série não monotônica; e a rodada mais recente é 51, não 52 | `https://www.poder360.com.br/poderdata/flavio-tem-51-e-lula-tem-49-dos-votos-validos-diz-poderdata-aya/` **[li]**; índice `https://www.poder360.com.br/poderdata/` | DIVERGE: o documento usa 52 (19/10) como "mais recente" |
| Veritá 51,56 (A Crítica) | Uma rodada Veritá de 2º turno com 51,56 x 48,44 aparece em `https://acritica.net/eleicoes-2026/pesquisa-verita-da-5156-a-flavio-bolsonaro-e-4844-a-lula-no-2o-turno/`: data não confirmada, anterior a 17/10; não posicionada na série | A Crítica **[fetch]** | NÃO POSICIONADA (ficar fora da série até datar) |

## Item 7. Financiamento (Veritá e Gerp "com recursos próprios")

Fonte primária **[li, TSE]**: dado aberto `pesquisa_eleitoral_2026.zip` (campo `ST_PESQUISA_PROPRIA`, `VR_PESQUISA`) e `pesquisa_pagante_2026.zip` (`NM_PAGANTE`). `ST_PESQUISA_PROPRIA`=S significa pesquisa própria; o custo declarado (`VR_PESQUISA`) é o custo da pesquisa, não um pagamento de terceiro. `DS_ORIGEM_RECURSO` vem "#NULO#" em todas.

| Afirmação | Achado no registro TSE | Fonte | Veredito |
| --- | --- | --- | --- |
| Veritá com recursos próprios | Nacionais: BR-04522/2026 (1º turno final, 26/9-2/10, n 40.500): S, pagante Instituto Veritá, R$ 200.000; BR-01107/2026 (12-16/10), BR-06396/2026 (15-19/10, n 15.554), BR-06070/2026 (18-22/10): S, pagante Instituto Veritá, R$ 435.512. **Mas** a rodada anterior de 20-25/9 (BR-04467/2026, n 40.500, R$ 1.000.000,08) e os registros estaduais de 21-25/9 constam como NÃO própria, pagante Sistema de Comunicação Pantanal / Rede Brasil de Televisão (BR-00467/2026 idem) | dado aberto TSE (URLs na seção final) | CONFIRMADO para as rodadas citadas (1º turno final e 2º turno); ressalva: a Veritá teve contratante (Rede Brasil de Televisão) na rodada de 20-25/9 |
| Gerp com recursos próprios | Todos os registros nacionais (n 2.400): S, pagante Gerp Mercadologia Ltda; BR-00509/2026 (30/9-2/10) e BR-08168/2026 (1-3/10): R$ 20.000; BR-07877/2026 (8-12/10) e BR-05187/2026 (14-16/10): R$ 10.000; BR-03835/2026 (17-20/10; divulgação 21/10) e BR-09327/2026: R$ 15.000 | dado aberto TSE | CONFIRMADO |
| "Isso diferencia Veritá e Gerp" (implícito) | **Não diferencia.** Também S, pagante o próprio instituto: AtlasIntel (R$ 75.000), PoderData (R$ 103.715), Real Time Big Data (R$ 20-30 mil), Palver (R$ 30.000), Instituto França (R$ 80.000), DataTrends, Vox, Alfa. Contratadas por terceiros (N): Datafolha (Folha + Globo), Quaest (Globo/Editora Globo), MDA (CNT), Nexus (BTG), Futura (pagante Futura Consultoria e Assessoria, não "própria"). Ou seja, os institutos que mais e menos acertaram aparecem nos dois grupos (Veritá/Gerp/Atlas/PoderData vs RTBD/França, todos próprios; Quaest/Datafolha/Nexus contratados) | idem | Ressalva forte: o argumento de "diferença de incentivos" precisa ser reformulado ou cortado |

## Divergências que o documento deve corrigir (resumo)

1. Datafolha 2º turno: n = 2.520 (não 2.154); valor divulgado 50 x 50 (50,54 e 50,5 são deduzidos).
2. Ranking Times: base é válidos, mas com procedência mista (publicado x deduzido pelo Times); Datafolha 42/45 e Nexus não são totais. D da RTBD (16,4) não reproduz (12,0); D da Gerp 03/10 vira 4,8 com os válidos publicados.
3. "Viés pró-Lula": os dados mostram viés contra Flávio; Lula foi subestimado em só 6 de 16 pesquisas.
4. Corpus do 2º turno não é "a mais recente de cada instituto" (conferido no registro TSE): PoderData tem 22/10 (51 x 49, não 52); Futura 21/10 (51,1); Nexus 13/10 (52 x 48) e 19/10; Palver 15/10 e 21/10; MDA 16/10; RTBD 23/10; Vox e Alfa existem. O documento diz que Palver/Nexus/MDA não tinham rodada: falso.
5. Gerp: série tem 55 -> 52 -> 53 (omite 13/10).
6. Transferência: PoderData dá Cury 56/27, Renan 48/25, Caiado 57/19; com essas taxas Flávio sai com ~52,1% (vs 51,47%). Declarar na sensibilidade.
7. Veritá do 1º turno (a "estrela" do ranking): registro identificado no TSE (BR-04522/2026, n 40.500, 26/9-2/10) mas sem relatório com decimais; os decimais 47,0/45,2 só no Times. O BR-01234/2026 citado por uma matéria não existe.
8. Financiamento: "recursos próprios" é o padrão (Atlas, PoderData, RTBD, Palver, França, DataTrends também); não separa Veritá/Gerp. Veritá teve contratante (Rede Brasil de Televisão) na rodada 20-25/9.
9. Fontes secundárias: trocar por TSE (`.../ele2026/6257/dados/br/br-c0001-e006257-u.json`) no item 1.

## Becos

- PesqEle (home, `listar.xhtml`, `/api/pesquisa/BR-xxxxx/2026`): 403 Akamai (três agentes e eu). Contornado só pelo dado aberto do TSE (CKAN `dadosabertos.tse.jus.br`, pacote `pesquisas-eleitorais-2026`), que cobre registro, campo, n, custo e pagante, mas **não** os resultados da pesquisa.
- TSE `dados-simplificados/.../-r.json`, `-w.json`, `-v.json` (2026 e 2022): 404; `config/ele-c.json` por eleição: 404. Funcionou: `comum/config/ele-c.json` e `dados/br/...-u.json`.
- Times Brasil via WebFetch: o resumidor recusou reproduzir o artigo e omitiu linhas; só o HTML bruto por `curl` (texto extraído em scratchpad) serviu para a leitura integral.
- Revista Oeste, Diário do Litoral: 403. Metrópoles: HTML vazio. Correio 24 Horas: paywall.
- DataTrends: nenhuma publicação com resultados achada (o TSE lista várias registradas, n 1.200, todas própria=S; qual é a do Times, não resolvido). Veritá 1º turno: relatório com decimais não achado. Palver 21/10, Nexus 19/10, MDA 16/10: valores não coletados (cota de busca).
- Cota de WebSearch esgotou antes de confirmar Futura 21/10, Nexus >13/10, Vox e Alfa.

## Registro TSE (dados abertos): conferência número a número

Fonte **[li]**: `https://cdn.tse.jus.br/estatistica/sead/odsele/pesquisa_eleitoral/pesquisa_eleitoral_2026.zip`, `https://cdn.tse.jus.br/estatistica/sead/odsele/pesquisa_eleitoral/pesquisa_pagante_2026.zip`, `https://cdn.tse.jus.br/estatistica/sead/odsele/pesquisa_eleitoral/pesquisa_contratante_2026.zip` (listados em `https://dadosabertos.tse.jus.br/api/3/action/package_show?id=pesquisas-eleitorais-2026`; gerados em 23/10/2026 05:46). Todos os registros abaixo EXISTEM com o cargo Presidente e a empresa esperada.

| Rodada | Registro | Campo (TSE) | n (TSE) | Própria? | Observação sobre divergência com matérias/relatórios |
| --- | --- | --- | --- | --- | --- |
| Datafolha 03/10 | BR-01708/2026 | 3/10 | 4.006 | N (Globo+Folha) | confere |
| Datafolha 01/10 | BR-08039/2026 | 28/9-1/10 | 2.506 | N | campo TSE 28/9-1/10 (Folha disse 29/9-1/10) |
| Quaest 03/10 / 28/09 | BR-02197/2026 / BR-06520/2026 | 2-3/10 / 24-27/9 | 3.702 / 2.004 | N (Globo) | confere |
| AtlasIntel 03/10 / 29/09 | BR-00999/2026 / BR-04391/2026 | 27/9-2/10 / 23-28/9 | **5.000** | S | registrado 5.000; relatórios dão 4.945 e 5.005 (efetivo) |
| Gerp 03/10 | BR-00509/2026 **ou** BR-08168/2026 | 30/9-2/10 ou 1-3/10 | 2.400 | S | **dois registros Gerp no mesmo período; o relatório lido pelo subagente diz 30/9-2/10 (BR-00509), o Times diz "3 de outubro"**. DT_DIVULGACAO do BR-00509 consta 29/9 (inconsistente) |
| Gerp 29/09 | BR-03929/2026 | 23-26/9 | 2.400 | S | matéria dizia 24-28/9 |
| PoderData 1T | BR-03519/2026 | 30/9-2/10 | 4.000 | S | confere |
| MDA 1T | BR-04756/2026 | 29/9-2/10 | **2.002** | N (CNT) | CNN 2.002 correto; PDF 2.007 era erro do subagente/relatório |
| RTBD 1T | BR-09503/2026 | 26-30/9 | 2.000 | S | confere |
| Palver 1T | BR-00198/2026 | 30/9-3/10 | 5.000 | S | confere |
| Futura 1T | BR-02431/2026 | 29/9-3/10 | 2.000 | N | campo 29/9-3/10 (relatório dizia 2-3/10) |
| Nexus 1T | BR-07557/2026 | 25-27/9 | 2.000 | N (BTG) | confere |
| França 1T | BR-02928/2026 | 28/9-2/10 | 2.000 | S | confere |
| Veritá 1T final | BR-04522/2026 | 26/9-2/10 | 40.500 | S | identificação por n e campo (A Crítica: "26/9-2/10, 40.500"); o BR-01234/2026 da matéria NÃO existe no TSE |
| DataTrends 1T | candidatos BR-06432, 04252, 04390, 04414, 09795/2026 (n 1.200) | 26-30/9 | 1.200 | S | qual é a do ranking: não resolvido |
| Ipec / Paraná Pesquisas nacional | nenhum | - | - | - | só registros estaduais (Paraná Pesquisas/FIEP-PR); Ipec sem registro de Presidente |
| Veritá 21/10 | BR-06396/2026 | 15-19/10 (divulgação 20/10) | 15.554 | S | matéria "divulgada 21/10" |
| Quaest 21/10 / 14/10 | BR-08535/2026 / BR-08729/2026 | 17-20/10 / 10-13/10 | 2.154 | N (Globo) | confere |
| Gerp 21/10 | BR-03835/2026 | **17-20/10** | 2.400 | S | matérias diziam 19-21/10 |
| PoderData 19/10 / 08/10 / 22/10 | BR-02586 / BR-08134 / BR-07926 (2026) | 16-18/10 / 5-7/10 / 19-21/10 | 3.000 / 3.000 / 4.000 | S | 22/10 (51 x 49) é a mais nova |
| AtlasIntel 19/10 / 09/10 | BR-02418 / BR-03663 (2026) | 13-18/10 / 3-8/10 | 5.000 | S | confere |
| Futura 16/10 / 21/10 | BR-03764 / BR-06614 (2026) | **13-15/10** / 19-20/10 | 2.000 | N | 16/10: relatório dizia 14-15/10 |
| Datafolha 22/10 / 08/10 / 15/10 | BR-09709 / BR-02949 / BR-00466 (2026) | 20-22/10 / 6-8/10 / 13-15/10 | **2.520** | N (Globo+Folha) | n=2.520 confirmado no TSE; campo 08/10 no TSE é 6-8/10 |
| RTBD 20/10 / 23/10 | BR-02952 / BR-09670 (2026) | 15-19/10 / 19-22/10 | 2.000 | S | confere |

> [!NOTE]
> As datas do próprio dado aberto têm inconsistências (ex.: Gerp BR-00509 com divulgação anterior ao campo). Use o número de registro e o n como âncora, e trate datas divergentes entre matéria e TSE como "a conferir no PesqEle com navegador real".
