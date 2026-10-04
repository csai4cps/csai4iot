# CSAI-4-IoT — código e resultados da tese

Material experimental organizado por campanha, preservado em 4 de outubro de 2026. Repositório preparado para acesso privado.

## Estrutura

| Diretório | Conteúdo |
|---|---|
| `code/nbaiot-main` | Notebook N-BaIoT de nove fontes, dez clientes, cem rodadas e sementes 43–52, com saídas salvas |
| `code/cumulative-base-extreme` | Notebook complementar Base × Extreme, com saídas salvas |
| `code/dataset-a` e `code/dataset-c` | Cópias dos notebooks da validação complementar |
| `code/audit-b-d` | Notebooks de auditoria e bloqueio de campanhas inviáveis |
| `results/` | Métricas por semente, médias/IC95%, Friedman, Wilcoxon-Holm, efeitos e relatórios de execução por campanha |
| `data/` | Entradas disponíveis das bases próprias A–D, preservadas sem alteração |
| `analysis/` | Artefatos derivados para as curvas, ablação pareada e diagnóstico temporal da tese |
| `provenance/` | Origens, manifestos e inventário SHA-256 dos arquivos preservados |
| `docs/` | Instruções de reprodução e limites dos registros históricos |
| `scripts/` | Verificação da integridade do pacote, sem executar os experimentos |

## Código preservado e vínculo com as execuções

Os notebooks N-BaIoT e Cumulative incluem saídas salvas com diretórios e parâmetros correspondentes aos resultados originais. As cópias A/C e de auditoria B/D não contêm saídas; os resultados A/C estão preservados separadamente. Os hashes identificam as cópias desta distribuição, não uma assinatura do código emitida pelo ambiente antes da execução. Não se apresenta como comprovada uma identidade retrospectiva integral entre arquivo atual e código executado.

## Resultados originais e arquivos grandes

O repositório contém os CSVs estatísticos e os relatórios selecionados, além das evidências A/C. Os resultados brutos completos, logs por cliente e ZIPs permanecem no Drive original e são indexados em `provenance/source-index.json`; os links podem exigir acesso à conta do autor. A pasta `analysis` contém derivados e não substitui esses arquivos originais.

- [N-BaIoT principal](https://drive.google.com/drive/folders/1dOCORj1QenIn5Rd-93GCBOL-9MoK8O2f)
- [Cumulative Base × Extreme](https://drive.google.com/drive/folders/1EZ9NIeVLuGLJneoiDVMmvEMixlzDppml)
- [Dataset A](https://drive.google.com/drive/folders/1pVno1G9TnZ7edReGqDdwzPsP1IHi05JM)
- [Dataset C](https://drive.google.com/drive/folders/1Savf5A50LTGBmk78asShq-0vvyg9T_JN)

## Reprodução

Leia `docs/REPRODUCIBILITY.md` antes de executar. Para verificar os arquivos preservados:

```sh
python3 scripts/verify_integrity.py
```

Nenhum notebook foi reexecutado para produzir esta distribuição. As campanhas B/D permanecem bloqueadas por insuficiência empírica; não se deve retirar seus mecanismos de auditoria para produzir um resultado comparável.

## Acesso e citação

Esta distribuição foi preparada como privada. Não concede autorização de redistribuição das bases nem uma licença de terceiros. Referências científicas e origem dos datasets devem ser citadas conforme a tese. Para associar esta distribuição à versão final da tese, use um commit ou release fixo do repositório, e não somente um link para uma branch mutável.
