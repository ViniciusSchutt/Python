#2) Faça um programa que preencha uma lista com 10 cores diferentes. Depois permita fazer
#uma pesquisa se uma determinada cor existe armazenada na lista, se existir deve ser
#impresso na tela a cor e em qual posição (índice) esta cor está armazenada. A pesquisa
#deve ser feita até que seja digitado FIM na cor a ser pesquisada na lista.

cor=['vermelho','azul','amarelo','verde','roxo','branco','preto','laranja','bege','marrom']
n=1
print('Busque pelas cores na lista (digite FIM para encerrar)')
while n>0:
    n=1
    pesq = str(input('Busca de cores: '))
    if pesq in cor:
        print('A cor ', pesq, 'está presente na posição ',cor.index(pesq))
    if pesq == "FIM":
        n=0
    if pesq not in cor:
        print('A cor informada não está na lista.')
print('O programa foi encerrado.')






