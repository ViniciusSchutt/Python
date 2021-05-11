#crie um algoritmo que receba vários números inteiros positivos e imprima o produto dos números ímpares
#e a soma dos números pares digitados

soma=0
produto=1

n=int(input("Informe um número positivo, zero ou negativo para terminar: \n"))

while n>0:
    if n%2 == 0:
        soma = soma + n
    else:
        produto = produto * n
    n=int(input("Informe um número positivo, zero ou negativo para terminar: \n"))
print("Soma dos números pares: ", soma)
print("Produto dos números impares: ", produto)
