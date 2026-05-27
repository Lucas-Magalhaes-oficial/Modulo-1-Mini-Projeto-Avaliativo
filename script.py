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