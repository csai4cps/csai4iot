# Reprodução e ambiente

1. Selecione a campanha e a [versão para execução local](../reproduction/). Os notebooks de referência estão em `code/`; não misture resultados de N-BaIoT, Cumulative complementar e A/C.
2. Preserve uma cópia do notebook e consulte os manifestos e a origem dos dados em `provenance/`.
3. Baixe a distribuição completa do repositório e siga o [guia local](../reproduction/README.md). As nove fontes N-BaIoT estão em `data/nbaiot-main/`; A/C/B/D estão em seus subdiretórios de `data/`. As seis versões locais verificam os hashes das entradas e não dependem de Drive. Os pacotes de resultados em `raw/` são opcionais para novas execuções.
4. Faça a auditoria e os controles previstos no notebook antes da campanha. A semente 42 é de calibração; a inferência principal usa 43–52. Mantenha o limiar 0,05 e o protocolo da campanha selecionada.
5. Antes de nova execução, registre o hash do código, versões das bibliotecas, backend HDBSCAN carregado, sistema, CPU, RAM, acelerador, drivers e threads. Salve esse registro junto do identificador da nova campanha.

## Dependências

Os códigos usam Python, NumPy, pandas, SciPy, scikit-learn, matplotlib e HDBSCAN. As versões locais têm [dependências explícitas](../reproduction/requirements.txt) e registram o ambiente de cada execução. Os arquivos preservados não fornecem um lockfile do runtime original. Os notebooks principal e complementar indicam apenas Python `3.x` nos metadados.

Nos notebooks de referência, FLAME tenta importar `hdbscan`, admite fallback para `sklearn.cluster.HDBSCAN` e, em último caso, instala `hdbscan` sem fixar versão. Não há registro explícito do módulo/versão carregado. Ausência da mensagem de fallback nas saídas é apenas indício compatível com importação direta. Um ambiente reconstruído deve registrar o backend efetivo e não presumir equivalência numérica dos dois backends.

## Limitações de reprodutibilidade

- Os hashes identificam os arquivos disponibilizados; não constituem registro da versão do código no momento das execuções.
- As cópias N-BaIoT/Cumulative contêm saídas salvas; A/C/B/D não contêm saídas. Os manifestos A/C têm hashes dos dados, não hashes do código.
- Versões exatas, CPU/RAM, acelerador e threads do ambiente original não foram localizados. Não se garante reprodução exata de tempos ou diferenças decorrentes de dependências.
- Cumulative Base/Extreme possui parâmetros e diretório próprios; seus metadados legados do piloto não substituem o modo FINAL registrado nas saídas.
- Os artefatos em `analysis/` contêm análises derivadas dos registros experimentais. As trajetórias temporais ilustrativas usam a semente 43; curvas e contrastes usam dez sementes pareadas conforme seus relatórios.

Nas versões locais, o backend é explicitamente `hdbscan`. O ambiente de validação não comprova equivalência numérica com o ambiente original; as campanhas completas não foram reexecutadas nesta distribuição.
