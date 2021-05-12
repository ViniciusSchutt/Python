"""
Partindo do princípio que você receberá sempre o tamanho desse “quadrado” desenhe uma tela onde
as bordas laterais deverão conter o símbolo do pipe “|”, as bordas superiores e inferiores deverão
conter um traço “-“ e as diagonais da direita para a esquerda e da esquerda para a direita deverão
conter a letra “X”, isso independentemente do tamanho do quadrado como no desenho abaixo

entrada 4 = saida ----|XX||XX|----
"""

tam = int(input("Digite o tamanho do quadrado, o tamanho deve estar entre 3 e 40: "))

if 3 <= tam <= 40:
    
    lista = [None] * tam
    bordasuperior = []
    bordainferior = []
    central = []
    i = 0
    fim = len(lista) -1

    def preenche():
        for i in range(len(lista)):
            bordasuperior.append('-')
            bordainferior.append('-')
            if i == 0:
                central.append('|')
            if i == fim:
                central.append('|')
            if i != 0 and i != fim:
                central.append('X')

    def define():
        if tam == 3:
            bs=''.join(bordasuperior)
            cent=''.join(central)
            bi=''.join(bordainferior)

            print(bs)
            print(cent)
            print(bi)

        if tam > 3:
            bs = ''.join(bordasuperior)
            cent = ''.join(central)
            bi = ''.join(bordainferior)
            print(bs)
            for i in range(len(lista)):
                if i != 0 and i != fim:
                    print(cent)
            print(bi)

    preenche()
    define()

else:
    print("Tamanho inválido.")