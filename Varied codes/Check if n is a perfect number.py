# 1 = Crie uma função que receba 1 número inteiro como parâmetro e verifique se ele é
# perfeito, ou seja, se a soma dos seus divisores exceto ele mesmo dá o próprio número,
# a mensagem se o número é perfeito ou não deve ser mostrada no programa principal

n = int(input("Enter any int number: "))

sum = 0  # esse parâmetro vai receber a soma de todos os divisores du número para testar se ele é perfeito
divider = 1
for divider in range(1, n):  # divisor começa em 1 porque tem que ser > 0, e vai contar todos até chegar a n
    if n % divider == 0:
        sum += divider

if n == sum:
    print("The number is perfect.")
else: 
    print("The number isn't perfect.")
