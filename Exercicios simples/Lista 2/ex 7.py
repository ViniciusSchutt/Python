#7)Escreva um programa que gere uma lista que é resultado do produto de duas listas L1 e
#L2. Mostre na tela as 3 listas.

lista1=[]
lista2=[]
x=1
for i in range(3):
    lista1.append(int(input('Insira um número na lista 1: ')))
    lista2.append(int(input('Insira um número na lista 2: ')))

C=[]
for i in range(3):
    C.append(lista1[i]*lista2[i])

print(lista1)
print(lista2)
print(C)
