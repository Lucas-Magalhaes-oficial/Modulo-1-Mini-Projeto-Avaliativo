# Modulo-1-Mini-Projeto Avaliativo

Este repositório contém o desenvolvimento do mini-projeto de Análise Exploratória de Dados (AED) aplicada ao setor de varejo, desenvolvido para o Módulo 1 (Semana 07) da SCTEC.

O objetivo principal é realizar o pipeline de ETL (Extração, Tratamento e Carga) de uma base de dados real com mais de 800 mil registros para extrair insights operacionais e estatísticos relevantes para o negócio.

## Tecnologias e Ferramentas
* **Python 3.14**
* **Módulos Nativos:** `csv` (utilizado para a leitura estruturada via `DictReader`)
* **Bibliotecas de Análise:** `pandas`

## Estrutura do Projeto
* `Base Varejo.csv`: Base de dados bruta contendo os registros históricos de compras.
* `script.py`: Script principal em Python contendo a lógica de tratamento e análise de dados.
* `README.md`: Documentação do projeto, instruções de uso e relatório final.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale a biblioteca Pandas executando o comando no terminal:
```bash
   pip install pandas

Garanta que o arquivo Base Varejo.csv está na mesma pasta que o arquivo script.py.

## Estrutura do Pipeline de ETL no Script Python

O arquivo `script.py` foi desenvolvido seguendo uma abordagem em Sprints para garantir a modularidade e organização do código:

1. **Extração (Nativa):** Leitura performática do arquivo `Base Varejo.csv` utilizando nativamente o módulo `csv.DictReader` para mapear o delimitador de ponto e vírgula (`;`), carregando a estrutura de dicionários subsequente para um DataFrame do Pandas.
2. **Transformação e Limpeza:**
   * Detecção de duplicados totais e remoção automática de 96.553 linhas duplicadas.
   * Identificação de dados nulos camuflados como strings vazias (`""`) e conversão para `NaN`.
   * Preenchimento da coluna de categorias de produtos (`PR_CAT`) vazias com o termo estipulado "Sem Categoria".
   * **Validação Condicional (Critério 4):** Estruturação de validação `if/else` para colunas de dimensões físicas. Como o dataset atual fornecido não inclui atributos de peso/altura, o código blinda a execução gerando nota operacional explicativa.
   * Conversão da coluna `DATA` de string para o formato nativo `datetime`.
   * Tratamento estrito do identificador numérico de compra `CO_ID` para o tipo inteiro (`int64`).
3. **Carga:** Exportação de uma base limpa intermediária chamada `df_limpo.csv` direto no repositório local.

## Estatística Descritiva: Número de Filhos (`CL_FHL`)

A análise estatística aplicada sobre a base de clientes mapeou os seguintes parâmetros operacionais:

* **Contagem de registros válidos:** 733.447 linhas analisadas pós-limpeza.
* **Média de filhos por cliente:** 1.15
* **Mediana:** 0.0 (indicando que mais da metade da base amostral não possui filhos cadastrados).
* **Desvio Padrão:** 1.42 (demonstra uma dispersão moderada em relação à média).
* **Moda:** 0 (o perfil mais frequente na base é de clientes sem filhos).
* **Limites:** Mínimo de 0 e Máximo de 4 filhos.
* **Análise de Quartis:**
  * **25% (Q1):** 0.0 filhos
  * **50% (Q2/Mediana):** 0.0 filhos
  * **75% (Q3):** 2.0 filhos (75% da base de clientes possui até 2 filhos).

## Insights Estratégicos de Negócio

Com base nos resultados consolidados pelos agrupamentos cruzados (`groupby`) no terminal, destacam-se os seguintes padrões operacionais:

1. **Predominância Absoluta de Alimentos:** A categoria ALIMENTOS engaja o maior volume de vendas disparado no negócio, com mais de 384 mil itens comercializados. Estratégias de fidelização e promoções cruzadas devem usar essa categoria como principal ponto de atração física ou digital.
2. **Equilíbrio Volumétrico por Gênero:** O comportamento de consumo entre os gêneros Feminino (F) e Masculino (M) mantém-se proporcionalmente equilibrado em todas as frentes (ex: Alimentos registrou cerca de 200k compras por mulheres e 183k por homens). Campanhas de marketing de massa não precisam necessariamente de segmentação restrita de gênero para categorias de primeira necessidade.
3. **Concentração Crítica no Segmento B:** O segmento de clientes classificado como B representa o motor de receita da operação varejista, sendo responsável por mais de 60% do volume total de movimentações (ex: das compras de alimentos, 245.501 vieram deste grupo). Recomenda-se blindar esse público com réguas exclusivas de CRM.
4. **Oportunidade em Higiene e Limpeza:** Juntas, as categorias de HIGIENE e LIMPEZA ultrapassam a marca de 266 mil itens vendidos, demonstrando forte recorrência de cesta de compras, performando como ótimos produtos de margem intermediária para o varejista.

---

## Reflexão Teórica: O Valor do Processo de ETL

O processo de Engenharia de Dados (ETL) provou-se indispensável neste projeto. Bases de dados brutas do mundo real raramente vêm prontas para modelagem ou tomada de decisão; elas carregam ruídos, registros duplicados causados por falhas de integração de sistemas e nulos ocultos.

Se a análise descritiva ou os agrupamentos fossem gerados diretamente sobre o arquivo bruto:
* Os cálculos de médias e volumetria estariam inflados por quase 100 mil linhas duplicadas.
* Campos vazios seriam interpretados incorretamente como strings válidas pelo Pandas, quebrando o agrupamento de categorias.
* O cruzamento de períodos e datas seria impossibilitado devido à tipagem original em formato texto (`str`).

A etapa de Transformação é o que de fato converte dados brutos em ativos de informação confiáveis, garantindo precisão matemática para a tomada de decisão gerencial.
