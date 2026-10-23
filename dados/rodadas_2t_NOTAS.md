# Rodadas de 2º turno (Flávio x Lula), 2026-10-05 a 2026-10-23: notas de coleta

Coleta em 2026-10-23, só por WebSearch/WebFetch (sem navegador headless). Dados: `dados/rodadas_2t.csv` (40 rodadas, 18 colunas). Cada linha leva a URL de onde o número saiu. Campo ausente = "não achado"; conflitos de n/registro ficam em `observacao`, com um valor principal na coluna (Datafolha 22/10: n=2520; Futura 19/10: registro BR-03764/2026). `tipo_divulgado` = TOTAL, VALIDO ou AMBOS.

> [!WARNING]
> PesqEle (https://pesqele-divulgacao.tse.jus.br/) devolve HTTP 403 (Akamai) a WebFetch e curl. NENHUM registro foi conferido no TSE: todos vêm de reportagem ou do agregador Poder360. Confirmar no PesqEle antes de publicar.

## 1. Datafolha 20-22/10: n e registro

| Item | Achado |
| --- | --- |
| Registro | BR-09709/2026, igual em 8 fontes (Poder360, CNN, Terra, Tribuna PR, Diário do Nordeste, Imirante, Blog Paulo Pereira, Gazeta da Amazônia). Resolvido. |
| n = 2.520 | Poder360 (https://www.poder360.com.br/poder-eleicoes-2026/flavio-tem-50-dos-votos-validos-contra-50-de-lula-diz-datafolha/), CNN, Terra, Gazeta da Amazônia |
| n = 2.154 | Tribuna PR, Diário do Nordeste, Imirante, Blog Paulo Pereira; Metrópoles não foi lido diretamente (2.154 vem do seu pedido) |
| Pista | O Diário do Nordeste escreve "nas duas primeiras rodadas foram entrevistadas 2.520", o que sugere n diferente na 3ª. O Quenty (agregador, baixa confiança) diz "2.520 no registro; 2.154 em vários veículos". |
| Coincidência | Quaest tem n = 2.154 nas rodadas de 14/10 e 21/10. Pode ser contaminação cruzada entre matérias. |

Veredito: NÃO resolvido com fonte primária. Hipótese não confirmada: 2.520 = amostra registrada e 2.154 = entrevistas efetivas divulgadas no texto Folha/Globo. Para o artigo: citar o registro BR-09709/2026 e escrever "n = 2.520 no registro; 2.154 em parte da imprensa", ou conferir o PesqEle/relatório Folha. As rodadas anteriores têm registro próprio: BR-02949/2026 (8/10, n 2.520) e BR-00466/2026 (15/10, n 2.520). Um bloco embutido na página da CNN mostrava "BR-00875/2026, 910 entrevistados, margem 3" (só em resumo de busca, não visto no fetch): é outra pesquisa, ignorar.

## 2. Novo vs a base (itens da base conferidos e rodadas ausentes)

Base conferida (rótulo correto):

| Instituto | Base | Achado |
| --- | --- | --- |
| Veritá 50,7 (21/10) | confere, VÁLIDO (total 49,7 x 48,2), BR-06396/2026 | ok |
| Quaest 50,56 | confere, mas é cálculo do Poder360 (45/(45+44)); o instituto divulgou só TOTAL 45x44 (9% bn, 2% ind.) | ok com ressalva |
| Gerp 53 (21/10) | VÁLIDO 53x47 (total 50x45), BR-03835/2026 | ok |
| PoderData 52 (19/10) | VÁLIDO 52x48, campo 16-18/10, BR-02586/2026 | ok, mas fonte só segunda mão |
| AtlasIntel 51,1 (19/10) | VÁLIDO 51,1x48,9 (total 49,8x47,6), BR-02418/2026 | ok. ATENÇÃO: na rodada de 9/10 o 51,1 era TOTAL (51,1x45,7). Risco de troca. |
| Futura 50,8 (16/10) | VÁLIDO, campo 14-15/10, BR-03764/2026 | ok |
| Datafolha 50x50 / 50,54 | VÁLIDO 50x50; total 47x46 (47/93 = 50,54, cálculo da base) | ok |
| RTBD 52 (20/10) | VÁLIDO 52x48 (total 48x45), campo 15-19/10, BR-02952/2026 | ok |

Rodadas NOVAS depois da base (divulgadas 22-23/10) ou fora dela:

- 22/10: PoderData/Aya 51x49 válidos (19-21/10, n 4.000, BR-07926/2026).
- 23/10: Real Time Big Data 52x48 válidos (19-22/10, BR-09670/2026; total 49x45). Segunda rodada RTBD além da de 20/10.
- 23/10: Vox Brasil Lula 50,6 x Flávio 49,4 válidos (20-22/10, n 2.100, presencial, BR-03259/2026). Única com Lula à frente.
- 23/10: Ipespe/Abrapel 50,5x49,5 válidos (20-22/10, n 1.500, BR-04350/2026).
- 23/10: DataTrends 51,9x48,1 válidos (19-21/10, BR-03365/2026). Fonte única (blog); fora do agregador Poder360.
- 23/10: Alfa Inteligência 52x48 válidos (18-22/10, n 2.700, BR-08496/2026; total 49,9x46,0). Fonte única.
- Antes de 22/10 e ausentes da base: BTG/Nexus 50,3x49,7 (19/10), CNT/MDA 50,5x49,5 (16/10), Instituto França 50,8x49,2 (20/10), Meio/Ideia 51,1x48,9 (21/10), Palver 50x48 total (21/10), Indexa/Broadcast 51x49 (15/10), Ipespe 17/10 (51,2x48,8), Vox 18/10.
- Nenhuma rodada com divulgação em 24/10 (o dia ainda não chegou). A Futura anunciou nova rodada para sábado 24/10 (via resumo de busca, não verificado).

## 3. Tendência (Flávio, votos válidos, rodadas por instituto)

| Instituto | Sequência |
| --- | --- |
| Datafolha | 52 -> 51 -> 50 |
| Quaest | 51,1 -> 50,56 |
| AtlasIntel | 52,8 -> 51,1 |
| BTG/Nexus | 52 -> 50,3 |
| PoderData | 53 -> 50 -> 52 -> 51 |
| Gerp | 55 -> 52 -> 53 |
| Futura | 51,8 -> 50,8 -> 50,4 -> 51,1 |
| DataTrends | 53,1 -> 51,5 -> 51,9 |
| Ipespe | 52,7 -> 51,2 -> 50,5 |
| Veritá | 51,1 -> 50,7 |
| Vox | 49 -> 49,4 |
| RTBD | 52 -> 52 |

Última rodada de cada um dos 17 institutos com válidos divulgados: média e mediana de Flávio = 51,0 (cálculo meu; amplitude 49,4 a 53,0). Palver (sem válidos divulgados; Poder360 recalcula 51) não entra. A queda de Flávio de 52-53 (início de out.) para ~50,5-51 é o padrão de Datafolha, Atlas, Nexus, Ipespe e Quaest; Gerp, DataTrends, RTBD e Alfa não mostram queda. Esta média simples não corrige viés de casa nem a mistura de modos.

## 4. Transferências (voto no 1º turno -> 2º turno)

| Fonte | Cury | Renan Santos | Caiado | Zema | Não votou/abst. |
| --- | --- | --- | --- | --- | --- |
| Quaest 14/10 (10-13/10) | L34 F30 bn30 ind6 | L14 F40 bn43 ind3 | L23 F42 bn33 ind2 | não divulgado | Lula 43 x Flávio 38 (bn/nulo/abstenção no 1T) |
| Quaest 21/10 (17-20/10) | L48 F33 bn16 ind3 | L25 F51 bn24 | L21 F57 bn22 | não divulgado | não separado |
| AtlasIntel 9/10 (3-8/10) | L50,4 F38,9 | L28,1 F40,3 bn/ns 31,6 | L26,9 F54,9 | não divulgado | não divulgado |
| Datafolha 8/10 | agregado Cury+Renan+Caiado+Zema: F46 L32 bn15 | | | | não divulgado |

URLs: Quaest 14/10 https://www.dgabc.com.br/Noticia/4352769/quaest-34-dos-eleitores-de-cury-migram-para-lula-no-2-turno-e-30-para-flavio ; Quaest 21/10 https://www.dgabc.com.br/Noticia/4353964/quaest-48-dos-eleitores-de-augusto-cury-migram-para-lula-e-33-para-flavio ; Atlas https://www.dgabc.com.br/Noticia/4351801/atlas-bloomberg-flavio-bolsonaro-tem-51-1-contra-45-7-de-lula-no-2-turno ; Datafolha https://www.metropoles.com/brasil/datafolha-46-dos-votos-de-renan-caiado-zema-e-cury-migram-para-flavio . Subamostras pequenas (margem ~10 a 13 pp). A mudança Quaest 14->21/10 (Caiado F42->57, Renan F40->51) é grande para uma semana: tratar como ruído de subamostra até haver tabela original. PoderData 8/10 tem cruzamentos de intenção só em imagem (não lidos). Não achei nenhuma transferência em Datafolha 15/10 e 22/10, Nexus, Gerp, Futura, Veritá, MDA, RTBD, Palver, França, Meio/Ideia, DataTrends, Vox, Alfa.

## 5. Inconsistências entre fontes

1. Datafolha 22/10: n 2.520 vs 2.154 (seção 1).
2. Quaest: n = 2.154 idêntico nas duas rodadas; Poder360 o lista também para 14/10, mas a data de campo muda. Possível n fixo ou erro de cópia. Contratante TV Globo/O Globo só documentado na rodada de 14/10; o "Genial/Quaest" das rodadas anteriores a outubro não é essa série.
3. Veritá: n = 15.554 idêntico em 12-16/10 e 15-19/10. Suspeito de cópia da ficha; confiança 95% e margem 1,0 nas duas.
4. Futura 19/10: registro BR-03764/2026 (CNN, o mesmo da rodada de 16/10) vs BR-06715/2026 (Poder360). Campo 14-15/10 vs 16-17/10 no mesmo texto da CNN. A Futura 16/10 traz "setembro" no subtítulo (erro).
5. Gerp 13/10: título Poder360 "53 contra 44" vs corpo "55 contra 45 válidos". Provável total 53x44 (não confirmado).
6. PoderData 22/10: campo 19-21/10 (Poder360, ND Mais) vs 19-20/10 (CNN).
7. Palver 21/10: campo 18-20/10 (dgabc) vs 16-20/10 (Poder360 agregador). Palver fala em mudança de calibração.
8. Vox 18/10: totais 46,4x44,6 (página lida) vs 44,9x43,8 (resumo de busca/Correio da Manhã). A Exame de 23/10 mistura as duas séries.
9. Coincidências de números que geram erro de rótulo: Atlas 51,1 (total em 9/10, válido em 19/10); Futura 21/10 Flávio total 48,9 = Lula válido 48,9; Veritá total 49,7 aparece também em resumo da rodada anterior.
10. Poder360 agregador de 23/10 lista Datafolha 20-22/10 com n 2.520 e Vox 20-22 BR-03259, mas ainda traz a Veritá 12-16/10 (BR-01107) e RTBD 15-19; não inclui Ipespe 23/10, DataTrends 23/10, Alfa nem Palver como atualizados.
11. Quaest 21/10 e Palver: o "válido" é recalculado pelo Poder360, não é número do instituto; o artigo deve marcar isso.
12. Rótulo TOTAL x VÁLIDO: PoderData, Ipespe, Nexus (19/10), Vox/Alfa na capa e DataTrends divulgam principalmente válidos; Quaest e Palver divulgam totais. Misturar sem converter distorce a média.

## 6. O que não foi achado (Becos)

- PesqEle: bloqueado (403). Nenhum registro validado no TSE.
- Paraná Pesquisas: nenhuma rodada nacional de 2º turno em outubro (última achada, março, BR-00873/2026). Ipec: nenhuma pesquisa de 2026. Futura 24/10: não existe ainda.
- Relatórios originais (PDF/tabelas) de Datafolha, Quaest, Atlas, Nexus etc.: só reportagens. Palver: o PDF disponível é impressão de portal, não o relatório do instituto.
- Datafolha, Folha e Globo (domínios originais): WebFetch bloqueado em datafolha.folha.uol.com.br; g1 e Folha não lidos.
- Modo de coleta ausente para Datafolha 8/10 e 15/10, Quaest 21/10, Nexus (telefone ok), MDA 16/10, Ipespe, Veritá 12-16, Alfa, Meio (provável telefone), DataTrends 23/10.
- Contratante: vários institutos só dizem "recursos próprios" ou omitem.
- Cruzamentos por voto no 1º turno: ver seção 4 (somente Quaest, Atlas, Datafolha agregado).
- Rodadas de 1-4/10 e anteriores: o CSV começa em 5/10, salvo CNT/MDA de 3/10 (campo 30/9-2/10) incluída para tendência; Gerp de 3/10 (49x44 total, BR-00509/2026) citada na coleta mas fora do CSV.
- Revista Oeste, Exame (parte), Gazeta do Povo, bhaz, maisgoias: HTTP 403 em alguns fetches.

## Conferência AtlasIntel 2022 2T

Data da conferência: 2026-10-23.

- Última pesquisa AtlasIntel do 2º turno de 2022: campo 26 a 29/10/2022, 7.500 entrevistas online em 1.830 municípios, margem de 1 ponto percentual. Válidos: **Lula 53,4% x Bolsonaro 46,6%** (divulgada 29/10/2022, 17h04, despacho Reuters). Nível de confiança: não declarado na matéria. Bloomberg não é citada nessa matéria.
- A base (Bolsonaro 46,6% válidos) **confere** com a divulgação do instituto. O resultado do TSE (Bolsonaro 49,1%) fica 2,5 pp acima: erro de Bolsonaro nos válidos = -2,5 pp (Lula: 53,4 previsto x 50,9 apurado = +2,5 pp).
- Fonte (Reuters, republicada): https://istoedinheiro.com.br/atlasintel-mostra-lula-com-534-contra-466-de-bolsonaro
- Rodada anterior (27/10/2022): Lula 53,2% x Bolsonaro 46,8% (https://www.opovo.com.br/eleicoes-2022/2022/10/27/pesquisa-atlas-intel-lula-vai-a-532-e-bolsonaro-recua-a-468.html, só nos resultados de busca, não aberta).
- NÃO achado: a URL do relatório em atlasintel.org nem versão Bloomberg Línea de 29/10/2022 (busca padrão não os retornou). A fonte é secundária (Reuters via Isto É Dinheiro).

## Confiança e margem 2T (rodadas_2t_confianca.csv)

- O CSV tem 40 linhas de rodada, não 39. Todas conferidas na mesma ordem de registro do rodadas_2t.csv.
- Confiança declarada 95% na maioria. Exceções: Gerp 95,55% (BR-07877 e BR-03835), Ipespe 95,45% (as três rodadas).
- "não achado" (6 linhas): AtlasIntel BR-02418 (CartaCapital e Reuters/Notícias Agrícolas dão só margem 1 pp; a rodada de 9/10 diz 95%); Futura BR-06614 (CartaCapital só dá margem e registro); PoderData BR-08134 e BR-02586; Gerp BR-05187; Palver BR-08028 (PDF é página impressa ilegível por extração).
- Margens conferidas na fonte: todas batem com a coluna `margem` do rodadas_2t.csv.
- Discrepâncias novas: (a) Alfa Inteligência: a fonte acritica.net diz n=2.700 (CSV tem 1.200); (b) PoderData BR-08134: a URL ndmais listada no CSV devolve o conteúdo da rodada 19-21/10 (n 4.000, margem 1,6), não a de 5-7/10; margem 1,8 vem do CSV; (c) Futura BR-06715: a URL CNN cita o registro BR-03764; (d) Gerp BR-05187 e Futura 16/10 têm URL de outra rodada no CSV (Gerp: infomoney é da rodada BR-03835).
- Rodadas mais recentes por instituto (18): 16 têm confiança achada; faltam AtlasIntel 19/10 (BR-02418) e Futura 21/10 (BR-06614). Palver 21/10 e PoderData 22/10 têm 95%.
