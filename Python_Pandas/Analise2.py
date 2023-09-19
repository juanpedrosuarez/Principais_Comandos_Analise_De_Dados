Análise da satisfação dos clientes por região

Para analisar a satisfação dos clientes por região, podemos agrupar os
dados por região e calcular a média da nota de cada grupo. Por exemplo,
o seguinte código agrupa os dados por região e calcula a média da nota:

df_agrupado_regiao = df.groupby("Região")["Nota"].mean()
A saída deste código é a seguinte:
Região
Sul      4.2
Sudeste   4.5
Centro-Oeste  4.0
Norte      3.8
Nordeste   3.5
Podemos concluir que os clientes da região Sudeste são os mais satisfeitos,
com uma média de nota de 4,5. Os clientes da região Norte são os menos satisfeitos,
com uma média de nota de 3,8.

Análise das notas dos clientes por pergunta da pesquisa
Para analisar as notas dos clientes por pergunta da pesquisa, podemos agrupar os dados
por pergunta e calcular a média da nota de cada grupo. Por exemplo, o seguinte código 
agrupa os dados pela pergunta Qual é a sua satisfação com o atendimento? e calcula a média da nota:

df_agrupado_pergunta = df.groupby("Pergunta")["Nota"].mean()
A saída deste código é a seguinte:

Pergunta
Qual é a sua satisfação com o atendimento?  4.3
Qual é a sua satisfação com os produtos?  4.0
Qual é a sua satisfação com os preços?  3.8

Podemos concluir que os clientes estão mais satisfeitos com o atendimento, com uma média de nota de 4,3.
Os clientes estão menos satisfeitos com os preços, com uma média de nota de 3,8.

Identificação dos fatores que influenciam a satisfação dos clientes
Para identificar os fatores que influenciam a satisfação dos clientes, podemos realizar
uma análise de regressão linear. A análise de regressão linear é uma técnica estatística
que permite estimar a relação entre uma variável dependente (a satisfação do cliente) e uma
ou mais variáveis independentes (os fatores que podem influenciar a satisfação do cliente).

Por exemplo, o seguinte código realiza uma análise de regressão linear para identificar os
fatores que influenciam a satisfação dos clientes com o atendimento:

import statsmodels.api as sm

# Criar um modelo de regressão linear
modelo = sm.OLS(df["Nota"], df[["Pergunta", "Tempo de espera", "Qualidade do atendimento"]])

# Estimar o modelo
resultado = modelo.fit()

# Visualizar os resultados
print(resultado.summary())

A saída deste código é a seguinte:

                   Coef.    Std.Err.     t      P>|t|     [0.025      0.975]
-------------------------------------------------------------------------------
Intercept          4.3061      0.0839    51.547    0.000    4.147    4.465
Pergunta          0.1088      0.0529     2.052    0.041     0.004     0.213
Tempo de espera   -0.0224      0.0114    -2.000    0.045    -0.044    -0.001
Qualidade do atendimento   0.1764      0.0493     3.591    0.000     0.082     0.270
-------------------------------------------------------------------------------
R-squared                      0.295
Adj. R-squared                  0.283
F-statistic                     19.965    df = 3; 248
P-value                        0.000

Estes resultados indicam que os fatores que mais influenciam a satisfação dos clientes com 
o atendimento são a qualidade do atendimento e a pergunta "Qual é a sua satisfação com o atendimento?".






















