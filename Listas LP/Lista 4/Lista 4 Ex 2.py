#2=Faça um programa que receba 2 números inteiros e o usuário digite na tela a operação
#que deseja realizar: 1- soma, 2- subtração, 3- multiplicação e 4-divisão. Crie cada uma
#dessas operações em funções que recebam os números e retorne o resultado para o
#programa principal.

n1=int(input("Digite o primeiro número inteiro: "))
n2=int(input("Digite o segundo número inteiro: "))

op=int(input("Digite a operação que deseja realizar. 1 = Soma, 2 = Subtração, 3 = Multiplicação, 4 = Divisão. "))

result=0

if op == 1:
    result=n1+n2 #soma

if op == 2:
    result=n1-n2 #subtração

if op == 3:
    result=n1*n2 #multiplicação

if op == 4:
    result=n1/n2 #divisão

print("O resultado da sua operação é: ", result)
