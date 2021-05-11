#Receber a idade de uma pessoa e informar:

#Se é maior de idade
#Se é menor de idade
#Se tem 60 anos ou mais – Melhor idade

idade=int(input("Informe a idade: "))

if idade>=18 and idade<=59:
    print("Maior de idade")

if idade>60:
    print("Melhor idade")

else:
    print("Menor de idade")


