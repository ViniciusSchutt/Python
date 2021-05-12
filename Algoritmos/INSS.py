
#o desconto do INSS segundo a tabela a seguir:
#Menor ou igual a R$ 600,00 - isento
#Maior que R$ 600,00 e menor ou igual a R$ 1200,00 – 20%
#Maior que R$1200,00 e menor ou igual a R$ 2000,00 – 25%
#Maior que R$ 2000,00 – 30%

salario=int(input("Informe o valor do seu salário: "))

if salario>600 and salario <=1200:
    desconto=salario*0.2
    print("O desconto do seu INSS é de: ", desconto)

if salario>1200 and salario<=2000:
    desconto=salario*0.25
    print("O desconto do seu INSS é de: ", desconto)

if salario>2000:
    desconto=salario*0.3
    print("O desconto do seu INSS é de: ", desconto)

else:
    print("Você é isento do desconto!")

