# 1) Escreva um programa que leia a idade de 10 pessoas e armazene-as numa lista. Calcule e mostre:
# a) a menor idade
# b) a média das idades
# c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
# d) a quantidade de pessoas com idade maior que a média

idades = []
menoridade = 0
# lista para armazenar as pessoas com idades entre 20 e 30 anos
vintetrinta = []
# lista para armazenar as pessoas com idade acima da media do intervalo
maiorqmedia = []
x = 0
# lista que recebe as idades e depois transfere para a lista "idades" principal
leridade = []

while x < 10:
    # a identifica a menor idade
    menoridade = min(idades)
    leridade = int(input("Informe as idades dessas 10 pessoas: "))
    idades.append(leridade)
    # c verifica se a idade de cada um dos pontos da lista está entre o intervalo 20~30
    if leridade > 19 and leridade < 31:
        vintetrinta.append(leridade)
        x += 1

# b calcula a media das idades
media = sum(idades)/len(idades)
a = 0
while a < 10:
    # d identifica se a idade de cada um dos pontos da lista é maior que a media ou nao
    if idades[a] > media:
        b = idades[a]
        maiorqmedia.append(b)
    a += 1
       
print("A menor idade é: ", menoridade)
print("A média das idades é: ", media)
print("A quantidade de pessoas com idade entre 20 e 30 anos é: ", len(vintetrinta))
print("A quantidade de pessoas com idade acima da média é: ", len(maiorqmedia))
