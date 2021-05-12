matriz=[[],[],[]]
f_range_1525=[] #quantidade de filhos das pessoas entre 15 e 25 anos
s_range_2030=[] #média salarial das pessoas entre 20 e 30 anos
x=0
while x<10:
    salario=float(input("Informe o salário: "))
    idade=int(input("informe a idade: "))
    filhos=int(input("Quantidade de filhos: "))
    if idade>=15 and idade<=25:
        f_range_1525.append(filhos)
    if idade>=20 and idade<=30:
        s_range_2030.append(salario)
    matriz[0].append(salario)
    matriz[1].append(idade)
    matriz[2].append(filhos)
    x+=1
print("Média salarial da população: ",sum(matriz[0])/len(matriz[0]))
print("Média de filhos: ",sum(matriz[2])/len(matriz[2]))
print("Qtd filhos de pessoas entre 15 e 25 anos: ",sum(f_range_1525))
print("Média salarial (20 a 30 anos): ",sum(s_range_2030)/len(s_range_2030))
