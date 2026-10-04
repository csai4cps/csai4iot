# Reprodução e ambiente

1. Selecione a campanha e seu notebook em `code/`; não misture resultados de N-BaIoT, Cumulative complementar e A/C.
2. Preserve uma cópia do notebook e consulte os manifestos e a origem dos dados em `provenance/`.
3. No Colab, monte o Drive e adapte os caminhos de entrada e saída às suas pastas. Os notebooks originais preservam os caminhos históricos. A entrada N-BaIoT deve conter as nove fontes harmonizadas/balanceadas indicadas nas saídas e manifestos; essas entradas não são substituídas pelos datasets A/C.
4. Faça a auditoria e os controles previstos no notebook antes da campanha. A semente 42 é de calibração; a inferência principal usa 43–52. Mantenha o limiar 0,05 e o protocolo da campanha selecionada.
5. Antes de nova execução, registre o hash do código, versões das bibliotecas, backend HDBSCAN carregado, sistema, CPU, RAM, acelerador, drivers e threads. Salve esse registro junto do identificador da nova campanha.

## Dependências

Os códigos usam Python, NumPy, pandas, SciPy, scikit-learn, matplotlib e HDBSCAN; o uso de Google Colab/Drive depende da plataforma. Os arquivos preservados não fornecem um lockfile do runtime original. Não incluímos versões atuais sob o rótulo de versões históricas. Os notebooks principal e complementar indicam apenas Python `3.x` nos metadados.

FLAME tenta importar `hdbscan`, admite fallback para `sklearn.cluster.HDBSCAN` e, em último caso, instala `hdbscan` sem fixar versão. Não há registro explícito do módulo/versão carregado. Ausência da mensagem de fallback nas saídas é apenas indício compatível com importação direta. Um ambiente reconstruído deve registrar o backend efetivo e não presumir equivalência numérica dos dois backends.

## Limites históricos

- Os hashes desta distribuição foram calculados em 04/10/2026. Eles fixam a identidade dos arquivos preservados e não certificam o código antes das execuções históricas.
- As cópias N-BaIoT/Cumulative contêm saídas salvas; A/C/B/D não contêm saídas. Os manifestos A/C têm hashes dos dados, não hashes do código.
- Versões exatas, CPU/RAM, acelerador e threads do ambiente original não foram localizados. Não se garante reprodução exata de tempos ou diferenças decorrentes de dependências.
- Cumulative Base/Extreme possui parâmetros e diretório próprios; seus metadados legados do piloto não substituem o modo FINAL registrado nas saídas.
- Os artefatos em `analysis/` foram derivados para a redação da tese. As trajetórias temporais ilustrativas usam a semente 43; curvas e contrastes usam dez sementes pareadas conforme seus relatórios.
