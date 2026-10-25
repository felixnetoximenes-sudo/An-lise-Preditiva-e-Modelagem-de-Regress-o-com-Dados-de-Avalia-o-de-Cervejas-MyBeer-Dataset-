import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
tabela = pd.read_csv('my_beer.csv')
tabela.fillna(0)
tabela.drop_duplicates()
tabela = tabela.rename(columns={'beer_type': 'Bebidas'})
somando = tabela[['global_rating_score', 'global_weighted_rating_score']].sum()
X = tabela['global_rating_score'].to_numpy().reshape(-1, 1)
Y = tabela['global_weighted_rating_score'].to_numpy()



X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.03, random_state=42)

ia = LinearRegression()
ia.fit(X_train, Y_train)
previsao = ia.predict(X_test)
previ = mean_absolute_error(previsao, Y_test)
print (f'Precisao da ia {previ}')


