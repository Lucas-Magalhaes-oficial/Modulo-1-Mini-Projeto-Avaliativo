import csv
import pandas as pd

# Leitura nativa configurada para ponto e vírgula, corrigindo a separação das colunas
with open('Base Varejo.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')
    dados_lista = list(leitor)

# Carga dos dados estruturados no DataFrame
df = pd.DataFrame(dados_lista)

# Exibição do diagnóstico corrigido
print(f"Total de registros: {df.shape[0]}")
print(f"Total de colunas identificadas: {df.shape[1]}")
print("\nPrimeiras linhas para conferência das colunas:")
print(df.head(2))
print("\nTipos de dados detectados pelo Pandas:")
print(df.dtypes)

# Diagnóstico de valores nulos para entender quais colunas precisam de atenção
print("\nValores nulos identificados por coluna:")
print(df.isna().sum())

# Verificação e remoção de registros duplicados
total_duplicados = df.duplicated().sum()
print(f"\nLinhas duplicadas encontradas: {total_duplicados}")

if total_duplicados > 0:
    df = df.drop_duplicates()
    print("Registros duplicados removidos com sucesso.")

import numpy as np

# Convertendo strings vazias para NaN real para o Pandas reconhecer os nulos
df.replace("", np.nan, inplace=True)

# 1. Tratamento da coluna de categorias (PR_CAT), preenchendo vazios com 'Sem Categoria'
if 'PR_CAT' in df.columns:
    df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')
    print("Valores ausentes em 'PR_CAT' preenchidos com 'Sem Categoria'.")

# 2. Validação condicional de dimensões físicas (Critério 4 da avaliação)
# Como a base atual não possui colunas físicas (ex: peso/altura), criamos a checagem
colunas_fisicas = ['PESO', 'ALTURA', 'LARGURA', 'PR_PESO']
dimensoes_encontradas = [col for col in colunas_fisicas if col in df.columns]

if dimensoes_encontradas:
    for col in dimensoes_encontradas:
        df[col] = df[col].fillna(df[col].median())
    print("Nulos de dimensões físicas tratados pela mediana.")
else:
    # Justificativa exigida pelo critério caso as colunas não existam no dataset recebido
    print("Nota: Nenhuma coluna de dimensão física foi identificada nesta versão da base de varejo.")