#faça um programa que simule um lançamento de dados. Lance os dados 10 vezes e armazene os dados em uma lista.
#depois, mostre quantas vezes cada valor foi conseguido.
#dica use um vetor de contadores (1 a 6) e uma função para gerar numeros aleatorios
#simulando o lancamento de dados

from random import randint
lista=[0] * 7
for i in range (10):
    n=randint(1,6)
    print("Numero: ", n)
    lista[n]=lista[n]+1

for i in range (1,7):
    print("Numero: ", i, "quantidade: ", lista[i])
