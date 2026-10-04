# Ablação pareada — 04/10/2026

Foram acrescentadas duas tabelas ao capítulo 5, uma para F1 macro e outra para ASR na rodada final 99. Cada tabela reúne 32 contrastes: quatro ataques, duas partições e quatro variantes. A versão completa é Adaptive_Ultimate; variantes: sem memória temporal, sem ponderação adaptativa, sem Circuit Breaker e Circuit Breaker fixo.

Cada diferença é completa menos variante, pareada por seed 43–52. Todos os contrastes contêm dez pares. IC95%: média das diferenças ± t(0,975;9) × desvio-padrão amostral das diferenças / sqrt(10). A tese mostra diferenças e limites em pontos percentuais e dz adimensional. Delta positivo favorece a completa em F1, mas indica maior evasão em ASR.

Os valores p de Wilcoxon-Holm e os tamanhos de efeito dz foram extraídos do [arquivo original](https://drive.google.com/file/d/11ygAzoRPYroPuEy404zegu5GsSxzg751/view), invertendo somente a orientação quando necessário. Preservada a família original de 36 pares por ataque, partição e métrica; não foi criado novo ajuste restrito a quatro pares. As diferenças coincidem exatamente com o arquivo; maior diferença em dz após recomputação: 1,67e-16. Nenhum contraste focal é significativo; menor p ajustado 0,71875.

Os intervalos para as diferenças são pontuais e não recebem correção simultânea. Intervalo t e teste de postos têm procedimentos distintos; não se interpreta eventual exclusão de zero no IC como significância após Holm. Ausência de significância não prova equivalência nem dispensabilidade universal dos componentes. A normalização não é isolada por essas variantes.

Artefato numérico: `contrastes_finais.csv`. O texto correspondente foi incorporado à tese, cujo projeto LaTeX é mantido separadamente. Os registros brutos são da campanha principal N-BaIoT; esta complementação não é uma análise das campanhas A/C nem do contraste de intensidade Cumulative Base × Extreme.

Compilação confirmada no Overleaf: zero erros, PDF com 290 páginas. Permanecem dois avisos (babel e posicionamento de um float do apêndice histórico). Tabelas 5.6 e 5.7 conferidas nas páginas 128–131, com cabeçalhos de continuação e interpretação. Commit sincronizado: 4542a72f245f056d4141ea0696c48482ed8ab9c8.
