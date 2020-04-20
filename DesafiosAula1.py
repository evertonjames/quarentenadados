import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]


avaliacoes = pd.read_csv("https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")
print(avaliacoes.head())

#Alterando título das colunas
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]

###--------------------------------------------------------------------------------------------###
#Desafio 1 do Paulo Silveira
#O Paulo fez uma análise rápida e disse que tem 18 filmes sem avaliações, será que ele acertou?
#Determine quantos filmes não tem avaliações e quais são esses filmes.
###--------------------------------------------------------------------------------------------###

###--------------------------------------------------------------------------------------------###
#Desafio 2 do Guilherme Silveira
#Mudar o nome da coluna nota do dataframe filmes_com_media para nota_média após o join.
###--------------------------------------------------------------------------------------------###

###--------------------------------------------------------------------------------------------###
#Desafio 3 do Guilherme Silveira
#Colocar o número de avaliações por filme, isto é, não só a média mas o TOTAL de votos por filme.
###--------------------------------------------------------------------------------------------###

###--------------------------------------------------------------------------------------------###
#Desafio 4 do Thiago Gonçalves
#Arredondar as médias (coluna de nota média) para duas casas decimais.
###--------------------------------------------------------------------------------------------###

###--------------------------------------------------------------------------------------------###
#Desafio 5 do Allan Spadini
#Descobrir os generos dos filmes (quais são eles, únicos). (esse aqui o bicho pega)
###--------------------------------------------------------------------------------------------###

###--------------------------------------------------------------------------------------------###
#Desafio 6 da Thais André
#Contar o número de aparições de cada genero.
###--------------------------------------------------------------------------------------------###

###--------------------------------------------------------------------------------------------###
#Desafio 7 do Guilherme Silveira
#Plotar o gráfico de aparições de cada genero. Pode ser um gráfico de tipo igual a barra.
###--------------------------------------------------------------------------------------------###
