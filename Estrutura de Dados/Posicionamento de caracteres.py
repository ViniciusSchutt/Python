tamanho = int(3)
indice = int(1)
palavras = [None] * 10

def ordena():

    for indice in range(tamanho - 1):  # compara indice zero com um, depois um com dois
        if (palavras[indice] > palavras[indice + 1]):
            palavras[indice] = palavras[indice + 1]
            palavras[indice + 1] = palavras[indice]
            print(f'{palavras[indice]}')


def insere():
    for indice in range(0, tamanho):  # qual será o limite da leitura
        palavras.insert(indice, str(input("Digite uma palavra: ")))  # insira no vetor, no indice uma string


def exibe():
    for indice in range(0, 3):
        print("O valor no indice %i" % indice, " é: %s" % palavras[indice])

insere()
print("Exibe vetor desordenado")
exibe()

ordena()
print("Exibe vetor ordenado")
exibe()


