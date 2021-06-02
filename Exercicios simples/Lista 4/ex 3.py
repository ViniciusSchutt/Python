#3= Um time de basquete possui 12 jogadores. Faça um programa que preencha uma
#matriz com o nome e a altura dos jogadores, e através de uma função faça os
#seguintes cálculos:
#a. o nome e a altura do jogador mais alto
#b. a média de altura do time

time=[]
nome=[]
alt=[]
x=0
i=0

while x<12:
    y=0
    n=str(input("Digite o nome do jogador: "))
    nome.append(n)
    while y<1:
        a=int(input("Digite a altura do jogador: "))
        alt.append(a)
        if alt[i]==max(alt):
            highest=nome[i]
        x=x+1
        y=y+1

time.append(nome+alt)

a=max(alt)
media=sum(alt)/len(alt)

print(time)
print("O nome do jogador mais alto é: ", highest, "E sua altura é: ", a)
print("A média de altura do time é: ", media)
