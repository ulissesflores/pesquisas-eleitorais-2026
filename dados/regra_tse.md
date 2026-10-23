# Regra legal de divulgação de pesquisas eleitorais (eleições 2026, 2º turno de 25/10/2026)

Data da apuração: 2026-10-23. Escopo: publicar hoje (23/10) um artigo que agrega pesquisas registradas no TSE e converte o agregado em probabilidade de vitória.

> [!IMPORTANT]
> Este arquivo é levantamento de fonte primária, não parecer jurídico. Onde está escrito INFERÊNCIA, é leitura minha do texto, sem decisão que a confirme. Para a parte de agregador/probabilidade, consulte advogado eleitoral antes de publicar, se o risco de representação importar.

## 0. Método e limites da apuração

- Lei 9.504/1997: texto lido em `https://www.planalto.gov.br/ccivil_03/leis/l9504.htm` (baixado em 2026-10-23, versão compilada com redações históricas e anotações).
- Resolução TSE 23.600/2019 e 23.747/2026: texto compilado lido em `tse.jus.br` pelo navegador embutido do app. O site do TSE bloqueia `curl`/WebFetch (HTTP 403, proteção anti-bot); por isso a leitura foi feita no navegador. Não usei Playwright.
- Jurisprudência: página "Temas Selecionados" do TSE (pesquisa eleitoral), lida inteira e pesquisada por termo.
- Limite: a cota de buscas web da sessão esgotou antes de eu fechar a busca por jurisprudência sobre agregadores. O resultado negativo abaixo vale para as buscas feitas (páginas do TSE lidas + várias buscas web), não prova que não exista decisão em tribunal regional ou em base não indexada.
- Não consultei o PJe/jurisprudência do TSE por termo ("agregador", "média de pesquisas"): a ferramenta de busca do TSE é SPA e não foi tentada. Quem tiver acesso deve rodar essas duas consultas em `https://www.tse.jus.br/jurisprudencia/decisoes/jurisprudencia`.

## 1. Resposta curta: o que a lei exige para publicar hoje (23/10) e em 24/10 e 25/10

| Pergunta | Resposta | Base |
|---|---|---|
| Posso divulgar pesquisa registrada hoje? | Sim, só as cujo prazo de 5 dias já venceu (registradas até 17/10 inclusive). O PesqEle informa a data de liberação de cada pesquisa. | Res. 23.600, art. 2º, caput, §2º e §3º |
| Quais dados acompanham cada pesquisa divulgada? | Período da coleta, margem de erro, nível de confiança, número de entrevistas, empresa que realizou (e contratante, se houver), número de registro. | Res. 23.600, art. 10, I a VI; art. 7º, §1º |
| Quem responde por divulgar pesquisa sem registro? | "Os responsáveis", incluindo quem replica e o veículo. Multa de R$ 53.205 a R$ 106.410. | Lei 9.504, art. 33, §3º; Res. art. 17 e art. 21; TSE (jurisprudência abaixo) |
| Pesquisa fraudulenta | Crime: detenção de 6 meses a 1 ano e multa; respondem representantes da empresa e do veículo. | Lei 9.504, art. 33, §4º e art. 35; Res. arts. 18 e 20 |
| Véspera (24/10)? | Sem proibição. A vedação de divulgar pesquisa nos 15 dias finais (art. 35-A) foi declarada inconstitucional pelo STF em 2006. A Res. 23.600 não tem essa vedação. | STF, ADI 3741/3742/3743; Res. art. 11 |
| Dia da eleição (25/10)? | Pesquisas feitas antes podem ser divulgadas "a qualquer momento, inclusive no dia das eleições" (5 dias + dados do art. 10). Levantamento de intenção de voto feito no próprio dia só pode sair a partir das 17h de Brasília. | Res. art. 11 e art. 12 (redação da Res. 23.727/2024) |
| Enquete | Vedada após 15 de agosto (a partir de 16/8). Enquete apresentada como pesquisa é tratada como pesquisa sem registro. | Res. art. 23, caput, §1º e §1º-A (Res. 23.747/2026); Lei 9.504, art. 33, §5º |
| Regra própria para agregador, média de pesquisas ou modelo probabilístico? | Não encontrei. Nem a Lei, nem a Res. 23.600 (texto compilado), nem a Res. 23.747/2026 nem o voto que a acompanha mencionam agregação, média, modelo ou probabilidade (busca textual: zero ocorrências). | Seções 3 e 4 |

Âncoras de liberação: registrada em 17/10, pode sair em 23/10; registrada em 18/10, em 24/10; registrada em 19/10, em 25/10. A data oficial é a que o PesqEle informa (art. 2º, §3º); não conte à mão.

Consequência prática para a data: o último dia de registro de pesquisas do 2º turno foi 19/10/2026 (nota do TSE de 19/10). Pelo art. 2º, §2º, entre registro e divulgação passam 5 dias inteiros: pesquisa registrada em 19/10 só pode ser divulgada a partir de 25/10. Um agregado publicado hoje não pode incluir números de pesquisa registrada depois de 17/10, mesmo que o instituto já os tenha vazado. Se o registro for alterado, o prazo recomeça (art. 8º, §1º). Conferir cada pesquisa no PesqEle.

## 2. Lei 9.504/1997, arts. 33 a 35-A (texto vigente)

URL: `https://www.planalto.gov.br/ccivil_03/leis/l9504.htm`

- Art. 33, caput: as entidades e empresas que realizarem pesquisas de opinião pública relativas às eleições ou aos candidatos, para conhecimento público, são obrigadas, para cada pesquisa, a registrar na Justiça Eleitoral "até cinco dias antes da divulgação" as informações dos incisos I a VII (contratante; valor e origem dos recursos; metodologia e período; plano amostral e ponderação, intervalo de confiança e margem de erro; sistema interno de controle da coleta; questionário completo; nome de quem pagou e cópia da nota fiscal, redação da Lei 12.891/2013).
- Art. 33, §2º (Lei 12.034/2009): a Justiça Eleitoral divulga aviso do registro em 24 h e as informações ficam à disposição dos partidos e coligações por 30 dias.
- Art. 33, §3º: "A divulgação de pesquisa sem o prévio registro das informações de que trata este artigo sujeita os responsáveis a multa no valor de cinqüenta mil a cem mil UFIR." (valor atualizado pela Res. art. 17: R$ 53.205,00 a R$ 106.410,00).
- Art. 33, §4º: "A divulgação de pesquisa fraudulenta constitui crime, punível com detenção de seis meses a um ano e multa [...]".
- Art. 33, §5º (Lei 12.891/2013): "É vedada, no período de campanha eleitoral, a realização de enquetes relacionadas ao processo eleitoral."
- Art. 34: o caput foi vetado. §1º: partidos podem, por requerimento, acessar o sistema interno de controle e conferir os dados publicados. §2º: descumprimento ou obstrução da fiscalização é crime (detenção de 6 meses a 1 ano, multa de 10 a 20 mil UFIR). §3º: irregularidade nos dados publicados sujeita às penas do §2º e obriga a veicular os dados corretos "no mesmo espaço, local, horário, página, caracteres e outros elementos de destaque".
- Art. 35: respondem penalmente pelos crimes dos arts. 33, §4º e 34, §§2º e 3º "os representantes legais da empresa ou entidade de pesquisa e do órgão veiculador".
- Art. 35-A (Lei 11.300/2006): "É vedada a divulgação de pesquisas eleitorais por qualquer meio de comunicação, a partir do décimo quinto dia anterior até as 18 (dezoito) horas do dia do pleito." O Planalto mantém o texto com a anotação "Vide ADIN 3.741-2". O STF, em 06/09/2006, julgou procedente em parte as ADIs 3741, 3742 e 3743 (rel. Min. Ricardo Lewandowski) e declarou inconstitucional apenas este artigo, por restringir o direito de informação do eleitor. Fonte: `https://noticias.stf.jus.br/postsnoticias/direto-do-plenario-stf-declara-inconstitucional-em-parte-lei-que-regula-campanhas-politicas/`. Lacuna: não li o acórdão nem a ementa oficial, só a notícia do STF. Não aplicar o art. 35-A; ele não consta da Res. 23.600.
- Art. 96, III: representações por descumprimento da Lei, na eleição presidencial, dirigem-se ao TSE (legitimados: partido, coligação ou candidato; Res. 23.600, art. 15 acrescenta o Ministério Público e as federações).

## 3. Resolução TSE 23.600/2019, texto vigente em 2026

Texto compilado: `https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-600-de-12-de-dezembro-de-2019`

### 3.1 Alterações (todas as que constam do texto compilado do TSE)

| Norma | Data | O que mudou | URL |
|---|---|---|---|
| Res. 23.624/2020 | 2020 | Ajustes só para as municipais de 2020 (EC 107/2020). Irrelevante para 2026. | citada no cabeçalho do compilado |
| Res. 23.676/2021 | 2021 (a notícia do TSE sobre a resolução das eleições 2022 é de dezembro/2021; data exata não conferida) | Redação de arts. 10 (§§1º-2º), 13, 15, 23 (§1º-A, §§2º, 4º, 5º); republicação em 2022. | citada no compilado |
| Res. 23.727/2024 | 27/02/2024 (DJe 4.3.2024) | Controle judicial só por provocação (art. 1º); relatório completo (art. 2º, §§7º-A, 7º-B, 11); art. 12 reescrito (17h de Brasília) e incisos I e II revogados; impugnação mais exigente (art. 16, §§1º a 1º-C); enquete com "viés cognitivo de autosseleção" (art. 23, §1º). | `https://www.tse.jus.br/legislacao/compilada/res/2024/resolucao-no-23-727-de-27-de-fevereiro-de-2024` |
| Res. 23.747/2026 | 26/02/2026 (DJe-TSE nº 30, ed. extra, 4.3.2026, p. 125-130) | Registro no PesqEle, declaração do estatístico (art. 2º, IX), prazo adicional de 3 dias para complementar (§7º-C), delimitação geográfica (§7º-E, §7º-F), CPF/CNPJ do pagador, consultas populares (art. 1º, §2º), enquete vedada "após o dia 15 de agosto" (art. 23). | `https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-747-de-26-de-fevereiro-de-2026` |

Verificação 2024/2025/2026 pedida: em 2024 houve uma alteração (23.727); em 2025 não consta alteração no compilado; em 2026 houve uma (23.747). Limite: a conclusão "nenhuma outra alteração" se apoia no compilado do TSE, que pode ter defasagem; não conferi o DJe posterior a 4.3.2026. A Res. 23.760/2026 (calendário eleitoral) é outra norma e não altera a 23.600 (citada na busca, não li).

Nota de rodapé de qualidade: um relatório de instituto publicado pelo Poder360 cita a alteração de 2026 como "Resolução 23.727". O número correto da alteração de 2026 é 23.747; a 23.727 é de 2024.

### 3.2 O que conta como "divulgação de pesquisa"

A Resolução não define "divulgação". Os dispositivos que delimitam o objeto:

- Art. 1º: "registro e [...] divulgação de pesquisas de opinião pública, realizadas para conhecimento público, relativas às eleições, às candidatas, aos candidatos [...]" (redação 23.747/2026).
- Art. 10, caput: "Na divulgação dos resultados de pesquisas, atuais ou não [...]". Ou seja, vale também para pesquisa antiga reproduzida.
- Art. 21: os responsáveis pela publicação da pesquisa não registrada ou em desacordo, "inclusive o veículo de comunicação social", podem arcar com as consequências "mesmo que estejam reproduzindo matéria veiculada em outro órgão de imprensa".
- Art. 23, §1º-A: enquete apresentada como pesquisa "será reconhecida como pesquisa de opinião pública sem registro".

Jurisprudência do TSE (Temas Selecionados, `https://temasselecionados.tse.jus.br/temas-selecionados/pesquisa-eleitoral`):

- Basta que a pesquisa sem registro seja dirigida ao conhecimento público; não importa o número de pessoas atingidas (AgR-AREspE 060081482, 3/8/2026, rel. Min. Antonio Carlos Ferreira; AgR-AREspE 060023490, 23/4/2025, rel. Min. André Mendonça, caso de WhatsApp).
- Basta "requisitos mínimos de formalidade" para configurar pesquisa: nomes, percentuais, a palavra "pesquisa" e indicação de entidade responsável (AgR-AREspE 060004568, 15/8/2025; AgR-AREspE 060002697, 8/4/2025, rel. Min. Isabel Gallotti).
- Enquete apresentada sem esclarecer a natureza, com dados próprios de pesquisa, "gera o efeito de pesquisa" (AgR-AREspE 060006814, 11/12/2025, rel. Min. André Mendonça).
- Ausência mínima das formalidades do art. 33, sem elementos que induzam o eleitor a erro, é mera enquete (AgR-REspEl 060053523, 2/12/2025, rel. Min. Estela Aranha; AgR-AREspE 060004152, 16/10/2025).
- O art. 33, §3º, por prever sanção, tem interpretação restritiva: divulgar dados do Google Trends em rede social não se equipara a pesquisa eleitoral (AgR-AI 060300747, 7.5.2020, rel. Min. Edson Fachin).
- Replicar nota de jornal de notória credibilidade no Instagram, de boa-fé, não configurou a infração (REspe 060142496, 28.5.2019, rel. Min. Og Fernandes), embora a regra geral seja que quem replica pesquisa sem registro responde.

### 3.3 Obrigações ao divulgar (art. 10 e arts. correlatos)

Art. 10: "Na divulgação dos resultados de pesquisas, atuais ou não, serão obrigatoriamente informados": (I) período de coleta; (II) margem de erro; (III) nível de confiança; (IV) número de entrevistas; (V) nome da entidade ou empresa que realizou e, se for o caso, de quem a contratou; (VI) número de registro da pesquisa.
Art. 7º, §1º: o número de identificação "deverá constar da divulgação e da publicação dos resultados da pesquisa".
Art. 3º: a lista de candidatos apresentada aos entrevistados deve conter os nomes com registro requerido (obrigação do instituto, não do divulgador).
Art. 10, §1º: a Justiça Eleitoral "não realiza qualquer controle prévio sobre o resultado das pesquisas, tampouco gerencia ou cuida de sua divulgação" (Res. 23.676/2021).

### 3.4 Dia da eleição e véspera

- Art. 11: "As pesquisas realizadas em data anterior ao dia das eleições poderão ser divulgadas a qualquer momento, inclusive no dia das eleições, desde que respeitado o prazo de 5 (cinco) dias previsto no art. 2° e a menção às informações previstas no art. 10".
- Art. 12 (redação da Res. 23.727/2024): "A divulgação de levantamento de intenção de voto efetivado no dia das eleições somente poderá ocorrer a partir das 17h (dezessete horas) do horário de Brasília." Os incisos que distinguiam a eleição presidencial (após o fim da votação em todo o território) foram revogados.
- Véspera: sem regra específica; vale o art. 11. Não há proibição de divulgar pesquisa na véspera.
- Aviso separado, não é regra de pesquisa: Lei 9.504, art. 39, §5º, tipifica como crimes no dia da eleição, entre outros, a propaganda de boca de urna, a divulgação de propaganda de partidos ou candidatos e (inciso IV, Lei 13.488/2017) a publicação de novos conteúdos ou impulsionamento nas aplicações de internet do art. 57-B, mantidos os já publicados. O inciso IV aparece na lista de condutas de propaganda; não verifiquei como o TSE o aplica a conteúdo jornalístico/analítico. INFERÊNCIA: publicar o artigo hoje, 23/10, e não em 25/10, elimina a dúvida.

### 3.5 Redes sociais

A Res. 23.600 não tem capítulo próprio para redes sociais. Aplica-se a mesma regra de divulgação. A jurisprudência do TSE trata postagem em Facebook, Instagram e grupos de WhatsApp como divulgação quando tem forma e dados de pesquisa e é dirigida ao conhecimento público (seção 3.2). Responde "o responsável pela divulgação", e o veículo responde pelo que republica (art. 21).

### 3.6 Registro e impugnação

- Art. 2º: registro no PesqEle a partir de 1º de janeiro do ano da eleição, até 5 dias antes da divulgação, pelo instituto/empresa. O agregador não registra: ele usa pesquisas já registradas.
- Art. 9º: acesso livre à consulta dos registros; `https://www.tse.jus.br/eleicoes/pesquisas-eleitorais` mantém "Consulta às pesquisas registradas" e "Validação de código de registro de pesquisas eleitorais".
- Art. 13 e art. 15 a 16: acesso a planilhas, impugnação, liminar de suspensão da divulgação (art. 16, §1º, redação 23.727). Impugnação tem ônus de precisão (art. 16, §1º-A).
- Art. 17 a 20: multa e crimes (valores atualizados).
- Orientação do TSE em 19/10/2026 (`https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/faltam-6-dias-prazo-para-registrar-pesquisas-eleitorais-termina-nesta-segunda-feira-19`): último dia de registro das pesquisas do 2º turno foi 19/10; reafirma o art. 11 (divulgação a qualquer momento, inclusive no dia, respeitados 5 dias); lista os seis dados do art. 10; diz que as melhorias do PesqEle em 2026 "não criam novas obrigações".

## 4. Agregadores, médias de pesquisas e modelos probabilísticos

### 4.1 Texto das normas

Nenhuma das normas lidas tem regra própria. Busca textual feita no PDF da Res. 23.747 com o voto (Pet. 0600742-06.2019.6.00.0000, `https://www.tse.jus.br/eleicoes/eleicoes-2026-content/normas-e-documentacoes/arquivos-2026/resolucao-e-voto-pesquisa`): 0 ocorrências de "agreg", "média", "modelo", "probabil", "rede", "internet". Idem na página institucional "Pesquisas eleitorais" do TSE. A página institucional pede a leitura dos arts. 33, 34, 35 e 96 da Lei e das Res. 23.600 e 23.608.

### 4.2 Jurisprudência e orientação

Não achei decisão do TSE, nem orientação publicada, tratando de "agregador de pesquisas", "média de pesquisas" ou "modelo estatístico" nas eleições de 2018, 2022 ou 2024. As buscas web mostraram apenas agregadores de imprensa e empresas que afirmam usar só pesquisas registradas no PesqEle (afirmações deles, não do TSE) e nenhuma notícia de representação contra agregador. Isto é ausência de achado, com os limites da seção 0, e não prova de legalidade.

O que existe e é analogia (todas INFERÊNCIA minha):

1. O tipo sancionado é divulgar pesquisa sem registro (Lei, art. 33, §3º), e o TSE exige interpretação restritiva por ser norma sancionatória (caso Google Trends, 7.5.2020). Um agregado calculado só sobre pesquisas registradas, apresentado como análise e não como pesquisa de campo, é o caso mais distante do tipo.
2. A doutrina do "efeito de pesquisa" (enquete apresentada como pesquisa é tratada como pesquisa) pesa contra apresentar o resultado com aparência de pesquisa: percentuais por candidato, a palavra "pesquisa", entidade responsável, sem esclarecer que é derivado. O risco sobe se o produto parecer um levantamento próprio (por exemplo, "pesquisa agregada" sem linha de origem).
3. Cada pesquisa que o artigo reproduzir (números do instituto) é "divulgação dos resultados de pesquisas" e sujeita ao art. 10 e ao art. 21, mesmo que citada de outro veículo. Por isso, ao citar números de uma pesquisa, incluir os seis itens do art. 10. Isso inclui o número de registro de cada pesquisa agregada. Não achei regra que mande o agregador listar o número de registro de cada pesquisa que apenas entra no cálculo, mas o art. 7º, §1º e o art. 10, VI exigem o número na divulgação do resultado, e listá-los é barato e permite ao leitor e à Justiça Eleitoral conferir (recomendação, não exigência confirmada).
4. Probabilidade de vitória é saída de modelo, não resultado de pesquisa. Nada na norma a trata. Declarar no texto que é estimativa do autor, com data, método, versão e premissas, afasta a aparência de pesquisa e reforça a boa-fé (princípio acolhido no caso Instagram/Folha, 28.5.2019).
5. Não incluir pesquisa sem registro (nem pesquisa não registrada de instituto estrangeiro, de candidato ou de partido) no agregado. Divulgar o resultado dela ou um número derivado dela é o caso de maior risco (jurisprudência: reproduzir pesquisa irregular já divulgada não afasta a multa, AgR-REspe 114342, 2.3.2011, rel. Min. Arnaldo Versiani, citado na página de Temas Selecionados).

### 4.3 Lista de conferência para publicar hoje (derivada das seções 1 a 4)

- Só entram pesquisas do PesqEle cuja data de liberação já chegou (registradas até 17/10 se publicar em 23/10).
- Para cada pesquisa citada: período, margem, nível de confiança, nº de entrevistas, instituto/contratante, nº de registro (art. 10).
- Rotular o agregado e a probabilidade como estimativa própria derivada de pesquisas registradas; não usar o rótulo "pesquisa" para eles.
- Nada de enquete, nem consulta ao leitor.
- Data e hora do corte dos dados, feito contra o PesqEle (não contra reportagens): registrar "constava registrada e liberada no PesqEle em DD/MM HH:MM" e guardar captura da consulta de cada pesquisa. Se uma pesquisa for depois considerada não registrada (art. 2º, §7º-C e §7º-D, prazo de complementação que vai além de 25/10), essa prova sustenta a defesa de boa-fé.
- Publicar antes de 25/10, para evitar a zona cinzenta do art. 39, §5º (se o conteúdo puder ser lido como propaganda).
- Não comparar com número de pesquisa que o instituto só vai poder divulgar a partir de 24 ou 25/10.

## 5. Pendências abertas

- Rodar no sistema de jurisprudência do TSE as consultas "agregador" e "média de pesquisas", e olhar TREs (a base de Temas Selecionados não as retornou).
- Ler o acórdão da ADI 3741 (não li; só a notícia do STF).
- Conferir se o compilado do TSE está atualizado após 4.3.2026.
- Res. 23.608/2019 (representações) e a Res. 23.610 (propaganda) não foram lidas aqui.
