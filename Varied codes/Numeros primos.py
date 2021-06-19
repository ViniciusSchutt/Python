# Faça um programa que receba dez números inteiros. Calcule e mostre:
# A soma dos números primos
# A média dos números múltiplos de 3 que são maiores que 10

qtd = 0
qtd1 = 0
soma = 0
soma1 = 0

for i in range(10):
    num = int(input("Escreva um número: "))
    qtd = 0
    for i in range(1, num+1):
        if num % i == 0:
            qtd = qtd + 1
    if qtd == 2:
        soma = soma+num
    if num % 3 == 0 and num > 10:
        qtd1 = qtd1+1
        soma1 = soma1+num

print("Soma dos numeros primos: ", soma)
print("A media dos numeros multiplos de 3 que são maiores que 10:", soma1/qtd1)
