soma = 0
tot = 0
soma_Impar = cont = 0
soma_Par = 0 

for c in range(0, 10):
    numero = int(input("Digite um número: "))

    if numero % 2 != 0:
        soma_Impar += numero

    if numero % 2 == 0:
        cont += 1
        soma_Par += numero

    for d in range(1, numero + 1):
        if numero % d == 0:
            soma += 1

    if soma == 2 or numero == 1:
        tot += 1
    soma = 0

media = soma_Par / cont
print(f'A quantidade de números primos é {tot}')
print(f'A soma dos números impares é: {soma_Impar}')
print(f'A média dos números pares é {media}')
