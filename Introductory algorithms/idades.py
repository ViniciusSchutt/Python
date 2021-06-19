#Receber a idade de uma pessoa e informar se:

#-é maior de idade
#-é menor de idade
#-tem 60 anos ou mais – Melhor idade

idade=int(input("Informe a idade: "))

if idade >= 18 and idade <= 59:
    print("Maior de idade")

if idade>60:
    print("Melhor idade")

else:
    print("Menor de idade")


