import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

dados = pd.read_csv('dados.csv')
print(dados)
x = dados['vendas']

plt.pie(x)
plt.show()