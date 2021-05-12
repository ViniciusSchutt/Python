#Exercício 5) Faça um programa que preencha uma lista com os nomes de 5 produtos, e outra lista com o valor dos produtos. Calcule e mostre:
#a. a quantidade de produtos que o valor é abaixo de 10 reais;
#b. a média dos valores dos produtos;
#c. a quantidade de produtos que valor acima da média;
#d. a maior valor e o nome do produto;
#e. faça uma listagem que imprima na tela (Nome Vlr do produto)

nomes=[]
valores=[]
abaixode10=[]
acimadamedia=[]
nomeevalor=[]
maiorvalor=[]
x=0

while x<5:
    listanomes=str(input("Digite os nomes dos produtos: "))
    nomes.append(listanomes)
    nomeevalor.append(listanomes)
    listavalores=float(input("Digite os valores dos produtos: "))
    valores.append(listavalores)
    nomeevalor.append(listavalores)
    if listavalores<10 and listavalores>0: #a
        abaixode10.append(valores)
    if listavalores == max(valores): #d
        maiorvalor=listavalores
        prod=listanomes
    x+=1

x=0

media=(sum(valores)/len(valores)) #b
contador=len(valores)

while x<contador: #c
    if valores[x] > media: 
        a=valores[x]
        acimadamedia.append(a)
    x+=1


print("A quantidade de produtos com valor abaixo de 10 é: ", len(abaixode10))
print("A média dos valores dos produtos é: ", media)
print("A quantidade de produtos com valor acima da média: ", len(acimadamedia))
print("O maior valor: ", maiorvalor, "E o nome do produto: ", prod)
print("Nomes dos produtos: ", nomes, "Valor dos produtos: ", valores) #e



    
