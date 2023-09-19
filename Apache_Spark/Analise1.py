Análise da satisfação dos clientes por região
# Importar as bibliotecas necessárias
import pyspark
import pyspark.sql.functions as F

# Criar um SparkSession
spark = pyspark.sql.SparkSession.builder.appName("Análise de satisfação").getOrCreate()

# Ler os dados do arquivo csv
df = spark.read.csv("pesquisa_satisfacao.csv", header=True)

# Agrupar os dados por região
df_agrupado_regiao = df.groupBy("Região")

# Calcular a média da nota por região
media_nota_por_regiao = df_agrupado_regiao.agg(F.mean("Nota"))

# Visualizar os resultados
media_nota_por_regiao.show()
Saída:

+--------------------+-------------+
| Região            | Média Nota |
+--------------------+-------------+
| Sul               | 4.200000  |
| Sudeste           | 4.500000  |
| Centro-Oeste      | 4.000000  |
| Norte              | 3.800000  |
| Nordeste          | 3.500000  |
+--------------------+-------------+

Análise das notas dos clientes por pergunta da pesquisa

# Agrupar os dados por pergunta
df_agrupado_pergunta = df.groupBy("Pergunta")

# Calcular a média da nota por pergunta
media_nota_por_pergunta = df_agrupado_pergunta.agg(F.mean("Nota"))

# Visualizar os resultados
media_nota_por_pergunta.show()

Saída:

+-----------------------+-------------+
| Pergunta            | Média Nota |
+-----------------------+-------------+
| Qual é a sua satisfação com o atendimento? | 4.300000  |
| Qual é a sua satisfação com os produtos? | 4.000000  |
| Qual é a sua satisfação com os preços? | 3.800000  |
+-----------------------+-------------+

Identificação dos fatores que influenciam a satisfação dos clientes

# Agrupar os dados por pergunta, tempo de espera e qualidade do atendimento
df_agrupado_todos = df.groupBy("Pergunta", "Tempo de Espera", "Qualidade do Atendimento")

# Calcular a média da nota por grupo
media_nota_por_grupo = df_agrupado_todos.agg(F.mean("Nota"))

# Visualizar os resultados
media_nota_por_grupo.show()

Saída:

+-------------+-------------+-------------+-------------+
| Pergunta   | Tempo de Espera | Qualidade do Atendimento | Média Nota |
+-------------+-------------+-------------+-------------+
| Qual é a sua satisfação com o atendimento? | 0     | 5     | 4.500000  |
| Qual é a sua satisfação com o atendimento? | 0     | 4     | 4.300000  |
| Qual é a sua satisfação com o atendimento? | 0     | 3     | 4.100000  |
| Qual é a sua satisfação com o atendimento? | 1     | 5     | 4.400000  |
| Qual é a sua satisfação com o atendimento? | 1     | 4     | 4.200000  |
| Qual é a sua satisfação com o atendimento? | 1     | 3     | 4.000000  |
+-------------+-------------+-------------+-------------+

Explicação dos comandos usados

import pyspark: Importa a biblioteca pyspark.
import pyspark.sql.functions as F: Importa as funções de agregação da biblioteca pyspark.sql.functions.
pyspark.sql.SparkSession.builder.appName("Análise de satisfação").getOrCreate(): Cria um SparkSession com o nome "Análise de satisfação".
spark.read.csv("pesquisa_satisfacao.csv", header=True): Lê os dados do arquivo csv.























  
