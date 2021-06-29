# Faça um programa que preencha uma matriz de ordem 3 x 5 de elementos inteiros.
# Crie uma função que receba essa matriz por parâmetro e faça os seguintes cálculos:
# a) o maior elemento da matriz;
# b) a média dos elementos da matriz;
# c) altere os números da matriz, multiplicando cada elemento pelo maior número;
# d) a média e o maior número devem ser impressos dentro da função;
# e) No programa principal imprima a nova matriz, após a finalização da execução da função.

from random import randint

matA = []
matB = []
matC = []
altA = []  # Matriz A alterada
altB = []  # ------ B --------
altC = []  # ------ C --------
x = 0

while x < 3:
    y = 0
    a = randint(0, 100)
    matA.append(a)
    x = x+1
    while y < 5:
        b = randint(0, 100)
        matB.append(b)
        y = y+1
    
        matC.append(a+b)
        maior = max(matC)  # a
        altA = a*maior
        altB = b*maior
        altC.append(altA+altB)  # c
        media = 0
        soma = sum(matA)+sum(matB)
        comp = len(matA)+len(matB)  # b
        media = soma/comp
        
print(f"A média dos elementos da matriz é: {media}")  # d
print(f"O maior número da matriz é: {maior}")

print(f"Matriz original: {matC}")
print(f"Matriz final: {altC}")  # e




