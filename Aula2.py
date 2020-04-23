import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Configuracao Global
sns.set_style("whitegrid")

filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")
# Filmes é um DataFrame
filmes.columns = ["filmeId", "titulo", "generos"]

avaliacoes = pd.read_csv("https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]

# Se fosse contar generos por filme
#print(filmes["generos"].str.get_dummies('|').sum(axis=1).value_counts())

print("Grafico Padrão - Quantidade de Filmes por genero")
filmes_por_genero = filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False)
filmes_por_genero.plot()
plt.show()

print("Grafico Pizza - Quantidade de Filmes por genero")
filmes_por_genero.plot(
    kind='pie',
    title='Gráfico de Categoria de Filme',
    figsize=(8,8))
plt.show()

print("Grafico Barras - Quantidade de Filmes por genero")
filmes_por_genero.plot(
    kind='bar',
    title='Filmes por categoria',
    figsize=(8,8))
plt.show()

print("Grafico Barras cor degrade - Quantidade de Filmes por genero")
plt.figure(figsize=(16,8))
sns.barplot(x=filmes_por_genero.index,
            y=filmes_por_genero.values,
            #title='Filmes por Genero',
            # +4 incluído para o tom do dagrade ficar um pouco mais escuro
            palette=sns.color_palette("BuGn_r", n_colors=len(filmes_por_genero) + 4)
            )
plt.show()

nota_media_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
filmes_com_media = filmes.join(nota_media_por_filme, on="filmeId")

print("Nota médica das avaliações")
print(avaliacoes.groupby("filmeId").mean())

notas_do_filme_1 = avaliacoes.query("filmeId==1")["nota"]
print("Média do Filme1")
print(notas_do_filme_1.mean())
notas_do_filme_1.plot(kind='hist')
plt.show()
print("Nota de intervalo de 50 filmes")
print(filmes_com_media.sort_values("nota", ascending=False)[2450:2500])

#Função para plotar gráfico e descrição
def plot_filme(n):
  notas_do_filme = avaliacoes.query(f"filmeId=={n}")["nota"]
  notas_do_filme.plot(kind='hist')
  print("Gráfico do Filme N:")
  plt.show()
  print("Describe do Filme N")
  return notas_do_filme.describe()
#Describe do filme mágico de Oz através da função
print(plot_filme(919))

#Gerar dois gráficos
def plot_filme2(n):
  notas_do_filme = avaliacoes.query(f"filmeId=={n}")["nota"]
  notas_do_filme.plot(kind='hist')
  print("Gráfico Histograma do Filme N:")
  plt.show()
  print('\n')
  notas_do_filme.plot.box()
  print("Gráfico Boxplot do Filme N:")
  plt.show()
  print("Describe do Filme N")
  return notas_do_filme.describe()
#Describe do filme mágico de Oz através da função
print(plot_filme2(919))

#Gerar vários boxplot na mesma imagem
sns.boxplot(data = avaliacoes.query("filmeId in [1,2,919,46578]"), x ="filmeId", y="nota")
plt.show()