import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.float_format = '{:,.2f}'.format

filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")
# Filmes é um DataFrame
filmes.columns = ["filmeId", "titulo", "generos"]
print(filmes.head())

avaliacoes = pd.read_csv("https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")
print(avaliacoes.head())

#Verificar formato do arquivo: qtd de linhas e colunas
print("Formato do arquivo: qtd de linhas e colunas:")
print(avaliacoes.shape)

#Alterando título das colunas
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]
print(avaliacoes.head())

#Descrição de todas as avaliações
print("Descrição das Notas:")
print(avaliacoes.describe())

#Consultar avaliações apenas do filme 1
print("Avaliações do filme 1:")
avaliacoes_filme1 = avaliacoes.query("filmeId==1")
print(avaliacoes_filme1.head())

#Descrição das avaliacoes apenas do filme 1
print("Descrição das avaliações do filme 1:")
print(avaliacoes_filme1.describe())

#calcular média das notas
print("Média das notas:")
print(avaliacoes["nota"].mean())

#calcular média de notas do filme 1
print("Média das notas do filme 1:")
print(avaliacoes_filme1["nota"].mean())

#Calcular a média das notas para cada filme
print("Média de notas para cada filme:")
nota_media_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
print(nota_media_por_filme.head())

#Criar novo DataFrame com nova coluna nota média por filme

# Não é uma boa prática porque não queremos correr o risco futuramente não ter mais a quantidade exata
#filmes[nota_media] = nota_media_por_filme
#filmes.join(nota_media_por_filme, on="filmeId")

filmes_com_media = filmes.join(nota_media_por_filme, on="filmeId")
print("Exibir novo DataFrame incluindo filmes com média:")
print(filmes_com_media.head())

#Ordenar filmes por nota
print("Filmes ordenados por maior média de nota")
print(filmes_com_media.sort_values("nota", ascending=False).head(15))

# Gerar gráfico histograma para as notas do filme 1
sns.set() #seta os quadriculados ao fundo do gráfico
plt.hist(avaliacoes_filme1["nota"]) #avaliacoes declarado anteriormente mais acima no código
#Faz a mesma coisa, porém usando a query
#plt.hist(avaliacoes.query("filmeId == 1")["nota"])
plt.xlabel('Notas Filme 1')
plt.ylabel("Quantidade")
plt.title("Avaliações do filme Toy Story")
plt.show()

#Gráfico notas filme 2
sns.set() #seta os quadriculados ao fundo do gráfico
plt.hist(avaliacoes.query("filmeId == 2")["nota"])
plt.xlabel('Notas Filme 2')
plt.ylabel("Quantidade")
plt.title("Avaliações do filme Jumanji")
plt.show()

#Gráfico notas filme 102084
sns.set() #seta os quadriculados ao fundo do gráfico
plt.hist(avaliacoes.query("filmeId == 102084")["nota"])
plt.xlabel('Notas Filme 102084')
plt.ylabel("Quantidade")
plt.title("Avaliações do filme Justice League: Doom")
plt.show()

#Desafio 1 do Paulo Silveira
#O Paulo fez uma análise rápida e disse que tem 18 filmes sem avaliações, será que ele acertou?
#Determine quantos filmes não tem avaliações e quais são esses filmes.

#Desafio 2 do Guilherme Silveira
#Mudar o nome da coluna nota do dataframe filmes_com_media para nota_média após o join.

#Desafio 3 do Guilherme Silveira
#Colocar o número de avaliações por filme, isto é, não só a média mas o TOTAL de votos por filme.

#Desafio 4 do Thiago Gonçalves
#Arredondar as médias (coluna de nota média) para duas casas decimais.

#Desafio 5 do Allan Spadini
#Descobrir os generos dos filmes (quais são eles, únicos). (esse aqui o bicho pega)

#Desafio 6 da Thais André
#Contar o número de aparições de cada genero.

#Desafio 7 do Guilherme Silveira
#Plotar o gráfico de aparições de cada genero. Pode ser um gráfico de tipo igual a barra.