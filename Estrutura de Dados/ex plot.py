import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("C:\\Users\\vinic\Downloads\\arqExcel.csv", delimiter=";")

#print(dataFrame)

print(dataFrame.tail(2))
print(dataFrame["produto"])
print(dataFrame["tipo"].unique())
print(dataFrame[(dataFrame["tipo"]=="Bebida") & (dataFrame["qtd"]<15)])
plt.xlabel("produto")
plt.ylabel("valor")
plt.bar(dataFrame.head(6)["produto"], dataFrame.head(6)["valor"])
plt.show()