#Escreva um programa que preencha uma matriz 4 x 6 com números inteiros
#calcule e mostre na tela
#a) A quantidade de números que estão no intervalo entre 10 e 30
#b) A soma dos números maiores que 10
#c) A soma dos números que estão na quarta coluna da matriz
#d) A média dos números da matriz que estão na terceira linha

mtz=[[],[],[],[]] #criação da matriz
A_intervalo=[] #matriz que comportará o intervalo entre 10 e 30
B_dezmais=[] #para os números maiores que 10
C_soma=[] #soma dos números da quarta coluna

y=0
while y<4:
    x=0
    while x<6:
        num=int(input('informe um número: ')) #solicita que o usuário preencha os números da matriz inteira
        mtz[y].append(num)
        if n<=29 and n>=11: #se a condição do número ser menor ou igual a 29 e maior ou igual a 11, ele entra na lista desse intervalo
            A_intervalo.append(num)
        if n>10: #se o número for maior que 10, é adicionado na lista acima de 10
            B_dezmais.append(num)
        x+=1
    y+=1
x=0
while x<4: 
    d=mtz[x][3] #roda até adicionar todos os números da quarta coluna na lista C_soma, que será impressa usando o comando sum direto no print
    C_soma.append(d)
    x+=1
    
somal3=sum(mtz[2]) #soma dos números da linha 3
tamanhol3=len(mtz[2]) #quantidade de números na linha 3
medialinha3=somal3/tamanhol3 #média desses números
print('Matriz: ', mtz)
print('Números no intervalo entre 10 e 30: ', A_intervalo)
print('Números maiores que 10: ', B_dezmais)
print('Soma dos nº na 4ª coluna: ', sum(C_soma))
print('Média dos números na 3ª linha: ', medialinha3)
