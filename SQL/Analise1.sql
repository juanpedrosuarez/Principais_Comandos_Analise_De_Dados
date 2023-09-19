SELECT: Seleciona os campos que serão retornados.
FROM: Especifica a tabela que será consultada.
GROUP BY: Agrupa os dados por um ou mais campos.
AVG: Calcula a média dos valores de um campo.
ORDER BY: Ordena os resultados por um ou mais campos.
INNER JOIN: Combina dois ou mais tabelas com base em um ou mais campos comuns.

O comando JOIN é usado para combinar dois ou mais tabelas com base em um ou mais
campos comuns. O tipo de JOIN mais comum é o INNER JOIN, que retorna apenas os 
registros que existem em ambas as tabelas.

O comando JOIN é definido da seguinte forma:
SELECT
  [campos]
FROM
  tabela_1
INNER JOIN
  tabela_2
ON
  [condição]

Onde:

campos: Campos que serão retornados.
tabela_1: Tabela que será consultada primeiro.
tabela_2: Tabela que será consultada depois.
condição: Condição que define como as tabelas serão combinadas.

A condição do JOIN é uma expressão que compara os valores de um
campo em cada tabela. Por exemplo, para combinar duas tabelas com 
base em um campo chamado "nome", a condição seria a seguinte:
ON tabela_1.nome = tabela_2.nome

Aqui estão alguns exemplos de JOINs:
INNER JOIN:

SELECT
  *
FROM
  tabela_1
INNER JOIN
  tabela_2
ON
  tabela_1.id = tabela_2.id

Este comando retornará todos os registros da tabela_1 e da tabela_2
que tenham o mesmo valor no campo "id".

  
LEFT JOIN:

SELECT
  *
FROM
  tabela_1
LEFT JOIN
  tabela_2
ON
  tabela_1.id = tabela_2.id

Este comando retornará todos os registros da tabela_1, mesmo que não
haja um registro correspondente na tabela_2.

  
RIGHT JOIN:

SELECT
  *
FROM
  tabela_1
RIGHT JOIN
  tabela_2
ON
  tabela_1.id = tabela_2.id

Este comando retornará todos os registros da tabela_2, mesmo que não
haja um registro correspondente na tabela_1.

  
FULL JOIN:

SELECT
  *
FROM
  tabela_1
FULL JOIN
  tabela_2
ON
  tabela_1.id = tabela_2.id
 
Este comando retornará todos os registros das tabelas 1 e 2

O comando GROUP BY é usado para agrupar os dados por um ou mais
campos. Os dados agrupados são usados para calcular agregações,
como a média, a soma ou o número de registros.

O comando GROUP BY é definido da seguinte forma:

SELECT
  [campos]
FROM
  tabela
GROUP BY
  [campos]

Onde:

campos: Campos que serão agrupados.
tabela: Tabela que será consultada.
Por exemplo, o seguinte comando agrupa os dados da tabela "pesquisa_satisfacao" por região:

SELECT
  regiao,
  COUNT(*) AS total_clientes
FROM
  pesquisa_satisfacao
GROUP BY
  regiao

Este comando retornará uma tabela com duas colunas:

regiao: O nome da região.
total_clientes: O número de clientes na região.


O comando ORDER BY é usado para ordenar os resultados por um ou mais campos.

O comando ORDER BY é definido da seguinte forma:
  
SELECT
  [campos]
FROM
  tabela
ORDER BY
  [campos]


Onde:

campos: Campos que serão ordenados.
tabela: Tabela que será consultada.
O sentido de ordenação pode ser ascendente (ASC) ou descendente (DESC). 
Por exemplo, o seguinte comando ordena os dados da tabela "pesquisa_satisfacao" 
por nota em ordem decrescente:

SELECT
  nota
FROM
  pesquisa_satisfacao
ORDER BY
  nota DESC


Este comando retornará uma tabela com uma coluna:

nota: A nota do cliente.
Os dados serão ordenados da nota mais alta para a nota mais baixa.
    

Análise da satisfação dos clientes por região

SELECT
  regiao,
  AVG(nota) AS media_nota
FROM
  pesquisa_satisfacao
GROUP BY
  regiao
ORDER BY
  media_nota DESC

Saída:

regiao | media_nota
------- | --------
Sudeste | 4.500000
Sul      | 4.200000
Centro-Oeste | 4.000000
Norte    | 3.800000
Nordeste | 3.500000

Análise das notas dos clientes por pergunta da pesquisa

SELECT
  pergunta,
  AVG(nota) AS media_nota
FROM
  pesquisa_satisfacao
GROUP BY
  pergunta
ORDER BY
  media_nota DESC

Saída:

pergunta | media_nota
---------- | --------
Qual é a sua satisfação com o atendimento? | 4.300000
Qual é a sua satisfação com os produtos? | 4.000000
Qual é a sua satisfação com os preços? | 3.800000


Identificação dos fatores que influenciam a satisfação dos clientes

SELECT
  pergunta,
  tempo_de_espera,
  qualidade_do_atendimento,
  AVG(nota) AS media_nota
FROM
  pesquisa_satisfacao
GROUP BY
  pergunta,
  tempo_de_espera,
  qualidade_do_atendimento
ORDER BY
  media_nota DESC

Saída:

pergunta | tempo_de_espera | qualidade_do_atendimento | media_nota
---------- | ------------- | ------------------------ | --------
Qual é a sua satisfação com o atendimento? | 0 | 5 | 4.500000
Qual é a sua satisfação com o atendimento? | 0 | 4 | 4.300000
Qual é a sua satisfação com o atendimento? | 0 | 3 | 4.100000
Qual é a sua satisfação com o atendimento? | 1 | 5 | 4.400000
Qual é a sua satisfação com o atendimento? | 1 | 4 | 4.200000
Qual é a sua satisfação com o atendimento? | 1 | 3 | 4.000000
















