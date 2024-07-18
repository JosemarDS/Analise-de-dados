import pandas as pd

# Exemplo de DataFrame
dados_vendas = pd.DataFrame({
    'Data': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Vendedor': ['Ana', 'Pedro', 'Carla'],
    'Produto': ['Caneta', 'Lápis', 'Borracha'],
    'Quantidade': [10, 20, 15],
    'Valor': [2.5, 1.2, 1.0]
})


caminho_arquivo = 'vendas_exportadas.csv'
dados_vendas.to_csv(caminho_arquivo, index=False)

caminho_excel = 'dados1.xlsx'
dados_vendas.to_excel(caminho_excel, index= False)
