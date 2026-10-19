# Curvas com intervalos de confiança de 95%

As curvas de Scaling, Sybil, OnOff e Cumulative apresentam bandas de IC95% para F1 macro e ASR bruto, em IID e NonIID_Dirichlet, para cinco métodos. São apresentados 8.000 valores médios, com precisão de seis casas, e 80 bandas calculadas a partir dos registros por semente.

Fonte: [campanha principal](https://github.com/csai4cps/csai4iot/releases/download/acervo-2026-10-19/nbaiot-main.zip). Os oito arquivos `raw_results.csv`, organizados por ataque e partição, contêm 72.000 observações em 7.200 grupos método–rodada, com uma observação por semente de 43 a 52. As médias e os desvios-padrão amostrais correspondem aos resumos de `all_summary_by_stage.csv`, incluído no pacote da campanha.

Cálculo: média ± 2,2621571627409915 × desvio-padrão amostral / sqrt(10). Trata-se do intervalo t bilateral de 95% para a média entre seeds, com nove graus de liberdade, conforme a metodologia da tese. O cálculo não transforma rodadas em réplicas independentes, não representa banda simultânea nem substitui testes pareados corrigidos. Os limites aproximados não foram truncados em [0,1].

O eixo vertical comum utiliza o intervalo [-0,15;1,10] para apresentar integralmente os limites calculados dos métodos exibidos (mínimo -0,124410; máximo 1,081296). As bandas transparentes indicam a incerteza da média por rodada.

Arquivo de resultados: intervalos_por_rodada.csv contém os 7.200 grupos, incluindo os nove métodos da campanha, com n, média, desvio-padrão e limites para as duas métricas. As figuras apresentam os cinco métodos selecionados para a comparação principal.
