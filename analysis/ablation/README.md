# Ablação pareada

A análise de ablação avalia F1 macro e ASR na rodada final 99. Para cada métrica, são considerados 32 contrastes: quatro ataques, duas partições e quatro variantes. A versão completa é Adaptive_Ultimate; variantes: sem memória temporal, sem ponderação adaptativa, sem Circuit Breaker e Circuit Breaker fixo.

Cada diferença é completa menos variante, pareada por seed 43–52. Todos os contrastes contêm dez pares. IC95%: média das diferenças ± t(0,975;9) × desvio-padrão amostral das diferenças / sqrt(10). A tese mostra diferenças e limites em pontos percentuais e dz adimensional. Delta positivo favorece a completa em F1, mas indica maior evasão em ASR.

Os valores p de Wilcoxon-Holm e os tamanhos de efeito dz foram extraídos do [arquivo original](https://github.com/csai4cps/csai4iot/blob/main/acervo/results/nbaiot-main/statistics/wilcoxon_holm_effect_sizes.csv), invertendo somente a orientação quando necessário. Preservada a família original de 36 pares por ataque, partição e métrica; não foi criado novo ajuste restrito a quatro pares. As diferenças coincidem exatamente com o arquivo; maior diferença em dz após recomputação: 1,67e-16. Nenhum contraste focal é significativo; menor p ajustado 0,71875.

Os intervalos para as diferenças são pontuais e não recebem correção simultânea. Intervalo t e teste de postos têm procedimentos distintos; não se interpreta eventual exclusão de zero no IC como significância após Holm. Ausência de significância não prova equivalência nem dispensabilidade universal dos componentes. A normalização não é isolada por essas variantes.

Artefato numérico: `contrastes_finais.csv`. Os registros brutos são da campanha principal N-BaIoT; a análise não abrange os resultados das campanhas A/C nem do contraste de intensidade Cumulative Base × Extreme.

