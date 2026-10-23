---
titulo: "Quem acerta, quem erra e para que lado: as pesquisas da eleição presidencial de 2026 à luz de 37 anos de erros"
autor: Ulisses Flores
data: 2026-10-23
corte_de_dados: "rodadas de 2º turno divulgadas até 23/10/2026; registro conferido no dado aberto do TSE gerado em 23/10/2026 05:46"
versao: v1 (pré-resultado do 2º turno de 25/10/2026)
---

# Quem acerta, quem erra e para que lado: as pesquisas da eleição presidencial de 2026 à luz de 37 anos de erros

**Ulisses Flores** · 23 de outubro de 2026 · versão escrita antes do 2º turno de 25/10/2026

## Resumo

Com 38 rodadas de 17 institutos registradas no TSE e divulgadas até 23/10/2026, a mediana das pesquisas dá a Flávio Bolsonaro (PL) 51,0% dos votos válidos contra 49,0% de Lula (PT). Calibrando o erro com os seis segundos turnos presidenciais de 2002 a 2022, a probabilidade de vitória de Flávio é de **77%**, numa faixa de 55% a 79% conforme o estimador do centro. O número central é sensível a quem entra na média: os oito institutos com 20 ou mais pesquisas finais em 2012-2022 dão 50,66% (69%), e os quatro que mais erraram abaixo dos rivais dão 50,82% (73%). Avaliamos a acurácia dos institutos em duas bases: as pesquisas finais presidenciais de 1989 a 2026, com campo até 7 dias antes da eleição, e 4.974 pesquisas finais para presidente, governador e prefeito de 2012 a 2022. Quatro resultados. (1) No 1º turno de 2026, as 12 pesquisas finais puseram Flávio abaixo do resultado (10 por mais de 0,5 pp), enquanto o erro em Lula não teve direção; no 1º turno, o candidato de direita ou do PSDB foi subestimado nas seis eleições de 2002 a 2022. (2) Nos segundos turnos, o erro médio é −0,30 pp (erro-padrão 0,54), sem viés detectável, e o tamanho do erro do 1º turno não prevê um erro do mesmo lado no 2º (correlação −0,61, n = 6). (3) A ordem dos institutos se repete pouco entre períodos: 0,06 a 0,38 no erro da margem (nenhum valor significativo) e 0,20 a 0,70 no erro médio por candidato. (4) Há padrões sugestivos, não conclusivos, de erro sistemático na mesma direção: Veritá e Paraná Pesquisas ficaram abaixo dos rivais na fatia do PT em todos os ciclos em que aparecem (5 de 5, p = 0,06; 4 de 4, p = 0,12); a inclinação histórica não previu a de 2026. Todas as previsões estão registradas para o teste contra o resultado de 25/10.

## 1. Pergunta e contribuição

Três perguntas guiam o texto:

1. **Quem acerta e quem erra**, na maior janela de dados disponível, e com que confiança dá para separar habilidade de sorte?
2. **Para que lado** cada instituto erra: existe erro sistemático a favor de um candidato ou campo, e ele se repete de uma eleição para outra?
3. **O que isso implica para o 2º turno de 25/10/2026**: qual é o centro honesto das pesquisas e quanta incerteza ele carrega?

O que este trabalho acrescenta ao que já existe:

- **Base longa e aberta, com linhagens.** Juntamos as pesquisas finais presidenciais de 1989 a 2026 e a base aberta do Pindograma de 2012 a 2022. Institutos que mudaram de nome entram com os dois nomes (Ibope e Ipec; DataPoder360 e PoderData; Atlas Político e AtlasIntel).
- **Teste direto da persistência.** A literatura não traz estudo acadêmico independente que teste se a acurácia passada de um instituto prevê a futura; a evidência disponível é interna à FiveThirtyEight (Silver, 2014) ou indireta (Graefe, 2018; Itaú, 2018). Testamos isso em dados brasileiros, para acurácia e para direção do erro.
- **Calibração do erro do 2º turno com a própria história do 2º turno**, em vez de usar o erro do 1º turno, que é de outra ordem de grandeza.
- **Conformidade e reprodutibilidade.** Toda rodada citada tem registro conferido no dado aberto do TSE, e todo número sai de código publicado.

As medidas de acurácia **não são novas**: usamos as medidas 3 e 5 de Mosteller et al. (1949), nas fórmulas reconstruídas por Kline e Stout (2009), e a medida A de Martin, Traugott e Kennedy (2005). Para disputas com muitos candidatos existe a medida B de Arzheimer e Evans (2014); não a usamos porque comparamos só os dois primeiros. Agregação de pesquisas e modelos probabilísticos têm literatura própria (Jackman, 2005; Linzer, 2013; Gelman et al., 2020); o modelo aqui é deliberadamente simples, calibrado na história brasileira. No Brasil, Gramacho (2013) avaliou as pesquisas de 2010 com a medida 3, e Meireles e Russo (2022) mediram erro quadrático médio de véspera de cerca de 3,5 pp em 2012-2020.

## 2. Dados

**Resultado oficial do 1º turno de 2026 (TSE).** 119.300.788 votos válidos. Flávio 56.104.503 (47,03%), Lula 53.879.538 (45,16%), Augusto Cury 2,89%, Renan Santos 2,24%, Ronaldo Caiado 2,18%, Romeu Zema 0,27%, demais 0,22%. Abstenção de 33.469.244 eleitores (21,08%); brancos 2.300.798; nulos 3.674.249.

**Corpus.**

| Base | Janela | Unidade | Tamanho | Fonte |
| --- | --- | --- | --- | --- |
| 2º turno 2026 | 07/10 a 23/10/2026 | rodada registrada | 39 rodadas de 18 institutos coletadas; 38 de 17 no agregado (Alfa fora, ver 4.6) | reportagens e institutos; registro, campo, entrevistas e contratante pelo dado aberto do TSE |
| 1º turno 2026 | 27/09 a 03/10/2026 | pesquisa final | 16 pesquisas, 12 institutos | ranking do Times Brasil/CNBC conferido contra os institutos |
| Presidencial 1989-2022 | 9 eleições, 2 turnos | última pesquisa de cada instituto | 92 linhas | relatórios e tabelas que citam o TSE |
| Todas as disputas 2012-2022 | 6 eleições | pesquisa final (1º turno até 21 dias; 2º turno até 14 dias) | 4.974 pesquisas, 2.220 disputas | base aberta do Pindograma (GPL-3), junção refeita em Python |

**Regras de comparação.** Tudo em votos válidos. Quando o instituto divulgou só votos totais, o válido é recalculado (candidato dividido pela soma dos dois no 2º turno). Quando divulgou os dois, usamos o recalculado a partir dos totais, que tem mais casas decimais que o válido arredondado. A replicação da base do Pindograma reproduz o erro médio por instituto do ranking publicado com correlação de 0,90 e a contagem de pesquisas por instituto com 0,99, mas cobre cerca de 72% das pesquisas do ranking publicado; a diferença não foi diagnosticada e é declarada como limitação.

## 3. Métodos

**Acurácia de uma pesquisa.** Para candidatos A e B, com p a estimativa e r o resultado, em votos válidos:

```latex
M_3 = \frac{1}{k}\sum_{i=1}^{k}\lvert p_i - r_i\rvert \qquad
M_5 = (p_A - p_B) - (r_A - r_B) \qquad
A = \ln\!\left[\frac{p_A/p_B}{r_A/r_B}\right]
```

M3 e M5 são as medidas 3 e 5 de Mosteller et al. (1949); A é a de Martin, Traugott e Kennedy (2005).

**Acurácia de um instituto.** Para não confundir instituto bom com disputa fácil, o desempenho na base 2012-2022 é **relativo aos rivais na mesma disputa**: o erro da pesquisa menos a média dos outros institutos naquela disputa. A média por instituto é encolhida para a média geral com peso n/(n + 15), como no Pindograma, e por n/(n + 3) na série presidencial, que tem poucas eleições por instituto. O encolhimento existe porque, com poucas pesquisas, sorte pesa mais que habilidade (Silver, 2014).

**Direção do erro.** Erro com sinal na fatia bipartidária do candidato do PT, em toda disputa em que ele está entre os dois primeiros do resultado: positivo é superestimar o PT. Como robustez, o mesmo para um bloco de esquerda (PT, PSOL, PCdoB, PSB, PDT, Rede, PV e partidos menores de esquerda), classificação declarada por nós, com referência a Bolognesi, Ribeiro e Codato (2023), cuja lista partido a partido não foi conferida. Separamos **viés** (contra o resultado) de **efeito de casa** (contra os rivais na mesma disputa), como em Jackman (2005) e Silver (2014). Como as pesquisas de um mesmo ciclo compartilham o erro daquele ciclo, contamos a direção **por pesquisa e por ciclo eleitoral**, e só chamamos de persistente a inclinação que se repete entre ciclos.

**Persistência.** Correlação de postos de Spearman entre o desempenho médio de cada instituto antes e depois de um ano de corte, entre institutos com 5 ou mais pesquisas em cada lado.

**Agregado do 2º turno.** O estimador central é a **mediana da rodada mais recente de cada instituto**. Como sensibilidade, uma regressão com tendência linear comum e efeito fixo de instituto (soma zero), projetada para 25/10 em quatro janelas, com bootstrap por instituto.

**Probabilidade.** A fatia real de Flávio é o centro mais um erro com desvio σ:

```latex
P(\text{Flávio vence}) = F_{t,\nu}\!\left(\frac{\mu + b - 50}{\sigma}\right), \qquad
\sigma = \sqrt{\sigma_{\text{sist}}^2 + \sigma_{\text{centro}}^2}
```

σ_sist é a raiz do erro quadrático médio do agregado (média dos institutos com campo até 7 dias antes) nos segundos turnos presidenciais de 2002 a 2022 (seis eleições; 1989 tem um instituto só e fica de fora). σ_centro é o desvio bootstrap da mediana. F_{t,ν} é a distribuição t de Student com ν = 6 graus de liberdade, que alarga a cauda porque σ foi estimado com seis pontos; reportamos também a normal. b é um ajuste de viés, zero no cenário central.

## 4. Resultados

### 4.1 O 1º turno de 2026: subestimação de Flávio, não superestimação de Lula

Recalculamos a acurácia a partir das estimativas de cada instituto em vez de usar o desvio acumulado do Times Brasil, porque dois valores desse ranking não se reproduzem com os válidos publicados pelos próprios institutos: Real Time Big Data (16,4 publicado, 12,0 recalculado) e Gerp (6,0 publicado, 4,8 recalculado).

**Tabela 1.** **Pesquisa final de cada instituto no 1º turno** (votos válidos; resultado do TSE: Flávio 47,03%, Lula 45,16%). "Erro na margem" é a diferença entre a vantagem de Flávio na pesquisa e nas urnas (+1,87): negativo subestimou Flávio. Ordem: do menor ao maior erro.

| Instituto | Contratante (registro TSE) | Campo | Entrevistas | Margem | Confiança | Registro | Flávio | Lula | Erro na margem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Veritá | Instituto Verita Ltda | 26/09 a 02/10 | 40.500 | ±1 pp | 95% | BR-04522/2026 | 47,0% | 45,2% | −0,1 |
| Gerp | Gerp Mercadologia Ltda | 30/09 a 02/10 | 2.400 | ±2,04 pp | 95,55% | BR-00509/2026 | 46,0% | 44,0% | +0,1 |
| Futura | Futura Consultoria E Assessoria Ltda / Futura | 29/09 a 03/10 | 2.000 | ±2,2 pp | 95% | BR-02431/2026 | 44,8% | 42,6% | +0,3 |
| Palver | Palver Consultoria E Desenvolvimento Tecnologico Ltda. | 30/09 a 03/10 | 5.000 | ±4 pp | 95% | BR-00198/2026 | 47,0% | 43,0% | +2,1 |
| Quaest | Globo Comunicacao E Participacoes S/A / Tv/Rede/Globo.Com/Canais Globo/Globoplay/Eletromidia; Editora Globo S/A / Editora Globo | 02/10 a 03/10 | 3.702 | ±2 pp | 95% | BR-02197/2026 | 45,0% | 46,0% | −2,9 |
| PoderData | Poderdata Pesquisa, Jornalismo E Comunicacao Ltda | 30/09 a 02/10 | 4.000 | ±2 pp | 95% | BR-03519/2026 | 43,0% | 45,0% | −3,9 |
| AtlasIntel | Atlasintel Tecnologia De Dados Ltda | 27/09 a 02/10 | 5.000 | ±1,0 pp | 95% | BR-00999/2026 | 44,1% | 47,0% | −4,8 |
| Datafolha | Empresa Folha Da Manha S.A.; Globo Comunicacao E Participacoes S/A / Tv/Rede/Globo.Com/Canais Globo/Globoplay/Eletromidia | 03/10 a 03/10 | 4.006 | ±2 pp | 95% | BR-01708/2026 | 42,0% | 45,0% | −4,9 |
| Instituto França | Instituto Franca De Pesquisas Ltda | 28/09 a 02/10 | 2.000 | ±2,2 pp | 95% | BR-02928/2026 | 40,5% | 43,9% | −5,3 |
| Nexus | Banco Btg Pactual S.A. | 25/09 a 27/09 | 2.000 | ±2 pp | 95% | BR-07557/2026 | 39,0% | 44,0% | −6,9 |
| Real Time Big Data | Real Time Midia Ltda | 26/09 a 30/09 | 2.000 | ±2 pp | 95% | BR-09503/2026 | 41,0% | 46,0% | −6,9 |
| MDA | Confederacao Nacional Do Transporte | 29/09 a 02/10 | 2.002 | ±2,2 pp | 95% | BR-04756/2026 | 42,1% | 47,8% | −7,6 |

Notas de origem: Gerp e Nexus pelos válidos que os próprios institutos publicaram; Instituto França recalculado dos totais (o instituto não publica válidos); Palver não divulga válidos, e os percentuais são os publicados; os decimais da Veritá vêm da compilação do Times Brasil/CNBC, e o instituto divulgou 47 e 45 inteiros.

**Leitura.** As 12 pesquisas finais puseram Flávio abaixo dos 47,03%, 10 delas por mais de 0,5 pp; Veritá e Palver ficaram a 0,03 pp, dentro do arredondamento (a Palver em percentuais que não são válidos, o que exige cautela). Lula não foi superestimado de forma sistemática: 5 institutos o subestimaram, 4 o superestimaram e 3 acertaram dentro de 0,5 pp. A afirmação correta, portanto, é **"as pesquisas subestimaram Flávio"**, e não "as pesquisas superestimaram Lula". Na fatia bipartidária, o erro médio das 12 pesquisas finais foi de 1,9 pp contra Flávio. As medidas da Tabela 1 usam só Flávio e Lula, para serem comparáveis entre institutos que divulgaram números diferentes de candidatos.

**Timing confunde acurácia.** Rodadas de 28/09 a 01/10 dos mesmos institutos erraram mais que as de 02-03/10. Parte do "erro" é movimento real de última hora para Flávio, coerente com a hipótese de mudança tardia de voto investigada para 2022 por Pereira e Nunes (2024). Nexus (campo até 27/09) e Real Time Big Data (até 30/09) entram com sua pesquisa final, mais antiga que a dos demais: a coluna de campo da Tabela 1 deixa isso visível.

### 4.2 37 anos: o 1º turno erra muito e para o mesmo lado; o 2º turno erra pouco e sem lado

| Eleição | Erro do agregado no 1º turno (pp, candidato de direita/PSDB) | Institutos | Erro do agregado no 2º turno | Institutos |
| --- | --- | --- | --- | --- |
| 1989 | -0,59 | 1 | -1,38 | 1 |
| 1994 | +0,89 | 1 | - | - |
| 1998 | +1,94 | 1 | - | - |
| 2002 | -1,78 | 4 | -2,50 | 4 |
| 2006 | -6,74 | 2 | -0,90 | 3 |
| 2010 | -1,82 | 4 | -0,41 | 4 |
| 2014 | -7,18 | 5 | +1,08 | 6 |
| 2018 | -5,71 | 11 | +0,97 | 8 |
| 2022 | -3,29 | 13 | -0,04 | 13 |

No 1º turno, o candidato de direita ou do PSDB foi subestimado nas seis eleições de 2002 a 2022 (as primeiras com dois ou mais institutos a até 7 dias da eleição), três vezes por mais de 5 pp. Antes de 2002 há um instituto por eleição; em 1994 e 1998, as eleições de Fernando Henrique Cardoso, o erro foi para o outro lado.

**Consequência para 2026.** O cenário "o viés do 1º turno se repete", que no documento-base levava a probabilidade a 93%, **não tem apoio nas seis eleições disponíveis** (aparece na Tabela 7 só para registro).

**Regra de inclusão e sensibilidade.** O agregado usa todos os institutos com campo até 7 dias antes. Com só os cinco de série longa (Datafolha, Ibope/Ipec, Vox Populi, Sensus, MDA), o erro quadrático médio sobe para 1,35 pp; sem Veritá, Sensus, Paraná Pesquisas e Brasmarket, cai para 0,93 pp. A escolha central (1,25) fica no meio.

### 4.3 Quem acerta e quem erra

**Tabela 2a.** Classificação presidencial 1989-2026 por linhagem, 1º turno (erro na fatia de válidos do candidato de direita/PSDB; média geral 4,57 pp; ordem pelo erro encolhido).

| Posição | Linhagem (nomes usados) | Pesquisas finais | Erro absoluto médio | Encolhido | Relativo aos rivais do mesmo ano | Viés médio (+ = pró-direita) | Erraram pró-direita / pró-esquerda | p do sinal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Veritá (Veritá) | 3 | 2,58 | 3,57 | -2,69 | +2,56 | 2 / 0 | 0,50 |
| 2 | Futura (Futura) | 2 | 2,48 | 3,74 | -1,91 | -2,48 | 0 / 2 | 0,50 |
| 3 | Atlas Político->AtlasIntel (AtlasIntel) | 2 | 2,51 | 3,75 | -1,86 | -2,51 | 0 / 2 | 0,50 |
| 4 | Datafolha (Datafolha) | 10 | 3,62 | 3,84 | -0,39 | -3,05 | 2 / 8 | 0,11 |
| 5 | Quaest (Genial/Quaest) (Quaest) | 2 | 3,62 | 4,19 | -0,68 | -3,62 | 0 / 2 | 0,50 |
| 6 | Ibope->Ipec (Ibope, Ipec) | 5 | 4,01 | 4,22 | -0,58 | -4,01 | 0 / 5 | 0,06 |
| 7 | Vox Populi (Vox Populi) | 4 | 4,25 | 4,39 | -0,05 | -4,25 | 0 / 4 | 0,12 |
| 8 | Paraná Pesquisas (Paraná Pesquisas) | 2 | 4,16 | 4,41 | -1,75 | -4,16 | 0 / 2 | 0,50 |
| 9 | MDA (CNT/MDA, MDA (CNT)) | 4 | 4,56 | 4,57 | -1,14 | -4,56 | 0 / 4 | 0,12 |
| 10 | Sensus (CNT/Sensus) | 4 | 5,54 | 5,12 | +2,03 | -5,54 | 0 / 4 | 0,12 |
| 11 | Real Time Big Data (Real Time Big Data) | 2 | 6,03 | 5,16 | +0,98 | -6,03 | 0 / 2 | 0,50 |
| 12 | Ipespe (Ipespe) | 2 | 6,56 | 5,37 | +0,85 | -6,56 | 0 / 2 | 0,50 |
| 13 | DataPoder360->PoderData (DataPoder360, PoderData) | 3 | 7,18 | 5,88 | +2,36 | -7,18 | 0 / 3 | 0,25 |
| 14 | FSB (FSB) | 2 | 8,38 | 6,10 | +2,88 | -8,38 | 0 / 2 | 0,50 |

**Tabela 2b.** Classificação presidencial 1989-2026 por linhagem, 2º turno (erro na fatia de válidos do candidato de direita/PSDB; média geral 1,96 pp; ordem pelo erro encolhido).

| Posição | Linhagem (nomes usados) | Pesquisas finais | Erro absoluto médio | Encolhido | Relativo aos rivais do mesmo ano | Viés médio (+ = pró-direita) | Erraram pró-direita / pró-esquerda | p do sinal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Datafolha (Datafolha) | 7 | 0,93 | 1,24 | -1,18 | -0,75 | 1 / 3 | 0,62 |
| 2 | Ibope->Ipec (Ibope, Ipec) | 6 | 1,16 | 1,43 | -0,91 | -1,16 | 0 / 4 | 0,12 |
| 3 | MDA (CNT/MDA) | 3 | 1,25 | 1,60 | -1,17 | +1,13 | 2 / 0 | 0,50 |
| 4 | Ipespe (Ipespe) | 2 | 2,49 | 2,17 | +0,27 | +0,39 | 1 / 1 | 1,00 |
| 5 | Paraná Pesquisas (Paraná Pesquisas) | 2 | 2,99 | 2,37 | +0,90 | +2,99 | 1 / 0 | 1,00 |
| 6 | Vox Populi (Vox Populi) | 4 | 2,69 | 2,38 | +0,70 | -2,69 | 0 / 4 | 0,12 |
| 7 | Sensus (CNT/Sensus) | 4 | 2,78 | 2,43 | +1,54 | -0,91 | 1 / 3 | 0,62 |
| 8 | Veritá (Veritá) | 2 | 3,36 | 2,52 | +1,50 | +3,36 | 2 / 0 | 0,50 |

**Tabela 3.** Classificação 2012-2022, todas as disputas (presidente, governador, prefeito), institutos com 20 ou mais pesquisas finais. Negativo = errou menos que os rivais na mesma disputa.

| Posição | Instituto | Pesquisas | Disputas | Anos | Erro na margem relativo aos rivais (encolhido) | Erro absoluto na margem | Mosteller 3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Instituto Amostragem | 35 | 23 | 2012-2022 | -2,95 | 7,39 | 3,08 |
| 2 | Futura | 51 | 32 | 2012-2022 | -2,65 | 9,38 | 3,32 |
| 3 | AtlasIntel | 79 | 44 | 2020-2022 | -2,53 | 7,03 | 2,60 |
| 4 | Serpes | 42 | 23 | 2012-2022 | -1,02 | 9,07 | 3,80 |
| 5 | Ipec (antigo Ibope) | 760 | 351 | 2012-2022 | -0,95 | 8,84 | 3,23 |
| 6 | Datafolha | 190 | 62 | 2012-2022 | -0,72 | 9,33 | 3,16 |
| 7 | Ibrape | 23 | 16 | 2012-2022 | -0,63 | 7,55 | 3,46 |
| 8 | Ranking Pesquisa | 47 | 19 | 2016-2022 | -0,52 | 8,09 | 4,47 |
| 9 | MDA | 26 | 17 | 2012-2022 | -0,36 | 9,13 | 3,69 |
| 10 | Paraná Pesquisas | 113 | 76 | 2016-2022 | -0,29 | 8,26 | 3,34 |
| 11 | Escutec | 28 | 23 | 2012-2022 | -0,21 | 12,61 | 5,03 |
| 12 | Real Time Big Data | 153 | 90 | 2018-2022 | +0,11 | 9,49 | 3,92 |
| 13 | Doxa | 25 | 19 | 2012-2022 | +0,11 | 11,35 | 3,90 |
| 14 | Quaest | 30 | 20 | 2016-2022 | +0,19 | 9,73 | 3,43 |
| 15 | Instituto Seta | 25 | 17 | 2014-2022 | +0,23 | 8,95 | 4,39 |
| 16 | Veritá | 93 | 73 | 2012-2022 | +0,88 | 9,89 | 3,99 |
| 17 | Ipespe | 52 | 32 | 2012-2022 | +0,95 | 9,98 | 4,33 |
| 18 | Consult Pesquisa (RN) | 21 | 15 | 2012-2022 | +1,13 | 10,32 | 3,91 |
| 19 | Vox Populi | 45 | 35 | 2012-2020 | +1,43 | 11,81 | 4,34 |

**Leitura.**

- **Os dois turnos ficam em quadros separados** porque a escala é outra: no 1º turno, com muitos candidatos, o erro médio de uma pesquisa final é 4,6 pp; no 2º turno, 2,0 pp. Juntar os dois puniria quem aparece mais no 1º turno. Só entram pesquisas com campo encerrado até 7 dias antes da eleição, a mesma regra da calibração de σ.
- **No 2º turno presidencial, Datafolha, Ibope/Ipec e MDA são os mais precisos** (0,93, 1,16 e 1,25 pp, com 7, 6 e 3 eleições), e também os que mais erraram abaixo dos rivais do mesmo ano. Veritá, Paraná Pesquisas e Sensus têm os maiores erros (2,8 a 3,4 pp), com 2 a 4 eleições cada.
- **No 1º turno presidencial,** Veritá, Futura e AtlasIntel lideram, mas com 2 ou 3 eleições cada; Datafolha e Ibope/Ipec têm 10 e 5 eleições e erram um pouco abaixo da média dos rivais. FSB e DataPoder360/PoderData têm os maiores erros, também contra os rivais do mesmo ano (2,9 e 2,4 pp acima).
- **Na base de todas as disputas (Tabela 3),** entre institutos com 20 ou mais pesquisas, Instituto Amostragem, Futura e AtlasIntel erraram menos que os rivais na mesma disputa, seguidos de Serpes, Ipec/Ibope e Datafolha; Vox Populi, Consult Pesquisa, Ipespe e Veritá erraram mais.
- **As classificações discordam** conforme a medida, o turno e a base, como já notado para os rankings publicados (Pindograma, 2024; Times Brasil/CNBC, 2026). Isso é uma propriedade do problema, não uma falha da conta: uma classificação de institutos depende do critério.

### 4.4 A ordem dos institutos se repete de um período para o outro? Pouco

**Tabela 4.** Acerto antes do corte prevê acerto depois? Correlação de postos entre períodos (institutos com 5 ou mais pesquisas em cada lado).

| Ano de corte | Institutos | Spearman, erro médio por candidato (M3) | Spearman, erro na margem (M5) |
| --- | --- | --- | --- |
| 2016 | 21 | 0,70 | 0,38 |
| 2018 | 26 | 0,47 | 0,19 |
| 2020 | 24 | 0,45 | 0,23 |
| 2022 | 19 | 0,20 | 0,06 |

O teste compara o desempenho médio de cada instituto antes e depois de um ano de corte, juntando turnos e cargos; não é um teste direto de "1º turno prevê 2º turno da mesma eleição", que exigiria mais eleições do que há. No erro médio por candidato, a ordem se repete de forma moderada (0,45 a 0,70 nos cortes de 2016 a 2020) e cai para 0,20 no corte de 2022. No erro da margem entre os dois primeiros, que é o que decide um 2º turno, a repetição é fraca (0,06 a 0,38). Com 19 a 26 institutos, o limiar de significância a 5% (bilateral) fica entre 0,39 e 0,46: passam os três primeiros valores da medida 3 e nenhum valor do erro na margem. O próprio Pindograma mediu correlação de 0,03 entre sua nota de 2012-2020 e o desempenho em 2022, e a FiveThirtyEight mediu cerca de 0,6 nos EUA com 28 institutos (Silver, 2014). Por isso o agregado do 2º turno não é ponderado pelo ranking.

### 4.5 Erro sistemático na mesma direção

> [!IMPORTANT]
> Erro sistemático numa direção **não indica intenção, contratação nem fraude**. Tem causas técnicas conhecidas: desenho e ponderação da amostra, modo de coleta, quem aceita responder (Groves & Lyberg, 2010; Kennedy et al., 2018; Sturgis et al., 2018). Esta seção mede o erro; não atribui motivo.

**Tabela 5.** Viés com direção, 2012-2022: erro com sinal na fatia bipartidária do candidato do PT (1517 pesquisas; indústria: +0,60 pp no 1º turno, +0,20 pp no 2º).

| Instituto | Pesquisas | Anos | Viés bruto pró-PT | Efeito de casa pró-PT (vs. rivais) | Encolhido | Pesquisas do mesmo lado | Ciclos pró-PT / ciclos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Brasmarket | 11 | 2022-2022 | -8,11 | -8,59 | -3,63 | 0% | 0 / 1 |
| Veritá | 53 | 2012-2022 | -4,34 | -4,48 | -3,32 | 12% | 0 / 5 |
| Paraná Pesquisas | 53 | 2016-2022 | -2,83 | -3,37 | -2,62 | 9% | 0 / 4 |
| Futura | 22 | 2012-2022 | -0,93 | -0,62 | -0,34 | 32% | 2 / 3 |
| Real Time Big Data | 45 | 2018-2022 | -1,74 | -0,28 | -0,21 | 52% | 1 / 3 |
| MDA | 23 | 2012-2022 | +1,58 | +0,37 | +0,22 | 73% | 2 / 4 |
| Quaest | 19 | 2020-2022 | +3,26 | +0,56 | +0,32 | 63% | 2 / 2 |
| Datafolha | 81 | 2012-2022 | +2,55 | +0,39 | +0,33 | 65% | 4 / 6 |
| Ipespe | 29 | 2014-2022 | +1,60 | +0,72 | +0,47 | 61% | 2 / 4 |
| Ipec (antigo Ibope) | 498 | 2012-2022 | +1,98 | +1,21 | +1,15 | 65% | 4 / 6 |
| Vox Populi | 27 | 2012-2018 | +6,16 | +3,52 | +2,27 | 78% | 3 / 4 |
| AtlasIntel | 58 | 2020-2022 | +1,14 | +2,87 | +2,28 | 72% | 1 / 2 |

**Padrões que se repetem em todos os ciclos** (sugestivos, nenhum conclusivo):

- **Veritá:** ficou abaixo dos rivais na fatia do PT em todos os 5 ciclos em que aparece (efeito de casa −4,5 pp; teste do sinal por ciclo, p = 0,06). Contra o resultado, superestimou o PT em 19% das suas pesquisas.
- **Paraná Pesquisas:** abaixo dos rivais na fatia do PT nos 4 ciclos (efeito de casa −3,4 pp; p = 0,12). Na série presidencial, nos 2 segundos turnos com pesquisa a até 7 dias da eleição, superestimou o candidato de direita em 1; o outro ficou dentro do arredondamento.

**Padrões de contagem por pesquisa, com ressalva:**

- **Ibope/Ipec:** na série presidencial, subestimou o candidato de direita nos 5 primeiros turnos com pesquisa a até 7 dias (p = 0,06) e nos 4 segundos turnos com erro maior que 0,5 pp (p = 0,12; outros 2 ficaram dentro do arredondamento). Todo o mercado errou nessa direção no 1º turno; contra os rivais do mesmo ano, o Ibope/Ipec errou menos que a média.
- **Datafolha:** subestimou o candidato de direita em 8 de 10 primeiros turnos (p = 0,11); no 2º turno, 3 contra, 1 a favor e 3 dentro do arredondamento. Contra os rivais, a diferença é pequena (+0,4 pp na fatia do PT, 4 de 6 ciclos).
- **Vox Populi e Sensus:** subestimaram o candidato de direita em todas as pesquisas finais presidenciais com erro acima do arredondamento (8 de 8 e 7 de 8).

**Padrões que não se sustentam:** AtlasIntel (efeito de casa +2,9 pp vindo quase todo de 2022; em 2020 foi −1,9; dois ciclos, sinais opostos); Quaest e Brasmarket (um ou dois ciclos).

**Ressalva estatística.** Faixa de empate: erros de até 0,5 pp contam como arredondamento, não como direção. Pesquisas de um mesmo ciclo compartilham o erro daquele ciclo, e institutos tendem a se aproximar uns dos outros (Clinton & Rogers, 2013); por isso a contagem por ciclo é a evidência mais conservadora. Há mais de vinte testes do sinal entre institutos e turnos; com a correção de Bonferroni, nenhum padrão sobrevive.

**A inclinação histórica previu 2026? Não.** A correlação de postos entre o efeito de casa histórico na fatia do PT e o erro de cada instituto no 1º turno de 2026 é 0,18 (9 institutos); com o efeito de casa no 2º turno de 2026, −0,25 (11 institutos). O caso mais claro é a Veritá: historicamente a mais distante do PT em relação aos rivais, acertou o 1º turno de 2026 e está levemente do lado de Lula no 2º turno (-0,16 pp). A leitura compatível com os dados é que institutos recalibram depois de errar.

### 4.6 O 2º turno de 2026

**Tabela 6.** **Rodada mais recente de cada instituto até 23/10** (votos válidos; quando o instituto divulgou só votos totais, o válido é calculado dividindo cada candidato pela soma dos dois). Contratante, campo, entrevistas, confiança e registro: dado aberto do TSE.

| Instituto | Contratante (registro TSE) | Campo | Entrevistas | Margem | Confiança | Registro | Flávio | Lula |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gerp | Gerp Mercadologia Ltda | 17/10 a 20/10 | 2.400 | ±2,0 pp | 95,55% | BR-03835/2026 | 52,6% | 47,4% |
| Real Time Big Data | Real Time Midia Ltda | 19/10 a 22/10 | 2.000 | ±2,0 pp | 95% | BR-09670/2026 | 52,1% | 47,9% |
| DataTrends | Instituto Datatrends Ltda | 19/10 a 21/10 | 2.000 | ±2,19 pp | 95% | BR-03365/2026 | 52,1% | 47,9% |
| Indexa | Agencia Estado S.A / Agencia Estado | 13/10 a 14/10 | 2.000 | ±2,2 pp | 95% | BR-04629/2026 | 51,2% | 48,8% |
| AtlasIntel | Atlasintel Tecnologia De Dados Ltda | 13/10 a 18/10 | 5.000 | ±1,0 pp | 95% | BR-02418/2026 | 51,1% | 48,9% |
| Futura | Futura Consultoria E Assessoria Ltda / Futura | 19/10 a 20/10 | 2.000 | ±2,2 pp | 95% | BR-06614/2026 | 51,1% | 48,9% |
| Ideia | Canal Meio S.A. | 15/10 a 19/10 | 1.500 | ±2,5 pp | 95% | BR-08251/2026 | 51,1% | 48,9% |
| Palver | Palver Consultoria E Desenvolvimento Tecnologico Ltda. | 16/10 a 20/10 | 5.000 | ±2,4 pp | 95% | BR-04612/2026 | 51,0% | 49,0% |
| PoderData | Poderdata Pesquisa, Jornalismo E Comunicacao Ltda | 19/10 a 21/10 | 4.000 | ±1,6 pp | 95% | BR-07926/2026 | 51,0% | 49,0% |
| Instituto França | Instituto Franca De Pesquisas Ltda | 16/10 a 20/10 | 3.000 | ±1,8 pp | 95% | BR-07896/2026 | 50,8% | 49,2% |
| Veritá | Instituto Verita Ltda | 15/10 a 19/10 | 15.554 | ±1,0 pp | 95% | BR-06396/2026 | 50,8% | 49,2% |
| Quaest | Editora Globo S/A / Editora Globo; Globo Comunicacao E Participacoes S/A / Tv/Rede/Globo.Com/Canais Globo/Globoplay/Eletromidia | 17/10 a 20/10 | 2.154 | ±2,0 pp | 95% | BR-08535/2026 | 50,6% | 49,4% |
| Datafolha | Empresa Folha Da Manha S.A.; Globo Comunicacao E Participacoes S/A / Tv/Rede/Globo.Com/Canais Globo/Globoplay/Eletromidia | 20/10 a 22/10 | 2.520 | ±2,0 pp | 95% | BR-09709/2026 | 50,5% | 49,5% |
| Ipespe | Ipespe Inst De Pesquisas Sociais Politicas E Economicas | 20/10 a 22/10 | 1.500 | ±2,6 pp | 95,45% | BR-04350/2026 | 50,5% | 49,5% |
| MDA | Confederacao Nacional Do Transporte | 13/10 a 15/10 | 2.002 | ±2,2 pp | 95% | BR-00652/2026 | 50,5% | 49,5% |
| Nexus | Banco Btg Pactual S.A. | 16/10 a 18/10 | 2.000 | ±2,0 pp | 95% | BR-04499/2026 | 50,3% | 49,7% |
| Vox Brasil | Instituto Vox Brasil Opiniao E Pesquisas Ltda | 20/10 a 22/10 | 2.100 | ±2,15 pp | 95% | BR-03259/2026 | 49,4% | 50,6% |

Nomes de parceiros de divulgação (Bloomberg, Aya, BTG, CNT, Meio, Broadcast, Abrapel, 100% Cidades) aparecem só quando são contratantes no registro do TSE.

**Centro.** Mediana 51,0% para Flávio; média 51,0%; desvio entre institutos 0,76 pp. Só a Vox Brasil (49,4) põe Lula numericamente à frente. A Vox Brasil não é o Vox Populi da série histórica: são empresas diferentes. Sem a rodada de fonte única (DataTrends), a mediana é 50,9. Sem as rodadas com campo a mais de 7 dias (Indexa e MDA), continua 51,0.

**Rodada fora do agregado.** Uma rodada (Alfa Inteligência) foi excluída por conflito entre o resultado divulgado e o registro no TSE: o número de entrevistas e a margem informados correspondem a outro registro do mesmo instituto.

**Tendência.** Três de quatro janelas mostram queda de Flávio e projetam 50,2 a 50,6 para 25/10 (desde 05/10, −0,12 pp por dia; desde 12/10, −0,06; desde 18/10, −0,08); só a janela desde 15/10 é plana (+0,03 pp por dia, projeção de 51,1). As janelas curtas têm poucos pares de rodadas do mesmo instituto. Por isso a tendência entra como sensibilidade, não como centro.

**Institutos sem histórico.** Dos 17 institutos do agregado, Gerp tem 11 pesquisas finais na base de 2012-2022 (penúltima de 113 no erro relativo da margem), e DataTrends, Vox Brasil, Indexa, Palver e Nexus não têm histórico na base. A mediana sem as 3 rodadas mais altas para Flávio é 50,79; sem as 3 mais altas e as 3 mais baixas, 51,00. A mediana dos oito institutos com 20 ou mais pesquisas finais é 50,66, e a dos quatro deles que erraram menos que os rivais (Futura, AtlasIntel, Datafolha, MDA) é 50,82.

**Transferência de votos dos eliminados.** Com as taxas da Quaest de 21/10, a transferência projeta 51,5% para Flávio; com as da PoderData/Aya, 52,1%. Mas a própria Quaest, na mesma rodada, dá 50,56%: os cruzamentos e o número final saem da mesma amostra, e a diferença mostra que parte de quem votou em Flávio ou Lula no 1º turno não está repetindo o voto. A transferência é uma hipótese estrutural, **não uma confirmação independente** do agregado, e as subamostras de cada eliminado têm de 50 a 65 entrevistados (margem de ±12 a ±14 pp).

### 4.7 Probabilidade

**Tabela 7.** Probabilidade de vitória de Flávio. Erro sistemático calibrado nos 2º turnos presidenciais 2002-2022 (RMS 1,25 pp; sigma total 1,26 pp).

| Centro (fatia de Flávio) | Valor | Ajuste de viés | P normal | P t (6 gl) |
| --- | --- | --- | --- | --- |
| CENTRAL: mediana da última rodada | 51,00 | sem viés (+0,00) | 79% | 77% |
| CENTRAL: mediana da última rodada | 51,00 | viés histórico do 2º turno (+0,30) | 85% | 83% |
| mediana sem a rodada de fonte única (DataTrends) | 50,90 | sem viés (+0,00) | 76% | 75% |
| mediana sem a rodada de fonte única (DataTrends) | 50,90 | viés histórico do 2º turno (+0,30) | 83% | 81% |
| mediana só com rodadas até 7 dias antes (regra da calibração) | 51,00 | sem viés (+0,00) | 79% | 77% |
| mediana só com rodadas até 7 dias antes (regra da calibração) | 51,00 | viés histórico do 2º turno (+0,30) | 85% | 83% |
| mediana sem as 3 maiores para Flávio | 50,79 | sem viés (+0,00) | 73% | 72% |
| mediana sem as 3 maiores para Flávio | 50,79 | viés histórico do 2º turno (+0,30) | 81% | 79% |
| mediana sem as 3 maiores e as 3 menores | 51,00 | sem viés (+0,00) | 79% | 77% |
| mediana sem as 3 maiores e as 3 menores | 51,00 | viés histórico do 2º turno (+0,30) | 85% | 83% |
| mediana dos 4 institutos que erraram menos que os rivais em 2012-2022 | 50,82 | sem viés (+0,00) | 74% | 73% |
| mediana dos 4 institutos que erraram menos que os rivais em 2012-2022 | 50,82 | viés histórico do 2º turno (+0,30) | 81% | 80% |
| mediana dos institutos com >=20 pesquisas 2012-2022 | 50,66 | sem viés (+0,00) | 70% | 69% |
| mediana dos institutos com >=20 pesquisas 2012-2022 | 50,66 | viés histórico do 2º turno (+0,30) | 78% | 76% |
| tendência + casa, janela desde 05/10 | 50,17 | sem viés (+0,00) | 55% | 55% |
| tendência + casa, janela desde 05/10 | 50,17 | viés histórico do 2º turno (+0,30) | 64% | 64% |
| tendência + casa, janela desde 12/10 | 50,60 | sem viés (+0,00) | 68% | 68% |
| tendência + casa, janela desde 12/10 | 50,60 | viés histórico do 2º turno (+0,30) | 76% | 75% |
| tendência + casa, janela desde 15/10 | 51,10 | sem viés (+0,00) | 81% | 79% |
| tendência + casa, janela desde 15/10 | 51,10 | viés histórico do 2º turno (+0,30) | 87% | 85% |
| tendência + casa, janela desde 18/10 | 50,62 | sem viés (+0,00) | 69% | 68% |
| tendência + casa, janela desde 18/10 | 50,62 | viés histórico do 2º turno (+0,30) | 77% | 75% |
| CENTRAL | 51,00 | viés do 1º turno de 2026 se repete (sem apoio histórico) (+1,89) | 99% | 97% |
| CENTRAL | 51,00 | sem viés, sigma calibrado em 14 dias (RMS 1.41) (+0,00) | 76% | 75% |

**Cenário central:** 77% para Flávio (normal: 79%). A faixa de 55% a 79% vem quase toda da escolha do centro, não de σ:

- **Só institutos com 20 ou mais pesquisas** (mediana 50,66): 69%. **Só os quatro mais precisos** (50,82): 73%.
- **Se a queda do início de outubro tiver continuado** (janela desde 05/10): 55%.
- **Com σ calibrado em pesquisas de até 14 dias** (RMS 1,41 pp): 75%. **Com σ de um 2º turno estadual** (3,3 pp): 62%.

O ajuste pelo viés histórico do 2º turno (+0,30 pp) aparece na Tabela 7 só como sensibilidade: o viés não é distinguível de zero, e somá-lo ao centro contaria duas vezes um erro que o RMS já inclui.

| σ (pp) | P(Flávio), centro 51,0, normal |
| --- | --- |
| 0,7 | 92% |
| 1,0 | 84% |
| 1,3 | 78% |
| 1,5 | 75% |
| 2,0 | 69% |
| 2,5 | 66% |
| 3,3 | 62% |

## 5. Discussão

O retrato que sai dos dados é diferente do que circula nos dois lados.

**Para quem lê o 1º turno como prova de que as pesquisas escondem a direita:** o 1º turno de fato subestimou o candidato de direita em todas as eleições desde 2002. Mas o 2º turno não repete o erro, e os institutos cujo erro vai sistematicamente na direção oposta (Veritá, Paraná Pesquisas) não acertam mais por isso: a Veritá acertou o 1º turno de 2026 e errou 4,8 pp no 2º turno de 2014.

**Para quem lê o 2º turno como inflado a favor de Flávio:** os números mais altos vêm de institutos sem histórico na base, mas a mesma ausência vale para institutos com números mais baixos, e o corte simétrico (3 de cada ponta) mantém a mediana em 51,0. Os institutos com 20 ou mais pesquisas também dão Flávio à frente (50,66).

**O ponto central:** o erro que importa num 2º turno é comum a todos os institutos (Shirani-Mehr et al., 2018; Prosser & Mellon, 2018; Jennings & Wlezien, 2018), e não tem direção previsível a partir do 1º turno. Uma eleição a 51-49 está dentro do erro histórico de um 2º turno presidencial (RMS 1,25 pp). Flávio é favorito, não vencedor certo.

## 6. Ameaças à validade

1. **Seis segundos turnos calibram σ.** A distribuição t compensa em parte, mas um erro fora da história (como o de 1º turno) é possível.
2. **Pesquisas correlacionadas.** Institutos usam cadastros, ponderações e modos parecidos e tendem a se aproximar uns dos outros; tratamos o agregado como uma medida com erro comum.
3. **Modos diferentes** (presencial, telefone com entrevistador, URA, online) não foram controlados no agregado.
4. **Comparecimento.** A abstenção de 21% no 1º turno não é modelada; é o canal que as pesquisas medem pior.
5. **Fontes secundárias para os números das rodadas.** Registro, campo, entrevistas, contratante, margem e confiança vêm do TSE; os percentuais vêm de reportagens e de relatórios dos institutos. Uma rodada do agregado tem fonte única (DataTrends).
9. **σ provavelmente subestimado.** Foi calibrado com pesquisas da véspera e é aplicado a rodadas de 3 a 11 dias antes; não inclui o movimento real dos últimos dias nem as rodadas de 24/10. Com pesquisas de até 14 dias, o RMS sobe de 1,25 para 1,41 pp (cenário na Tabela 7).
6. **Replicação parcial da base do Pindograma** (cerca de 72% das pesquisas do ranking publicado).
7. **Classificação ideológica.** A medida pró-PT não depende de classificação; a de bloco de esquerda depende da lista declarada.
8. **Dados históricos de 1989 a 2010** vêm de tabelas que citam o TSE, porque o sítio de resultados do TSE recusa acesso automatizado para esses anos.

## 7. Previsões registradas para o teste de 25/10/2026

Registradas em 23/10/2026, antes das rodadas finais de 24/10 e do resultado. O selo SHA-256 deste arquivo, do código e dos dados está em `output/provenance.json` do repositório (conferível com `python3 -I make_provenance.py --verify`).

| # | Previsão | Como será avaliada |
| --- | --- | --- |
| P1 | Flávio vence com probabilidade 0,77 | Escore de Brier (Brier, 1950): 0,053 se Flávio vencer, 0,593 se perder |
| P2 | Fatia de Flávio nos válidos entre 49,2% e 52,8% (intervalo de 80%) e entre 47,9% e 54,1% (95%) | resultado TSE |
| P3 | O erro absoluto do agregado (mediana) será menor que 1,25 pp | resultado TSE |
| P4 | A mediana dos institutos com 20+ pesquisas finais (50,66) erra menos que a dos demais (51,02) | erro absoluto de cada mediana |
| P5 | A ordem dos institutos no erro da margem do 1º turno prevê pouco a do 2º: Spearman entre −0,2 e 0,4 | erro M5 de cada instituto no 2º turno |
| P6 | Não haverá viés de 2º turno do mesmo tamanho do 1º: erro bipartidário do agregado menor que 1,9 pp em módulo | resultado TSE |
| P7 | Os dois maiores efeitos de casa de 2026 (Gerp +1,93 e Vox Brasil −1,65) ficam ambos mais longe do resultado que a mediana dos institutos | erro absoluto de cada um |

## 8. Status epistêmico de cada achado

| Achado | Status | Por quê |
| --- | --- | --- |
| Pesquisas finais do 1º turno de 2026 subestimaram Flávio (12 de 12, 10 por mais de 0,5 pp); Lula sem erro com direção | Defensável | Estimativas de cada instituto contra o resultado do TSE |
| 1º turno subestima o candidato de direita/PSDB (6 de 6 desde 2002) | Defensável | Série presidencial 2002-2022 |
| 2º turno sem viés detectável (−0,30 ± 0,54 pp) e erro de 1,25 pp | Defensável, com n = 6 | Série presidencial 2002-2022 |
| Erro do 1º turno não prevê erro do mesmo lado no 2º (correlação −0,61) | Conjectura fértil | n = 6 |
| Classificação de acurácia | Defensável, com ressalva | Muda com a medida, o turno e a base |
| A ordem de acurácia se repete pouco entre períodos | Testado: fraco na margem (0,06 a 0,38), moderado no erro por candidato (0,20 a 0,70) | 2012-2022, antes x depois de um corte |
| Veritá e Paraná Pesquisas abaixo dos rivais na fatia do PT em todos os ciclos | Sugestivo | 5/5 e 4/4 ciclos; p = 0,06 e 0,12; não sobrevive à correção de multiplicidade |
| Efeito de casa pró-PT da AtlasIntel | Não sustentado | Dois ciclos, sinais opostos |
| Erro histórico na mesma direção prevê o de 2026 | Não sustentado | Spearman 0,18 e −0,25 |
| Probabilidade de 77% (faixa 55% a 79%) | Conjectura fértil | Depende do centro e de σ calibrado com seis eleições |
| Transferência dá Flávio 51,5% a 52,1% | Hipótese estrutural | Mesma amostra do agregado; subamostras de 50 a 65 entrevistados |
| Comportamento da abstenção em 25/10 | Especulação | Não modelado |

## 9. Conformidade com a legislação eleitoral

Este texto é uma **estimativa própria derivada de pesquisas registradas**, não uma pesquisa eleitoral, e não contém enquete nem consulta ao leitor. Todas as rodadas citadas foram conferidas no dado aberto de registro do TSE (arquivo `pesquisa_eleitoral_2026.zip`, gerado em 23/10/2026 às 05:46) e foram registradas até 17/10/2026; pela regra de divulgação a partir do quinto dia após o registro, já podiam ser divulgadas em 23/10/2026. As Tabelas 1 e 6 trazem, para cada pesquisa citada, instituto, contratante, período de campo, número de entrevistas, margem de erro, nível de confiança e número de registro, como exige o art. 10 da Resolução TSE nº 23.600/2019. As alterações das Resoluções nº 23.727/2024 e nº 23.747/2026 foram lidas no texto compilado do TSE (https://www.tse.jus.br/legislacao/compilada/res/2024/resolucao-no-23-727-de-27-de-fevereiro-de-2024 e https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-747-de-26-de-fevereiro-de-2026). A leitura jurídica é do autor, não um parecer.

## 10. Dados, código e reprodução

Todo número deste texto sai dos scripts em `codigo/`, rodados em 23/10/2026 com Python 3 sem dependências externas, na ordem definida em `run_all.py`:

```bash
python3 -I run_all.py
```

A base de 2012-2022 é do Pindograma (licença GPL-3; https://github.com/pindograma/ranking_de_institutos). O registro das pesquisas de 2026 é do TSE (https://dadosabertos.tse.jus.br, pacote `pesquisas-eleitorais-2026`).

## Referências

- ARZHEIMER, K.; EVANS, J. A new multinomial accuracy measure for polling bias. **Political Analysis**, v. 22, n. 1, p. 31-44, 2014. https://doi.org/10.1093/pan/mpt012
- BOLOGNESI, B.; RIBEIRO, E.; CODATO, A. Uma nova classificação ideológica dos partidos políticos brasileiros. **Dados**, v. 66, n. 2, e20210164, 2023. https://doi.org/10.1590/dados.2023.66.2.303
- BRIER, G. W. Verification of forecasts expressed in terms of probability. **Monthly Weather Review**, v. 78, n. 1, p. 1-3, 1950. https://doi.org/10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2
- CLINTON, J. D.; ROGERS, S. Robo-polls: taking cues from traditional sources? **PS: Political Science & Politics**, v. 46, n. 2, p. 333-337, 2013. https://doi.org/10.1017/S1049096513000012
- GELMAN, A.; HULLMAN, J.; WLEZIEN, C.; MORRIS, G. E. Information, incentives, and goals in election forecasts. **Judgment and Decision Making**, v. 15, n. 5, p. 863-880, 2020. https://doi.org/10.1017/S1930297500007981
- GRAEFE, A. Predicting elections: experts, polls, and fundamentals. **Judgment and Decision Making**, v. 13, n. 4, p. 334-344, 2018. https://doi.org/10.1017/s1930297500009219
- GRAMACHO, W. G. A margem das margens?: a precisão das pesquisas pré-eleitorais brasileiras em 2010. **Opinião Pública**, v. 19, n. 1, p. 65-80, 2013. https://doi.org/10.1590/s0104-62762013000100004
- GROVES, R. M.; LYBERG, L. Total survey error: past, present, and future. **Public Opinion Quarterly**, v. 74, n. 5, p. 849-879, 2010. https://doi.org/10.1093/poq/nfq065
- KLINE, R.; STOUT, C. **Measuring polling bias in 2008: the Bradley effect and related issues**. Working paper. Irvine: UC Irvine, Center for the Study of Democracy, 2009.
- ITAÚ ASSET MANAGEMENT. **Pesquisas eleitorais no Brasil**. White paper, maio 2018.
- JACKMAN, S. Pooling the polls over an election campaign. **Australian Journal of Political Science**, v. 40, n. 4, p. 499-517, 2005. https://doi.org/10.1080/10361140500302472
- JENNINGS, W.; WLEZIEN, C. Election polling errors across time and space. **Nature Human Behaviour**, v. 2, n. 4, p. 276-283, 2018. https://doi.org/10.1038/s41562-018-0315-6
- KENNEDY, C. et al. An evaluation of the 2016 election polls in the United States. **Public Opinion Quarterly**, v. 82, n. 1, p. 1-33, 2018. https://doi.org/10.1093/poq/nfx047
- LINZER, D. A. Dynamic Bayesian forecasting of presidential elections in the states. **Journal of the American Statistical Association**, v. 108, n. 501, p. 124-134, 2013. https://doi.org/10.1080/01621459.2012.737735
- MARTIN, E. A.; TRAUGOTT, M. W.; KENNEDY, C. A review and proposal for a new measure of poll accuracy. **Public Opinion Quarterly**, v. 69, n. 3, p. 342-369, 2005. https://doi.org/10.1093/poq/nfi044
- MEIRELES, F.; RUSSO, G. Pesquisas eleitorais no Brasil: tendências e desempenho. **Estudos Avançados**, v. 36, n. 106, p. 117-131, 2022. https://doi.org/10.1590/s0103-4014.2022.36106.007
- MOSTELLER, F. et al. **The pre-election polls of 1948**. New York: Social Science Research Council, 1949. (Bulletin 60).
- PEREIRA, F. B.; NUNES, F. Pesquisas eleitorais e mudanças tardias na decisão do voto. **Opinião Pública**, v. 30, e3011, 2024. https://doi.org/10.1590/1807-019120243011
- PINDOGRAMA. **Ranking de institutos de pesquisa**. 24 set. 2024. Código e dados: https://github.com/pindograma/ranking_de_institutos
- PROSSER, C.; MELLON, J. The twilight of the polls? A review of trends in polling accuracy and the causes of polling misses. **Government and Opposition**, v. 53, n. 4, p. 757-790, 2018. https://doi.org/10.1017/gov.2018.7
- SHIRANI-MEHR, H.; ROTHSCHILD, D.; GOEL, S.; GELMAN, A. Disentangling bias and variance in election polls. **Journal of the American Statistical Association**, v. 113, n. 522, p. 607-614, 2018. https://doi.org/10.1080/01621459.2018.1448823
- SILVER, N. How FiveThirtyEight calculates pollster ratings. **FiveThirtyEight**, 25 set. 2014.
- STURGIS, P. et al. An assessment of the causes of the errors in the 2015 UK general election opinion polls. **Journal of the Royal Statistical Society: Series A**, v. 181, n. 3, p. 757-781, 2018. https://doi.org/10.1111/rssa.12329
- TIMES BRASIL/CNBC. Decisão 2026: ranking das pesquisas eleitorais mostra diferenças entre as estimativas dos institutos e o resultado das urnas. 19 out. 2026. https://timesbrasil.com.br/eleicoes-2026/decisao-2026-ranking-das-pesquisas-eleitorais-mostra-diferencas-entre-as-estimativas-dos-institutos-e-o-resultado-das-urnas/
- TRIBUNAL SUPERIOR ELEITORAL. **Resolução nº 23.600, de 12 de dezembro de 2019**, com as alterações das Resoluções nº 23.727/2024 e nº 23.747/2026.
