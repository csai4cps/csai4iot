# Curvas com IC95% — 04/10/2026

As quatro figuras de Scaling, Sybil, OnOff e Cumulative receberam bandas de IC95% para F1 macro e ASR bruto, em IID e NonIID_Dirichlet, nos cinco métodos já exibidos. Foram preservados os 8.000 pontos das curvas médias existentes, com precisão de seis casas; 80 bandas foram calculadas a partir dos registros por seed.

Fonte: [campanha principal](https://drive.google.com/drive/folders/1dOCORj1QenIn5Rd-93GCBOL-9MoK8O2f). Foram lidos os oito raw_results.csv por ataque/partição: 72.000 linhas, 7.200 grupos método–rodada, cada grupo contendo exatamente uma observação para cada seed de 43 a 52. Médias e desvios-padrão amostrais foram reconciliados com [all_summary_by_stage.csv](https://drive.google.com/file/d/1iM3ndPf541q-8puptLHBKg0eiqCJar5I/view); maior diferença numérica 3,33e-16.

Cálculo: média ± 2,2621571627409915 × desvio-padrão amostral / sqrt(10). Trata-se do intervalo t bilateral de 95% para a média entre seeds, com nove graus de liberdade, conforme a metodologia da tese. O cálculo não transforma rodadas em réplicas independentes, não representa banda simultânea nem substitui testes pareados corrigidos. Os limites aproximados não foram truncados em [0,1].

O eixo vertical comum foi ampliado de [0;1,02] para [-0,15;1,10] para apresentar integralmente os limites calculados dos métodos exibidos (mínimo -0,124410; máximo 1,081296). As cores dos métodos e as médias foram preservadas; bandas transparentes são desenhadas antes das curvas.

Artefato numérico local: intervalos_por_rodada.csv contém os 7.200 grupos, incluindo os nove métodos da campanha, com n, média, desvio-padrão e limites para as duas métricas. A tese apresenta os mesmos cinco métodos das figuras anteriores.
