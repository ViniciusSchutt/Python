#1) Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma lista. Calcule e mostre:
#a) a menor idade
#b) a média das idades
#c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
#d) a quantidade de pessoas com idade maior que a média

idades=[] #lista com as idades
menoridade=0 
vintetrinta=[] #lista para armazenar as pessoas com idades entre 20 e 30 anos
maiorqmedia=[] #lista para armazenar as pessoas com idade acima da media do intervalo
x=0 #contador inicializado em 0
leridade=[] #lista que recebe as idades e depois transfere para a lista "idades" principal

while x<10:
    leridade=int(input("Informe as idades dessas 10 pessoas: "))
    idades.append(leridade)
    if leridade>19 and leridade<31: #c verifica se a idade de cada um dos pontos da lista está entre o intervalo 20~30
        vintetrinta.append(leridade)
    x+=1

menoridade=min(idades) #a identifica a menor idade
media=sum(idades)/len(idades) #b calcula a media das idades
a=0
while a<10:
    if idades[a] > media: #d identifica se a idade de cada um dos pontos da lista é maior que a media ou nao
        b=idades[a]
        maiorqmedia.append(b)
    a+=1
       
print("A menor idade é: ", menoridade)
print("A média das idades é: ", media)
print("A quantidade de pessoas com idade entre 20 e 30 anos é: ", len(vintetrinta))
print("A quantidade de pessoas com idade acima da média é: ", len(maiorqmedia))
        

