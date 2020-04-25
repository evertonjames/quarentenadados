from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#setando a precisão de casas decimais que o pandas irá exibir os dados
(pd.options.display.float_format)
#%precision %.2f
pd.options.display.float_format = '{:,.2f}'.format
#Config para exibir todas as colunas no terminal ao fazer print da tabela
pd.set_option('display.expand_frame_repr', False)

#uri = "https://github.com/guilhermesilveira/enem-2018/blob/master/MICRODADOS_ENEM_2018_SAMPLE_43278.csv?raw=true"
uri = "C:\\Users\\evert\\PycharmProjects\\quarentenadados\\datasets\\MICRODADOS_ENEM_2018_SAMPLE_43278.csv"
dados = pd.read_csv(uri)
print("Tabela de dados ENEM 2018")
print(dados.head())

#o describe só gera informação de dados numéricos
print("descrição das colunas")
print(dados.describe())

#temos alguns dados relevantes: notas das provas e redação.
#criar tabela apenas com colunas de notas
colunas_de_notas = ['NU_NOTA_CN','NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT','NU_NOTA_REDACAO']
dados_notas = dados[colunas_de_notas].dropna()
dados_notas.columns = ['ciencias_naturais', 'ciencias_humanas', 'linguagem_codigo', 'matematica', 'redacao']
print("Tabela com notas do ENEM 2018")
print(dados_notas.head())

print("Quantidade de linhas na tabela de dados_notas")
print(len(dados_notas))

#Calcular a correlação usando o .corr():
corr = dados_notas.corr()
print("Correlação entre as colunas de notas")
print(corr)

# gráficos para visualizar a correlação de uma melhor forma
# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=np.bool))
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()

#Gráfico de mapa de calor
print("Gráfico de mapa de calor")
sns.heatmap(corr)
plt.show()

#gráfico de correlação entre as notas
sns.pairplot(dados_notas)
plt.show()
