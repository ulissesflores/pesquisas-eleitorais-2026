# Laudo de auditoria adversarial do artigo v1 (deep-reasoner, 2026-10-23)

Artigo auditado: `artigo/artigo-v1.md` (SHA-256 b155257553ca40bd2b1bfb8c7dffaa1794625507b8c95844982bfb09b1d19a93)

**Veredito: PUBLICÁVEL COM CORREÇÕES.** 26 números conferidos contra resultados/*.json; 1 errado (Veritá −0,24 escrito à mão; o JSON dá −0,16).

## BLOQUEIA
1. Resultado da Alfa publicado com registro em conflito (52,0, "com ela a mediana continua", dados misturados de dois registros). Correção: tirar o número; dizer só que uma rodada foi excluída por conflito.
2. Confiança "não achado" para AtlasIntel BR-02418 e Futura BR-06614, mas o dado está no CSV do TSE (linhas 27457 e 25710: 95%). Correção: preencher pelo plano amostral do TSE; tirar pendência e cenários.
3. Tabela 1 e §4.1 reproduzem resultados de 2026 sem os itens do art. 10 (registro, n, margem, confiança, contratante); Gerp 1T com registro não resolvido (BR-00509 ou BR-08168).

## DEVE CORRIGIR
4. "Compradas pelo PT" associado a achado estatístico; "inclinação", "institutos de direita". Correção: frase explícita de que erro sistemático não indica intenção nem fraude; linguagem neutra.
5. Rótulos assimétricos sobre quem puxa a mediana ("quatro" errado; RTBD é mediana, 60/113; Vox Brasil, Indexa, Palver, Nexus também sem histórico). Corte simétrico 3+3 mantém 51,00; tirar só os 3 de cima dá 50,79.
6. Tabelas 2a/2b sem limite de dias (DataPoder360 2018 a 10 dias; Paraná 2014 a 18; Ideia 2018 a 18). Aplicar 7 dias.
7. Ibope/Ipec 6/6 conta erros de arredondamento (−0,17, −0,47) como direção; com faixa de empate de 0,5 pp fica 4/4, p = 0,125; ~24 testes sem correção de multiplicidade.
8. "Veritá e Paraná subestimaram o PT em todos os ciclos" é efeito de casa contra rivais, não contra o resultado; p por ciclo 0,0625 e 0,125.
9. Contratante incompleto (Datafolha e Quaest também Globo Comunicação); nomes "AtlasIntel/Bloomberg", "Ipespe/Abrapel", "PoderData/Aya" sugerem contratantes que o TSE não registra.
10. Tabela 1 mistura origem (Gerp, Nexus, França deduzidos pelo Times; Nexus publicou 39/44 -> M5 −6,87); M3 sobre 2, 4 ou 5 candidatos; rodadas de 27/09 e 30/09 ao lado de 03/10.
11. Tendência: 3 de 4 janelas caem (12/10 e 18/10 também); Indexa (11 dias) e MDA (10 dias) no agregado contra a regra de 7 dias (sem as duas, mediana 51,00).
12. σ calibrado em pesquisas de véspera aplicado a rodadas de 3 a 11 dias antes; RMS presidencial 2T vai de 0,70 (7 dias) a 1,47 (14 dias) em calibra_sigma.json.
13. Persistência: resumo cita só a margem; e o teste é antes/depois de um ano de corte, não 1T -> 2T.
14. "Histórico longo" é por volume, não por acurácia; recorte por acurácia (Futura, AtlasIntel, Datafolha, MDA) dá 50,82 (~74%).
15. Veritá −0,24 escrito à mão; JSON dá −0,16.

## MENOR
16. "2,1 pp contra Flávio" usa 16 rodadas; nas 12 finais dá −1,90 (afeta cenário +2,12 e P6).
17. Resumo mais forte que o §8; "tende levemente ao contrário" contradiz a média −0,30; "até 85%" depende de ajuste indetectável e conta viés duas vezes.
18. §9: escrever a regra (registro + 5 dias), não a data declarada (Gerp BR-05187 tem divulgação antes do fim do campo).
19. Referências: Bolognesi não está em literatura.md; Times Brasil e Hub Político citados e não listados; Arzheimer, Linzer, Gelman 2020, Groves, Jennings, Kennedy, Sturgis, Gramacho, Meireles listados e não citados; fórmulas de Mosteller são reconstrução de Kline & Stout.
20. Deslizes: os 12 ficaram abaixo (2 por 0,03); "Veritá e Sensus" pula a Paraná; Ideia omitida; Veritá "4 a 5 pp em outros ciclos" (2022: 2,5 e 1,9); rodadas sem data passam no filtro de 7 dias (probabilidade.py:42).

## Não verificado pelo auditor
Replicação Pindograma (0,90/0,99/72%) e transferência (51,5/52,1) não estão em JSON; percentuais das rodadas só contra os CSV; parte jurídica é leitura de regra_tse.md, não parecer.
