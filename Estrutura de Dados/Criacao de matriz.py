"""
Partindo do princípio que receberá sempre um tamanho “quadrado”, esse código desenha e
printa uma tela onde as bordas laterais contém o símbolo do pipe “|”, as bordas superiores
e inferiores, um traço "-" e as diagonais da direita para a esquerda e da esquerda para a
direita, a letra “X”, independentemente do tamanho do quadrado, como no desenho abaixo:

entrada = 4
        ----
saída = |XX|
        |XX|
        ----
"""

tam = int(input("Digite o tamanho do quadrado, o tamanho deve estar entre 3 e 40: "))

if 3 <= tam <= 40: #se a entrada do usuário atender a requisição de tamanho entre 3 e 40, faça:
    
    lista = [None] * tam
    bordasuperior = []
    bordainferior = []
    central = []
    i = 0
    fim = len(lista) -1

    def preenche(): #função que preenche a matriz
        for i in range(len(lista)):
            bordasuperior.append('-')
            bordainferior.append('-')
            if i == 0:
                central.append('|')
            if i == fim:
                central.append('|')
            if i != 0 and i != fim:
                central.append('X')

    def define(): #função que define a matriz de acordo com seu tamanho, basicamente diferenciando entre matrizes de tamanho 3 ou maiores
        if tam == 3:
            bs=''.join(bordasuperior) #bs é uma abreviação para Borda Superior
            cent=''.join(central) #cent é uma abreviação para central, da linha central da matriz
            bi=''.join(bordainferior) #bi é uma abreviação para Borda Inferior

            print(bs)
            print(cent)
            print(bi)

        if tam > 3:
            bs = ''.join(bordasuperior)
            cent = ''.join(central)
            bi = ''.join(bordainferior)
            print(bs)
            for i in range(len(lista)):
                if i != 0 and i != fim: #enquanto i não for correnpondente a primeira e última linhas da matriz
                    print(cent) #imprima a linha central
            print(bi)

    preenche()
    define()

else:
    print("Tamanho inválido.") #caso o tamanho informado pelo usuário não esteja no intervalo 3 <= tam <= 40, imprime "Tamanho inválido".