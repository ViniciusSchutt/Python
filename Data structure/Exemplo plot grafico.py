# Primeiro exemplo de como plotar gráficos no Python
import pandas as pd
import matplotlib.pyplot as plt # na biblioteca matplotlib, usaremos a classe pyplot para fazer o gráfico

dataFrame = pd.read_csv(r"C:\Users\vinic\Downloads\arqExcel.csv", delimiter=";")
# através da biblioteca pandas estamos chamando read para ler arquivos do tipo csv

print(dataFrame) # simplesmente printa o arquivo csv selecionado
print(dataFrame.tail(2))
print(dataFrame["produto"])
print(dataFrame["tipo"].unique())
print(dataFrame[(dataFrame["tipo"] == "Bebida") & (dataFrame["qtd"] < 15)])

"""
plt.xlabel("produto")
plt.ylabel("valor")
plt.bar(dataFrame.head(6)["produto"], dataFrame.head(6)["valor"])
plt.show()"""

