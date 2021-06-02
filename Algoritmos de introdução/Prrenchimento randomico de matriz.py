"""
Escreva um programa que preencha uma matrizde ordem 5x5 de elementos inteiros
e mostre na tela a matriz preenchida (2pts)
Calcule e mostre na tela:
A média dos números da diagonal principal da matriz; (1,5 pts)
O menor número da coluna 2, ou seja, índice 1: (1,5 pts)
A média dos números da 4ª linha da matriz, ou seja, índice 3; (1,5 pts)
A quantidade de números da matriz q sao >= 10 e <= 25; (1,5 pts)
Faça a média de cada coluna da matriz e armazene em uma lista; (1,5 pts)
"""

from random import randint

matriz = [[], [], [], [], []]
i = 0
while i < 5:
   j = 0
   while j < 5:
       a = randint(0, 25)
       matriz[i].append(a)
       j += 1
   i += 1

dgl = []
med_col = [[], [], [], [], []]
i = 0
j = 0
while i < 5:
    dgl.append(matriz[i][j])
    i += 1
    j += 1
i = 0
smaller = matriz[i][1]
while i < 5:
    if matriz[i][1] < smaller:
        smaller = matriz[i][1]
    i += 1
i = 0
amount = 0
while i < 5:
    j = 0
    while j < 5:
        if matriz[i][j] >= 10:
            amount = amount + 1
        elif matriz[i][j] <= 25:
            amount = amount+1
        j = j + 1
    i = i + 1
i = 0
while i < 5:
    j = 0
    while j < 5:
        med_col[i].append(matriz[j][i])
        j = j + 1
    i = i + 1
print(matriz) # "Mostre na tela a matriz preenchida
print("A média dos números da diagonal principal da matriz é: ", sum(dgl)/len(dgl))
print("O menor número da 2ª coluna da matriz é: ", smaller)
print("A média dos números da 4ª linha da matriz é: ", sum(matriz[3])/len(matriz[3]))
print("A quantidade de números da matriz que estãi entre 10 e 25 é: ",amount)
print("Média da 1ª coluna: ", sum(med_col[0])/len(med_col[0]))
print("Média da 2ª Coluna: ", sum(med_col[1])/len(med_col[1]))
print("Média da 3ª Coluna: ", sum(med_col[2])/len(med_col[2]))
print("Média da 4ª Coluna: ", sum(med_col[3])/len(med_col[3]))
print("Média da 5ª Coluna: ", sum(med_col[4])/len(med_col[4]))


        
