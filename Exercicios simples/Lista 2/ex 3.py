#3)Faça um programa que preencha duas listas, lista A e lista B com 5 números em cada.
#Gere a lista C, com os números da lista A e lista B. Depois calcule e mostre na tela a
#quantidade de números perfeitos. Um número é perfeito quando ele é igual a soma dos
#seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus
#divisores).

listaA=[] #sem disclaimer
listaB=[] #//
listaC=[] #//
nperf=[]#números perfeitos
a=0
b=0
print("Cada lista será composta por cinco números. Informe os números da lista A: ")
while a<5:
    nsLA=int(input('Número: ')) #numeros lista A
    listaA.append(nsLA)
    listaC.append(nsLA)
    a+=1

print("Agora, informe os números para a lista B: ")
while b<5:
    nsLB=int(input('Número: ')) #numeros lista B
    listaB.append(nsLB)
    listaC.append(nsLB)
    b+=1
i=0
#d=1
for i in range(0,10):
    soma=0
    d=1
    while d<listaC[i]:
        if listaC[i]%d==0:
            soma += d
            if soma==listaC[i]:
                nperf.append(listaC[i])
        d+=1
    if d==listaC[i]:
            i+=1
print("A quantidade de números perfeitos é: ", len(nperf))
