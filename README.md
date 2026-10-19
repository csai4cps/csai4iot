# CSAI-4-IoT — Segurança do aprendizado federado em redes IoT

Material suplementar da tese de doutorado **“CSAI-4-IoT: Um Modelo de Segurança Cibernética para Sistemas IoT Baseado em Aprendizado Federado com Mecanismos Adaptativos de Defesa”**, de **Hebert de Oliveira Silva**, desenvolvida no Programa de Pós-Graduação em Tecnologia da Universidade Estadual de Campinas (UNICAMP), Faculdade de Tecnologia.

Este repositório público do projeto **CSAI-4-CPS / CSAI-4-IoT** reúne os códigos, os dados utilizados nos experimentos, os resultados e as análises que fundamentam a pesquisa.

## Resumo da tese

O aprendizado federado permite que diferentes participantes treinem um modelo compartilhado sem reunir os dados brutos em um único servidor. Entretanto, participantes maliciosos podem manipular os dados locais ou as atualizações enviadas, comprometendo o modelo global. A tese investiga esse problema na classificação de tráfego de dispositivos da Internet das Coisas (IoT), no contexto de Sistemas Ciber-Físicos (CPS).

O modelo proposto, **CSAI-4-IoT**, utiliza a estratégia de agregação **Adaptive Ultimate**, que combina uma referência íntegra no servidor, normalização da magnitude das atualizações, confiança baseada no histórico dos participantes e ponderação de suas contribuições. Um controlador adaptativo, denominado **Circuit Breaker**, decide se a atualização agregada será aplicada integralmente, atenuada ou bloqueada.

A avaliação principal utiliza tráfego de **nove dispositivos do N-BaIoT**, distribuído entre **dez clientes**, com **cem rodadas por execução** e **dez sementes de avaliação (43–52)**. São examinados os ataques Scaling, Sybil, On-Off e Cumulative, em distribuições homogêneas e heterogêneas de dados. A proposta é comparada com FedAvg, Krum, FLAME e FLTrust, além de variantes que permitem analisar seus componentes. Os datasets próprios A e C fornecem avaliações complementares; B e D são documentados pela auditoria de viabilidade e não integram a campanha quantitativa final.

Os resultados indicam desempenho próximo ao FLTrust e elevada qualidade de classificação com baixa evasão em Scaling, Sybil e On-Off nas condições estudadas. As comparações pareadas, após correção para múltiplas comparações, **não demonstraram superioridade estatística geral**. As conclusões permanecem limitadas aos dados avaliados, ao treinamento emulado e à integridade da referência do servidor. O uso de aprendizado federado, isoladamente, não constitui garantia de privacidade.

## O que está disponível no GitHub

| Material | Conteúdo | Onde consultar |
|---|---|---|
| Código experimental | Notebooks dos benchmarks, das avaliações complementares e das auditorias de viabilidade. | [acervo/code](acervo/code/) |
| Dados de entrada | Fontes N-BaIoT, datasets próprios e relatórios de preparação. | [acervo/data](acervo/data/) |
| Resultados | Métricas por execução, resumos estatísticos e resultados das campanhas iniciais e finais. | [acervo/results](acervo/results/) |
| Análises | Comparações de ablação, intervalos de confiança e dinâmica temporal dos mecanismos de defesa. | [acervo/analysis](acervo/analysis/) |
| Proveniência e integridade | Identificação das fontes, configurações das campanhas, inventários e hashes para verificar os arquivos. | [acervo/provenance](acervo/provenance/) |
| Documentação metodológica | Orientações de reprodução, dependências e limitações do ambiente experimental. | [Reprodutibilidade](acervo/docs/REPRODUCIBILITY.md) |
| Pacotes completos | Arquivos brutos, registros experimentais e gráficos das quatro campanhas finais. | [Downloads das campanhas](https://github.com/csai4cps/csai4iot/releases/tag/acervo-2026-10-19) |

## Por onde começar

1. Consulte o [índice do acervo](acervo/) para localizar o material por campanha.
2. Para examinar os resultados principais, abra [N-BaIoT](acervo/results/nbaiot-main/). As avaliações complementares estão em [Dataset A](acervo/results/dataset-a/), [Dataset C](acervo/results/dataset-c/) e [Cumulative Base/Extreme](acervo/results/cumulative-base-extreme/).
3. Para reproduzir os procedimentos, leia a [documentação metodológica](acervo/docs/REPRODUCIBILITY.md), identifique os dados e selecione o notebook da mesma campanha.
4. Para análises a partir dos registros completos, baixe o pacote correspondente e consulte o [inventário de integridade](acervo/provenance/pacotes-verificados.json).

As avaliações preliminares estão em [campanha inicial](acervo/results/initial-campaign/) e [avaliação inicial dos datasets A–D](acervo/results/initial-abcd/). Seus protocolos e resultados devem ser interpretados separadamente das campanhas finais.

## Pacotes das campanhas finais

Os quatro pacotes contêm **2.377 arquivos**, incluindo resultados brutos, registros experimentais e gráficos.

| Campanha | Arquivos | Download |
|---|---:|---|
| N-BaIoT — avaliação principal | 541 | [nbaiot-main.zip](https://github.com/csai4cps/csai4iot/releases/download/acervo-2026-10-19/nbaiot-main.zip) |
| Dataset A — avaliação complementar | 776 | [dataset-a.zip](https://github.com/csai4cps/csai4iot/releases/download/acervo-2026-10-19/dataset-a.zip) |
| Dataset C — avaliação complementar | 775 | [dataset-c.zip](https://github.com/csai4cps/csai4iot/releases/download/acervo-2026-10-19/dataset-c.zip) |
| Cumulative — comparação Base/Extreme | 285 | [cumulative-base-extreme.zip](https://github.com/csai4cps/csai4iot/releases/download/acervo-2026-10-19/cumulative-base-extreme.zip) |

Os hashes SHA-256 dos pacotes e de seus arquivos estão no [inventário](acervo/provenance/pacotes-verificados.json). As condições de reprodução e os limites de interpretação dos resultados acompanham a documentação de cada campanha.
