# O programa preenche uma lista com 10 cores diferentes. Depois, permite
# pesquisar se uma determinada cor existe armazenada na lista, e se existir,
# imprime a cor e em qual posição (índice) esta cor está armazenada. A pesquisa
# continua até que seja digitado FIM na cor a ser pesquisada na lista.

cor = ['vermelho', 'azul', 'amarelo', 'verde', 'roxo', 'branco', 'preto', 'laranja', 'bege', 'marrom']
n = 1
print('Busque pelas cores na lista (digite FIM para encerrar)')
while n > 0:
    n = 1
    pesq = str(input('Busca de cores: '))
    if pesq in cor:
        print('A cor ', pesq, 'está presente na posição ', cor.index(pesq))
    if pesq == "FIM":
        n = 0
    if pesq not in cor:
        print('A cor informada não está na lista.')
print('O programa foi encerrado.')






