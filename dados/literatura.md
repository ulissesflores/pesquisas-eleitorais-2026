# Literatura para o artigo de agregação e acurácia de pesquisas eleitorais (Brasil, 2026)

Data da verificação: 2026-10-23. Formato: referência APA 7, DOI/URL, achado em uma linha, status.
Critério: VERIFICADO = autores, ano, periódico, volume, páginas e DOI vistos em Crossref, editora ou SciELO. O achado só cita o que foi lido em resumo ou texto; quando vem de fonte secundária, está dito. NÃO VERIFICADO = o que falta está escrito.
Limites gerais: OUP, Nature, Cambridge e repositórios de Southampton/NCRM bloquearam leitura automatizada (HTTP 401/403/429), então muitos textos completos não foram lidos; os resumos vieram de Crossref, OpenAlex e PubMed. A API do Semantic Scholar devolveu 429.

## 0. Respostas diretas

- **A métrica "erro na margem" é a medida 5 de Mosteller?** Sim. Medida 5 = diferença entre a margem líder-segundo na pesquisa e a margem no resultado: (P_A - V_A) - (P_B - V_B). Duas fontes concordam na numeração: Martin, Traugott & Kennedy (versão JSM 2003, que cita Mosteller 1949, p. 55) e Kline & Stout (2009, Tabela 1).
- **Medida 3** = média do desvio absoluto, sem sinal, entre todos os candidatos/partidos: soma de |P_i - V_i| dividida por n. Em disputa de dois candidatos sem indecisos, a medida 3 vale metade da medida 5.
- Ressalvas: Mosteller (1949) deu descrições verbais, não fórmulas; as fórmulas são reconstruções de Kline & Stout. O livro de 1949 não foi lido (só empréstimo no Internet Archive). As medidas 1, 2, 4 e 6 dependem de uma fonte (Kline & Stout); o texto da medida 4 saiu corrompido na extração. Medidas 3, 5, 7 e 8 estão verificadas.
- **Erro total e margem de erro (Shirani-Mehr et al. 2018):** o resumo diz RMSE de cerca de 3,5 p.p., "about twice as large" quanto o implícito nas margens de erro reportadas. O "2x" é em relação à margem implícita, não uma lei exata.
- **Acurácia passada prevê acurácia futura?** Evidência direta fraca e quase toda interna da FiveThirtyEight (seção 3). Não achei estudo acadêmico independente que teste persistência por instituto; no Brasil, só um white paper (Itaú, 2018) dizendo que não achou instituto consistentemente superior em 1994-2014.

## 1. Acurácia de pesquisas: medidas

### 1.1 Mosteller et al. (1949)
- Mosteller, F., Hyman, H., McCarthy, P. J., Marks, E. S., & Truman, D. B. (1949). *The pre-election polls of 1948: Report to the Committee on Analysis of Pre-Election Polls and Forecasts* (Bulletin 60). Social Science Research Council.
- ABNT: MOSTELLER, F. et al. **The pre-election polls of 1948**. New York: Social Science Research Council, 1949. (Bulletin 60).
- Sem DOI. Registro: https://openlibrary.org/works/OL1248543W
- Achado: primeiro conjunto sistemático de medidas de acurácia, criado após o fracasso de 1948 (8 medidas; ver seção 0).
- Status: VERIFICADO a referência (Open Library, resenhas no Crossref, bibliografia de Martin et al. e Arzheimer & Evans). O texto do relatório NÃO foi lido; o número de páginas diverge entre fontes (391 e 396).

Tabela das medidas (Kline & Stout 2009, Tabela 1; P = pesquisa, V = voto, A e B = dois primeiros):

| # | Definição | Status |
|---|---|---|
| 1 | P_A - V_A | NÃO VERIFICADO em segunda fonte |
| 2 | P_A/(P_A+P_B) - V_A/(V_A+V_B) | NÃO VERIFICADO em segunda fonte |
| 3 | média de abs(P_i - V_i) sobre os n candidatos | VERIFICADO (duas fontes) |
| 4 | média do erro relativo abs(1 - P_i/V_i) (leitura aproximada) | NÃO VERIFICADO (texto corrompido) |
| 5 | (P_A - V_A) - (P_B - V_B), erro na margem | VERIFICADO (duas fontes) |
| 6 | maior abs(P_i - V_i) | NÃO VERIFICADO em segunda fonte |
| 7 | qui-quadrado de aderência | VERIFICADO (descrição) |
| 8 | acerto do voto no colégio eleitoral (EUA) | VERIFICADO (descrição) |

- Kline, R., & Stout, C. (2009). *Measuring polling bias in 2008: The Bradley effect and related issues* [working paper]. UC Irvine, Center for the Study of Democracy. https://www.democracy.uci.edu/files/docs/conferences/grad/Kline-Stout_CSDconf_4-27-09.pdf. VERIFICADO (texto lido). Trabalho não revisado por pares.
- Martin, E. A., Traugott, M. W., & Kennedy, C. (2003). *A review and proposal for a new measure of poll accuracy* [Proceedings of the JSM, Survey Research Methods Section]. http://www.asasrms.org/Proceedings/y2003/Files/JSM2003-000913.pdf. VERIFICADO (texto lido; é a versão preliminar do artigo de 2005).

### 1.2 Martin, Traugott & Kennedy (2005), medida A
- Martin, E. A., Traugott, M. W., & Kennedy, C. (2005). A review and proposal for a new measure of poll accuracy. *Public Opinion Quarterly, 69*(3), 342-369. https://doi.org/10.1093/poq/nfi044
- Achado: propõe A = ln[(r/d)/(R/D)], log da razão de chances entre a pesquisa (r/d) e o resultado (R/D); A = 0 é concordância perfeita; sinal indica o viés; comparável entre eleições com resultados e indecisos diferentes. Var(A) = 1/(n·r·d).
- Status: VERIFICADO (metadados Crossref e página da OUP, que lista os três autores; Crossref lista só "E. A. Martin"). O PDF final do POQ não foi lido; a fórmula veio da versão JSM 2003 e de Arzheimer & Evans. Conferir a equação no PDF final antes de citar página.

### 1.3 Arzheimer & Evans (2014), medidas B e B_w
- Arzheimer, K., & Evans, J. (2014). A new multinomial accuracy measure for polling bias. *Political Analysis, 22*(1), 31-44. https://doi.org/10.1093/pan/mpt012
- Achado: generaliza A para multipartidário: A'_i = ln{[p_i/(1-p_i)]/[v_i/(1-v_i)]}; B = média de |A'_i|; B_w pondera pelo peso do partido no voto, para que partido minúsculo não infle o erro. Aplicado à eleição presidencial francesa de 2012. Relevante para o Brasil (muitos candidatos no 1º turno).
- Status: VERIFICADO (Crossref + texto de autor). A fórmula exata de B_w NÃO foi lida; "soma de v_i·|A'_i|" é inferência. Implementação: Stata Journal 16(1):139-158 (2016), https://doi.org/10.1177/1536867x1601600113 (não aberto).

### 1.4 Shirani-Mehr, Rothschild, Goel & Gelman (2018)
- Shirani-Mehr, H., Rothschild, D., Goel, S., & Gelman, A. (2018). Disentangling bias and variance in election polls. *Journal of the American Statistical Association, 113*(522), 607-614. https://doi.org/10.1080/01621459.2018.1448823
- Achado: 4.221 pesquisas de 608 eleições estaduais dos EUA (1998-2014): RMSE de cerca de 3,5 p.p., aproximadamente o dobro do implícito nas margens de erro reportadas; viés absoluto médio por eleição de cerca de 2 p.p.
- Status: VERIFICADO (Crossref + resumo via OpenAlex).

### 1.5 Brier (1950)
- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review, 78*(1), 1-3. https://doi.org/10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2
- Achado: escore de Brier, erro quadrático médio das probabilidades previstas contra o desfecho 0/1.
- Status: VERIFICADO a referência (Crossref). O achado é conhecimento geral; o texto de 1950 NÃO foi lido.

### 1.6 Groves & Lyberg (2010)
- Groves, R. M., & Lyberg, L. (2010). Total survey error: Past, present, and future. *Public Opinion Quarterly, 74*(5), 849-879. https://doi.org/10.1093/poq/nfq065
- Achado: o erro total de pesquisa é o arcabouço que organiza as fontes de erro de survey, e poucos levantamentos estimam todos os componentes.
- Status: VERIFICADO (Crossref + resumo via OpenAlex).

## 2. Erros de pesquisas no tempo e no espaço; avaliações pós-eleição

- Jennings, W., & Wlezien, C. (2018). Election polling errors across time and space. *Nature Human Behaviour, 2*(4), 276-283. https://doi.org/10.1038/s41562-018-0315-6
  Achado: mais de 30 mil pesquisas de 351 eleições gerais em 45 países (1942-2017); o desempenho recente não é anormal e varia com o contexto. Há errata (https://doi.org/10.1038/s41562-020-0914-x), não conferida contra os números citados. Status: VERIFICADO (Crossref + PubMed; texto não lido).
- Kennedy, C., Blumenthal, M., Clement, S., Clinton, J. D., Durand, C., Franklin, C., McGeeney, K., Miringoff, L., Olson, K., Rivers, D., Saad, L., Witt, G. E., & Wlezien, C. (2018). An evaluation of the 2016 election polls in the United States. *Public Opinion Quarterly, 82*(1), 1-33. https://doi.org/10.1093/poq/nfx047
  Achado: causas mais bem apoiadas: virada tardia e falha em ajustar pela sobrerrepresentação de graduados; pouca evidência de "Shy Trump". Status: VERIFICADO (Crossref + resumo; texto não lido).
- Sturgis, P., Kuha, J., Baker, N., Callegaro, M., Fisher, S., Green, J., Jennings, W., Lauderdale, B. E., & Smith, P. (2018). An assessment of the causes of the errors in the 2015 UK general election opinion polls. *Journal of the Royal Statistical Society: Series A, 181*(3), 757-781. https://doi.org/10.1111/rssa.12329
  Achado: erro principal por amostras não representativas (quota sampling). Status: VERIFICADO (Crossref; o título no registro tem o erro de grafia "Gseneral").
- Sturgis, P., Baker, N., Callegaro, M., Fisher, S., Green, J., Jennings, W., Kuha, J., Lauderdale, B. E., & Smith, P. (2016). *Report of the Inquiry into the 2015 British general election opinion polls*. Market Research Society; British Polling Council. https://eprints.ncrm.ac.uk/id/eprint/3789/1/Report_final_revised.pdf
  Status: NÃO VERIFICADO em editora. Autores e ano vistos no OpenAlex; editoras vistas em busca web; o PDF bloqueou (401/403), a URL oficial da British Polling Council não foi conferida e o conteúdo não foi lido.
- Prosser, C., & Mellon, J. (2018). The twilight of the polls? A review of trends in polling accuracy and the causes of polling misses. *Government and Opposition, 53*(4), 757-790. https://doi.org/10.1017/gov.2018.7
  Achado: erros de pesquisa constantes no tempo e acima do que as margens de erro implicam. Status: VERIFICADO (Crossref + resumo).
- Panagopoulos, C., Endres, K., & Weinschenk, A. C. (2018). Preelection poll accuracy and bias in the 2016 U.S. general elections. *Journal of Elections, Public Opinion and Parties, 28*(2), 157-172. https://doi.org/10.1080/17457289.2018.1441850
  Achado: pesquisas subestimaram os Republicanos, mas os vieses geralmente não foram significativos. Status: VERIFICADO (Crossref + resumo).
- DeSart, J., & Holbrook, T. (2003). Campaigns, polls, and the states: Assessing the accuracy of statewide presidential trial-heat polls. *Political Research Quarterly, 56*(4), 431-439. https://doi.org/10.1177/106591290305600405
  Achado: amostra maior e filtro de eleitor provável melhoram a acurácia; a distância até a eleição pesa. Status: VERIFICADO (Crossref).

## 3. Agregação e modelos probabilísticos

- Jackman, S. (2005). Pooling the polls over an election campaign. *Australian Journal of Political Science, 40*(4), 499-517. https://doi.org/10.1080/10361140500302472
  Achado: modelo de agregação que estima o "house effect" de cada instituto; em 2004 (Austrália) alguns institutos tinham viés grande e significativo. Uma eleição só: não testa persistência. Status: VERIFICADO (Crossref + resumo).
- Linzer, D. A. (2013). Dynamic Bayesian forecasting of presidential elections in the states. *Journal of the American Statistical Association, 108*(501), 124-134. https://doi.org/10.1080/01621459.2012.737735
  Achado: modelo bayesiano dinâmico hierárquico que combina previsão de base com pesquisas estaduais e produz probabilidade de vitória. Status: VERIFICADO (Crossref + resumo).
- Heidemanns, M., Gelman, A., & Morris, G. E. (2020). An updated dynamic Bayesian forecasting model for the US presidential election. *Harvard Data Science Review, 2*(4). https://doi.org/10.1162/99608f92.fc62f1e1
  Achado: atualiza o modelo em Stan, ajusta viés diferencial de não resposta e garante consistência entre previsão estadual e nacional. Status: VERIFICADO (Crossref + resumo).
- Gelman, A., Hullman, J., Wlezien, C., & Morris, G. E. (2020). Information, incentives, and goals in election forecasts. *Judgment and Decision Making, 15*(5), 863-880. https://doi.org/10.1017/S1930297500007981
  Achado: como incentivos moldam a incerteza nas previsões eleitorais e a dificuldade de avaliar calibração. Status: VERIFICADO a referência (Crossref + resumo); o artigo NÃO foi lido além do resumo.
- Pasek, J. (2015). Predicting elections: Considering tools to pool the polls. *Public Opinion Quarterly, 79*(2), 594-619. https://doi.org/10.1093/poq/nfu060
  Achado: compara agregação simples, modelos preditivos e híbridos em 2012. Status: VERIFICADO (Crossref + resumo).
- Clinton, J. D., & Rogers, S. (2013). Robo-polls: Taking cues from traditional sources? *PS: Political Science & Politics, 46*(2), 333-337. https://doi.org/10.1017/S1049096513000012
  Achado: indício de que institutos "pegam dicas" uns dos outros (herding); pesquisas não são independentes. Status: VERIFICADO (Crossref + resumo).
- Pickup, M., & Johnston, R. (2008). Campaign trial heats as election forecasts: Measurement error and bias in 2004 presidential campaign polls. *International Journal of Forecasting, 24*(2), 272-284. https://doi.org/10.1016/j.ijforecast.2008.02.007
  Status: VERIFICADO nos metadados (Crossref); achado NÃO LIDO (sem resumo acessível).
- Graefe, A. (2018). Predicting elections: Experts, polls, and fundamentals. *Judgment and Decision Making, 13*(4), 334-344. https://doi.org/10.1017/s1930297500009219
  Achado: a média de pesquisas supera o especialista típico; afirma que a acurácia passada de um método não é bom indicador da futura. Status: VERIFICADO (PDF lido). Os dois estudos que ele cita para a relação negativa NÃO foram abertos.

## 4. Ranking de institutos, house effects e persistência

- Silver, N. (2014, 25 de setembro). *How FiveThirtyEight calculates pollster ratings*. FiveThirtyEight. URL original: https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/ (hoje redireciona para abcnews.com). Lido nos arquivos: https://web.archive.org/web/20150104112804/http://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings
  Achado: correlação de cerca de 0,6 entre o desempenho dos mesmos 28 institutos antes e depois de 2008; o melhor instituto é cerca de 1 p.p. mais acurado que a média (erro médio de 5,3 p.p.); histórico "reflete mais ruído que sinal" até cerca de 30 pesquisas; "Mean-Reverted Advanced Plus-Minus" soma o equivalente a 30 pesquisas médias (shrinkage); define house effect (vs. outras pesquisas), distinto de viés (vs. resultado), e herding. Status: VERIFICADO (texto integral lido em dois snapshots).
- Rakich, N. (2023, atualizado em 10 de março). *How our pollster ratings work*. FiveThirtyEight. https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/ (lido em https://web.archive.org/web/20240105233432/https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
  Achado: Predictive Plus-Minus = Advanced Plus-Minus revertido a uma média que depende de qualidade metodológica e número de pesquisas; peso por ano 0,93^(ciclo - ano); penalidade por herding. Créditos: pesquisa de Mary Radcliffe, Cooper Burton e Dhrumil Mehta; modelo de Nate Silver. Status: VERIFICADO (texto lido). Observação: a versão de 2023 é do 538, não do Silver Bulletin.
- Silver, N. (2024, 12 de junho; arquivo republicado em 2025). *Silver Bulletin pollster ratings 2024 archive*. https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive e Silver, N., & McKown-Dawson, E. (2026, 14 de janeiro). *Pollster ratings, Silver Bulletin style*. https://www.natesilver.net/p/pollster-ratings-silver-bulletin
  Achado: "restaura" a metodologia do 538 de 2023, sem documento metodológico próprio; tabelas só para firmas com 20 ou mais pesquisas. Status: VERIFICADO (páginas lidas).
- Evidência acadêmica independente sobre persistência por instituto: NÃO ENCONTREI nenhum estudo que teste se acurácia ou viés passado do instituto prediz o futuro. A leitura é: a única evidência direta é interna da 538 (correlação ~0,6, ruído acima de sinal até ~30 pesquisas); Graefe (2018) dá evidência contra persistência para métodos de previsão (não institutos); Shirani-Mehr et al. (2018) e Prosser & Mellon (2018) indicam erro dominado por componente comum a todos os institutos; Clinton & Rogers (2013) indicam herding. INFERÊNCIA: erro compartilhado e herding limitam o ganho de ponderar institutos pelo histórico.

## 5. Literatura brasileira

Aviso de escassez: encontrei pouca literatura revisada por pares sobre o erro das pesquisas de 2018 e 2022. Não achei artigo sobre o tema em RBCP, DADOS, Revista de Sociologia e Política ou RBCS (a busca no SciELO foi bloqueada; usei Crossref por periódico). Também não achei estudo brasileiro sobre persistência por instituto.

### 5.1 Revisados por pares
- Pereira, F. B., & Nunes, F. (2024). Pesquisas eleitorais e mudanças tardias na decisão do voto. *Opinião Pública, 30*, e3011. https://doi.org/10.1590/1807-019120243011
  Achado: único artigo que li centrado no erro do 1º turno presidencial de 2022; testa mudanças tardias de voto (voto estratégico, alinhamento de indecisos) como explicação; não compara institutos sistematicamente. Status: VERIFICADO (SciELO + Crossref). Os números de erro (agregador cerca de 33% vs. cerca de 41,3% para Bolsonaro) vieram de leitura resumida do HTML e o denominador difere dos 43,20% de votos válidos oficiais: conferir no PDF antes de citar.
- Meireles, F., & Russo, G. (2022). Pesquisas eleitorais no Brasil: tendências e desempenho. *Estudos Avançados, 36*(106), 117-131. https://doi.org/10.1590/s0103-4014.2022.36106.007
  Achado: mais de 2 mil pesquisas de 5 eleições (2012 a 2020, bases do Poder360 e Pindograma, registros do TSE); RMSE médio de véspera de cerca de 0,035; em 2018, 0,031 (Poder360) e 0,037 (Pindograma); amostras maiores e proximidade da data reduzem o erro. Status: VERIFICADO (Crossref + texto integral lido). Não cobre 2022 e não compara institutos.
- Gramacho, W. G. (2013). A margem das margens?: a precisão das pesquisas pré-eleitorais brasileiras em 2010. *Opinião Pública, 19*(1), 65-80. https://doi.org/10.1590/s0104-62762013000100004
  Achado: 156 pesquisas de 2010 avaliadas com a medida 3 de Mosteller; erros maiores que as margens informadas, sem condenar a precisão do conjunto. Status: VERIFICADO (Crossref + resumo).
- Kamradt, J. (2017). É possível confiar nas pesquisas eleitorais? Análise das intenções de votos nas eleições para governadores no Brasil em 2014. *Compolítica, 1*(1), 157. https://doi.org/10.21878/compolitica.2017.1.1.224
  Achado: 77 pesquisas de 23 institutos nos 27 estados; 32% das previsões não se realizaram. Periódico menor, só 2014. Status: VERIFICADO (Crossref + resumo).

### 5.2 Preprint e dissertação
- Meireles, F. (2026). *Regulação e transparência das pesquisas eleitorais no Brasil* [preprint]. SocArXiv. https://doi.org/10.31235/osf.io/r9sj2_v1
  Achado: mais de 52 mil pesquisas registradas no TSE (2012-2024); as mais baratas ou autofinanciadas têm menor completude informacional. Não mede erro. Status: VERIFICADO (Crossref + resumo); preprint, sem revisão por pares.
- Almeida, J. F. G. de. (s.d.). *Avaliando empiricamente os determinantes de erro nas pesquisas eleitorais brasileiras para presidente* [dissertação]. PUC-Rio. https://doi.org/10.17771/pucrio.acad.73601
  Status: NÃO VERIFICADO (sem ano e sem resumo no Crossref; texto não lido; não citar sem abrir o PDF).

### 5.3 Literatura cinzenta
- Itaú Asset Management. (2018, maio). *Pesquisas eleitorais no Brasil* [white paper]. https://assetfront.arquivosparceiros.cloud.itau.com.br/ISG/Pesquisas_Eleitorais_no_Brasil_White_Paper.pdf
  Achado: pesquisas presidenciais 1994-2014 (Ibope, Datafolha e outros); não identificou instituto consistentemente superior; desvios muitas vezes maiores que o esperado pelas margens. Evidência brasileira contra persistência, para 1994-2014. Status: VERIFICADO (texto lido); autoria individual e data exata não confirmadas.
- Toledo, M. T. (2022, 5 de outubro). *Onde as pesquisas podem ter errado?* Fundação Perseu Abramo/NOPPE. https://fpabramo.org.br/2022/10/05/onde-as-pesquisas-podem-ter-errado
  Achado: subestimação de Bolsonaro no 1º turno de 2022 em votos válidos: Datafolha 7,2 p.p., Ipec 6,2, Quaest 5,2, AtlasIntel 2,1 (apurado: Bolsonaro 43,20%). Instituição ligada ao PT; texto de análise, não revisado por pares. Status: VERIFICADO (página lida); os números de cada instituto não foram conferidos contra os relatórios originais.
- Magalhães, R. N. (2026). *agregR: Bayesian state-space aggregation of Brazilian presidential polls* (v1.0.4) [pacote R]. CRAN. https://doi.org/10.32614/CRAN.package.agregR
  Achado: agregador bayesiano baseado em Jackman (2009) com ajuste de viés por desempenho passado. Software, sem validação revisada por pares vista. Status: VERIFICADO (página CRAN lida).
- Datafolha (declaração de Luciana Chong, 1º turno 2022, via BNews): https://www.bnews.com.br/noticias/eleicoes-2022/bolsonaro-recebeu-voto-util-na-ultima-hora-diz-datafolha.html. Status: NÃO VERIFICADO (fonte primária do Datafolha não localizada; só resumo de busca).
- Ipec, nota institucional após o 1º turno 2022. Status: NÃO VERIFICADO (só reportagens; nota original não localizada).
- Cade/Ministério da Justiça (inquérito de out/2022 contra institutos); PL 2567/2022; ação da PF e do TSE. Status: NÃO VERIFICADO (só reportagens em resumo de busca).
- Notas da ABEP, ANIP e Abrapel sobre 2022: NÃO VERIFICADO (não localizadas).

## 6. Descartados e becos

- Posts "Introducing FiveThirtyEight pollster ratings" e "Are some pollsters consistently better?": não achei com esses títulos; a pergunta está no corpo do post de 2014 (seção 4).
- Pickup, Stephenson, Scotto, Bruce & Gelman "Why do polls differ? House effects": não achado. "Stoetzel/Jackman 2005": Stoetzel é o pioneiro francês; a referência correta é Jackman (2005).
- Fisher et al. (2011, Electoral Studies, https://doi.org/10.1016/j.electstud.2010.09.005): existe, mas trata de previsão de cadeiras, irrelevante para persistência.
- Figueiredo Filho et al. "Quem acerta mais?" e trabalhos de Zucco/Martins sobre pesquisas: não achados. Silva & Gonçalves (2019, RSP): sobre financiamento, fora de escopo.
- Walther (2015) e o preprint arXiv 2411.01730: metadados existem, conteúdo não lido, sem confirmação de achado sobre persistência.
- Franklin (2003), Durand (2008) e Mitofsky (1998): não consultados diretamente.
- Semantic Scholar API: 429. SciELO search: 403. OUP/Nature/Cambridge/Southampton/NCRM: bloqueio anti-bot.
