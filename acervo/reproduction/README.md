# Execução local dos protocolos CSAI-4-IoT

Estas seis versões utilizam exclusivamente os dados incluídos no repositório. Não requerem Google Drive, autenticação Google ou download de arquivos durante a campanha. As dependências Python devem ser instaladas antes da execução.

| Campanha | Notebook local |
|---|---|
| dataset-b | [CSAI4IoT_DatasetB_Auditoria_e_Benchmark_Local.ipynb](CSAI4IoT_DatasetB_Auditoria_e_Benchmark_Local.ipynb) |
| dataset-d | [CSAI4IoT_DatasetD_Auditoria_e_Benchmark_Local.ipynb](CSAI4IoT_DatasetD_Auditoria_e_Benchmark_Local.ipynb) |
| cumulative-base-extreme | [CSAI4IoT_Cumulative_Final_BaseVsExtreme_100R_Seeds43_52_Local.ipynb](CSAI4IoT_Cumulative_Final_BaseVsExtreme_100R_Seeds43_52_Local.ipynb) |
| dataset-a | [CSAI4IoT_DatasetA_Benchmark_Final_Local.ipynb](CSAI4IoT_DatasetA_Benchmark_Final_Local.ipynb) |
| dataset-c | [CSAI4IoT_DatasetC_Benchmark_Complementar_Local.ipynb](CSAI4IoT_DatasetC_Benchmark_Complementar_Local.ipynb) |
| nbaiot-main | [CSAI4IoT_NBaIoT_MixedDevice_9Sources_100R_Seeds43_52_ThesisPressure_Local.ipynb](CSAI4IoT_NBaIoT_MixedDevice_9Sources_100R_Seeds43_52_ThesisPressure_Local.ipynb) |

## Preparação

Baixe e extraia o **Source code (zip)** da [release atual](https://github.com/csai4cps/csai4iot/releases/tag/acervo-2026-10-19-v2), ou clone o repositório. Preserve sua estrutura de pastas. Os quatro ZIPs de resultados são opcionais para novas execuções; todos os dados de entrada necessários estão em `acervo/data/`.

O ambiente de validação usa Python 3.12. Na raiz do repositório:

```text
python -m venv .venv
```

Ative o ambiente (`.venv\Scripts\activate` no Windows ou `source .venv/bin/activate` no Linux/macOS) e execute:

```text
python -m pip install -r acervo/reproduction/requirements.txt
python -m ipykernel install --user --name csai-local --display-name "Python 3 (CSAI local)"
```

Abra o notebook em uma interface Jupyter compatível e selecione o kernel **Python 3 (CSAI local)**. Execute as células na ordem. A interface Jupyter é instalada separadamente; também é possível usar uma instalação existente ou um editor com suporte a notebooks.

O notebook encontra a raiz a partir do diretório atual e de seus diretórios superiores. Se iniciado em outro local, defina a variável de ambiente `CSAI_REPO_ROOT` com o caminho da pasta extraída antes de iniciar o kernel.

## Dados, auditoria e resultados

A primeira célula confere a existência e o SHA-256 das entradas. Divergências interrompem a execução antes do treinamento. Os resultados são gravados em `.local-results/<campanha>/<identificador-único>/`, sem sobrescrever os resultados publicados. O arquivo `runtime.json` registra as entradas, as versões de dependências, o sistema e a configuração de threads disponível.

A e C mantêm a auditoria e as exclusões previstas no protocolo. B e D mantêm os controles que bloqueiam campanhas sem dados empíricos suficientes; seu bloqueio é um resultado esperado da auditoria e não deve ser contornado por aumento artificial da amostra.

N-BaIoT e Cumulative carregam nove fontes e preservam cem rodadas, sementes 43–52, semente 42 reservada à calibração e limiar 0,05. HDBSCAN utiliza explicitamente o pacote `hdbscan`, sem troca automática de implementação. A última célula inicia a campanha completa e pode demandar processamento prolongado.

## Relação com os resultados publicados

Os [notebooks de referência](../code/) permanecem íntegros. As versões locais modificam a aquisição de dados, a configuração de caminhos, a seleção explícita do backend e a organização das saídas. As funções científicas foram comparadas estruturalmente com as versões de referência. Os hashes de ambas as versões constam no [registro de execução local](../provenance/local-execution.json).

As novas versões não contêm saídas de execuções anteriores. O ambiente listado em `requirements.txt` corresponde à validação desta distribuição, não ao ambiente original dos experimentos. Foram verificados carregamento, integridade, inicialização e auditorias; as campanhas completas não foram reexecutadas para esta distribuição. Consulte também as [limitações de reprodutibilidade](../docs/REPRODUCIBILITY.md).
