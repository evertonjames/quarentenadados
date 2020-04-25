import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.float_format = '{:,.2f}'.format

filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]


avaliacoes = pd.read_csv("https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")
avaliacoes.head()

#Alterando título das colunas
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]

#Calcular a média das notas para cada filme
nota_media_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()


###--------------------------------------------------------------------------------------------###
#Desafio 1 do Paulo Silveira
#O Paulo fez uma análise rápida e disse que tem 18 filmes sem avaliações, será que ele acertou?
#Determine quantos filmes não tem avaliações e quais são esses filmes.
###--------------------------------------------------------------------------------------------###

filmes_com_media = filmes.join(nota_media_por_filme, on="filmeId")

###Verificar melhor, ainda nao funcionou
print("qtd de Filmes sem nota")
print(filmes_com_media['nota'].isnull().value_counts())

print(filmes_com_media["nota"].isnull)

# print("filmes sem avaliação")
# print(filmes_com_media[filmes_sem_avaliacao])

###--------------------------------------------------------------------------------------------###
#Desafio 2 do Guilherme Silveira
#Mudar o nome da coluna nota do dataframe filmes_com_media para nota_média após o join.
###--------------------------------------------------------------------------------------------###

filmes_com_media = filmes_com_media.rename(columns={'nota': 'nota_media'})
print(filmes_com_media.head())

###--------------------------------------------------------------------------------------------###
#Desafio 3 do Guilherme Silveira
#Colocar o número de avaliações por filme, isto é, não só a média mas o TOTAL de votos por filme.
###--------------------------------------------------------------------------------------------###
total_votos_por_filme = avaliacoes.groupby('filmeId')['nota'].count()
print(total_votos_por_filme.head())

filmes_com_media_e_votos = filmes_com_media.join(total_votos_por_filme, on='filmeId')
filmes_com_media_e_votos = filmes_com_media_e_votos.rename(columns={'nota': 'total_votos'})
print("Filmes com média e votos:")
print(filmes_com_media_e_votos.head())

###--------------------------------------------------------------------------------------------###
#Desafio 4 do Thiago Gonçalves
#Arredondar as médias (coluna de nota média) para duas casas decimais.
###--------------------------------------------------------------------------------------------###
filmes_com_media_e_votos['nota_media'] = filmes_com_media_e_votos['nota_media'].round(2)
print("Filmes com média e votos arredondados em 2 casas decimais:")
print(filmes_com_media_e_votos.head())
###--------------------------------------------------------------------------------------------###
#Desafio 5 do Allan Spadini
#Descobrir os generos dos filmes (quais são eles, únicos). (esse aqui o bicho pega)
###--------------------------------------------------------------------------------------------###
generos_df = filmes_com_media_e_votos.generos.str.get_dummies('|')
generos = generos_df.columns.to_list()
print("Todos os generos:")
print(generos)
###--------------------------------------------------------------------------------------------###
#Desafio 6 da Thais André
#Contar o número de aparições de cada genero.
###--------------------------------------------------------------------------------------------###
total_filmes_por_genero = filmes_com_media_e_votos.generos.str.get_dummies().sum()
print("Qtd de aparições por genero:")
print(total_filmes_por_genero)
###--------------------------------------------------------------------------------------------###
#Desafio 7 do Guilherme Silveira
#Plotar o gráfico de aparições de cada genero. Pode ser um gráfico de tipo igual a barra.
###--------------------------------------------------------------------------------------------###
total_filmes_por_genero.sort_values(ascending=False)
plt.bar(total_filmes_por_genero.index, total_filmes_por_genero.values, color='blue')
sns.set()
plt.xlabel('Generos')
plt.ylabel('Quantidade')
plt.title("Quantidade de Generos por Filme")
plt.show()
