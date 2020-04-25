import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
pd.options.display.float_format = '{:,.2f}'.format


imdb = pd.read_csv("https://gist.githubusercontent.com/guilhermesilveira/24e271e68afe8fd257911217b88b2e07/raw/e70287fb1dcaad4215c3f3c9deda644058a616bc/movie_metadata.csv")
print("Tabela com os dados dos filmes")
print(imdb.head())

print("Cores únicas:?")
print(imdb["color"].unique())

print("Quantas vezes cada cor aparece:")
print(imdb["color"].value_counts())

print("Exibir percentual de participação percentual % de cada cor no total")
print(imdb["color"].value_counts(normalize=True))

print("Quantas vezes aparece cada diretor:")
print(imdb["director_name"].value_counts())

print("menor nota na crítica: ")
print(imdb["num_critic_for_reviews"].min())

print("Gráfico Histograma de notas: ")
imdb["num_critic_for_reviews"].hist()
plt.show

print("Gráfico Histograma de Faturamento")
#imdb["gross"].plot(kind='hist')
imdb["gross"].hist()
plt.show()

print("Gráfico displot do faturamento")
sns.distplot(imdb["gross"])
plt.show()

print("Filmes ordenados por maior faturamento")
print(imdb.sort_values("gross", ascending=False).head())


#Verificar qtd de linhas
color_or_bw = imdb.query("color in ['Color', ' Black and White']")
print(len(color_or_bw))

#Criar nova coluna atribuindo 0 ou 1 para identificar se filme é colorido ou preto e branco
color_or_bw["color_0_ou_1"] = (color_or_bw["color"]=="Color") * 1
print("Tabela com a nova coluna color_0_ou_1")
print(color_or_bw.head())

print("Qtd de Filmes colorido e preto e branco")
print(color_or_bw["color_0_ou_1"].value_counts())

print("Gráfico para comparar que tipo de filme fatura mais(colorido - 1 ou preto e branco = 0)")
sns.scatterplot(data=color_or_bw, x='color_0_ou_1', y='gross')
plt.show()

print("Média de faturamento de filmes coloridos e preto e branco")
print(color_or_bw.groupby("color").mean())

print("Média de notas de filmes coloridos e preto e branco")
print(color_or_bw.groupby("color").mean()["imdb_score"])

print("Coluna Orçamento e Faturamento")
budget_gross = imdb[["budget", "gross"]]
print(budget_gross)

print("Qqd de linhas sem remover valores Nan")
print(len(budget_gross))

print('Gráfico budget x gross removendo linhas com valores NaN ou 0')
budget_gross.dropna().query("budget >0 | gross > 0")
sns.scatterplot(x='budget', y='gross', data= budget_gross)
plt.show()

print("Filmes ordenados por maiores budgets")
print(imdb.sort_values("budget", ascending=False).head())

#Como os valores de budget estão nas moedas locais, vamos usar apenas os filmes americados que certamente estão em dólar
print("Código de país do filme")
print(imdb["country"].unique())

#Criando nova base de dados apenas com filmes do EUA
imdb = imdb.drop_duplicates() #remove linhas duplicadas
imdb_usa = imdb.query("country == 'USA'")
print("Filmes americanos")
print(imdb_usa.sort_values("budget", ascending=False).head())

#Plotar gráfico de relação entre budget x gross para filmes do EUA
budget_gross = imdb_usa[["budget", "gross"]].dropna().query("budget >0 | gross > 0")
print("Gráfico Filmes do EUA com budget x gross removendo linhas com valores NaN ou 0 ")
sns.scatterplot(x="budget", y="gross", data = budget_gross)
plt.show()

#Verificar lucro e prejuízo
imdb_usa['lucro'] = imdb_usa['gross'] - imdb_usa['budget']
budget_gross = imdb_usa.query("budget >0 | gross > 0")[["budget", "lucro"]].dropna()
print("Gráfico lucro x prejuízo")
sns.scatterplot(x="budget", y="lucro", data = budget_gross)
plt.show()

#Verificar Ano de lançamento e faturamento
#Feature Engeniering - criar uma feature a partir de outras duas
budget_gross = imdb_usa.query("budget >0 | gross > 0")[["title_year", "lucro"]].dropna()
sns.scatterplot(x="title_year", y="lucro", data = budget_gross)
print("Gráfico Ano e Faturamento")
plt.show()


filmes_por_diretor = imdb_usa["director_name"].value_counts()
gross_director = imdb_usa[["director_name", "gross"]].set_index("director_name").join(filmes_por_diretor, on="director_name")
gross_director.columns=["dindin", "filmes_irmaos"]
gross_director = gross_director.reset_index()
gross_director.head()
print("Gráfico filmes do mesmo diretor")
sns.scatterplot(x="filmes_irmaos", y="dindin", data = gross_director)
plt.show()

#Ver gráficos de variáveis tudo de uma vez só
sns.pairplot(data = imdb_usa[["gross", "budget", "lucro", "title_year"]])
plt.show()