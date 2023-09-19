import pandas as pd

# Importar os dados do arquivo csv
df = pd.read_csv("pesquisa_satisfacao.csv")

# Visualizar as primeiras linhas do dataframe
df.head()

# Visualizar as últimas linhas do dataframe
df.tail()

# Visualizar um resumo do dataframe
df.describe()

# Filtrar os dados por um determinado valor
df = df[df["Satisfação"] == "Satisfeito"]

# Filtrar os dados por um intervalo de valores
df = df[df["Nota"] >= 7]

# Agrupar os dados por um determinado atributo
df_agrupado = df.groupby("Satisfação")

# Visualizar o número de registros por grupo
df_agrupado.size()

# Visualizar a média da nota por grupo
df_agrupado["Nota"].mean()

# Criar uma coluna com o código do cliente
df["Código"] = df["Nome"].str[:10]

# Criar uma coluna com a nota do cliente
df["Nota"] = df["Satisfação"].map({"Satisfeito": 5, "Indiferente": 3, "Insatisfeito": 1})

# Exportar os dados para um arquivo csv
df.to_csv("pesquisa_satisfacao_exportada.csv")

Exemplo prático

Vamos analisar um conjunto de dados hipotético de uma pesquisa de satisfação ao cliente de um banco. O conjunto de dados contém as seguintes informações:

Nome: Nome do cliente
Satisfação: Satisfação do cliente (Satisfeito, Indiferente, Insatisfeito)
Nota: Nota do cliente (de 1 a 5)
Data: Data da pesquisa
Objetivo:

Avaliar a satisfação dos clientes do banco.

Análise:

Primeiro, vamos importar os dados do arquivo csv:


import pandas as pd

# Importar os dados do arquivo csv
df = pd.read_csv("pesquisa_satisfacao.csv")

#Vamos visualizar as primeiras linhas do dataframe:
df.head()

#Vamos verificar a média da nota dos clientes satisfeitos:
df_agrupado = df.groupby("Satisfação")

df_agrupado["Nota"].mean()
Satisfação
Satisfeito    4.5
Indiferente    3.0
Insatisfeito    2.0

Podemos concluir que os clientes satisfeitos têm uma média de nota de 4,5, enquanto os clientes insatisfeitos têm uma média de nota de 2.

Vamos também visualizar o número de clientes por tipo de satisfação:
df_agrupado.size()
Satisfação
Satisfeito    100
Indiferente    50
Insatisfeito    50
Podemos concluir que a maioria dos clientes (66,7%) está satisfeita com o banco.
















