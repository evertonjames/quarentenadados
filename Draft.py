import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")

imdb = pd.read_csv("https://gist.githubusercontent.com/guilhermesilveira/24e271e68afe8fd257911217b88b2e07/raw/e70287fb1dcaad4215c3f3c9deda644058a616bc/movie_metadata.csv")

print("Coluna Orçamento e Faturamento")
budget_gross = imdb[["budget", "gross"]]
#print(budget_gross)

print("Qqd de linhas sem remover valores Nan")
print(len(budget_gross))

print('Gráfico budget x gross removendo linhas com valores NaN ou 0')
budget_gross.dropna().query("budget >0 | gross > 0")
sns.scatterplot(x='budget', y='gross', data= budget_gross)
#plt.show()

#print("Filmes ordenados por maiores budgets")
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
#plt.show()

#Verificar lucro e prejuízo
imdb_usa['lucro'] = imdb_usa['gross'] - imdb_usa['budget']
budget_gross = imdb_usa.query("budget >0 | gross > 0")[["budget", "lucro"]].dropna()
print("Gráfico lucro x prejuízo")
sns.scatterplot(x="budget", y="lucro", data = budget_gross)
#plt.show()

#Verificar Ano de lançamento e faturamento
#Feature Engeniering - criar uma feature a partir de outras duas
budget_gross = imdb_usa.query("budget >0 | gross > 0")[["title_year", "lucro"]].dropna()
sns.scatterplot(x="title_year", y="lucro", data = budget_gross)
print("Gráfico Ano e Faturamento")
#plt.show()


filmes_por_diretor = imdb_usa["director_name"].value_counts()
gross_director = imdb_usa[["director_name", "gross"]].set_index("director_name").join(filmes_por_diretor, on="director_name")
gross_director.columns=["dindin", "filmes_irmaos"]
gross_director = gross_director.reset_index()
gross_director.head()
print("Gráfico filmes do mesmo diretor")
sns.scatterplot(x="filmes_irmaos", y="dindin", data = gross_director)
#plt.show()

#Ver gráficos de variáveis tudo de uma vez só
sns.pairplot(data = imdb_usa[["gross", "budget", "lucro", "title_year"]])
#plt.show()

#Ver correlação entre variáveis
#Quanto mais próximo de 1 maior a correlação
correlacao_imdb_usa = imdb_usa[["gross", "budget", "lucro", "title_year"]].corr()
print("Correlação entre gross, budget, lucro e title_year")
print(correlacao_imdb_usa)