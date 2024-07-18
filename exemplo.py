import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from tkinter import filedialog

def carregar_seaborn():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    plt.figure(figesize=(10,6))
    sns.barplot(x='mes', y='vendas', data=df)
    plt.show()

    

def carregar_3d():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(df['Vendedor'], df['Vendas'], df['Mês'])
    ax.set_title('teste')
    ax.set_xlabel('Vendas')
    ax.set_ylabel('Vendedor')
    plt.show()

carregar_3d()
