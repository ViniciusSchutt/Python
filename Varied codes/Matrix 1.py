# Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros,
# calcule e mostre na tela:
# a) menor número da matriz;
# b) soma dos números múltiplos de 3 da matriz;
# c) média dos números da matriz;

m = [[10, 22, 42, 1, 3], [90, 24, 75, 12, 10], [88, 11, 64, 23, 15]]
x = 0
z = 0
while x < 3:
    while z < 5:
        if m[x][z] <= 1:
            menor = m[x][z]
        z += 1
    x += 1

x = 0
mt = []
while x < 3:
    z = 0
    while z < 5:
        if m[x][z] % 3 == 0:
            mt.append(m[x][z]) 
        z += 1
    x += 1  # soma dos números múltiplos de 3

med = []
x = 0
while x < 3:
    med.append(sum(m[x]))
    x += 1
soma = sum(med)
x = 0
pos = []
while x < 3:
    pos.append(len(m[x]))
    x += 1
div = sum(pos)
print("O menor número da matriz é: ", menor)
print("A soma dos números múltiplos de 3 da matriz é: ", sum(mt))
print("A média dos números da matriz é: ", soma/div)
