#1=Crie uma função que receba 1 número inteiro como parâmetro e verifique se ele é
#perfeito, ou seja, se a soma dos seus divisores exceto ele mesmo dá o próprio número,
#a mensagem se o número é perfeito ou não deve ser mostrada no programa principal

n=int(input("Digite um número inteiro qualquer: "))

soma = 0 #esse parâmetro vai receber a soma de todos os divisores du número para testar se ele é perfeito
divisor = 1
for divisor in range(1,n): #divisor começa em 1 porque tem que ser > 0, e vai contar todos até chegar a n
    if n % divisor == 0:
            soma += divisor 

if n == soma:
    print("O numero é perfeito.")
else: 
    print("O numero não é perfeito.")
      
