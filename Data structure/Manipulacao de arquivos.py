# Primeiro exemplo de manipulação de arquivos

vetor=['Linha01\n', 'Linha02\n', 'Linha03\n']


def criaarquivo():
    arquivo = open('C:\\Users\\vinic\\AppData\\Local\\Temp\\arqTeste.txt', 'w')
    arquivo.write(str("Linha01\n"))
    arquivo.write(str("Linha02\n"))
    arquivo.write(str("Linha03\n"))
    print("Arquivo criado")
    arquivo.close()
"""

def criaarquivocomvetor():
    arquivo = open('C:\\Users\\vinic\\AppData\\Local\\Temp\\arqTeste.txt', 'w')
    arquivo.writelines(vetor)
    print("Arquivo criado")
    arquivo.close()

def criaarquivoalteralinhas():
    arquivo = open('C:\\Users\\vinic\\AppData\\Local\\Temp\\arqTeste.txt', 'r+')
    arquivo.seek(8)
    arquivo.write(str(chr(9)+"Linha nova"))
    print("Arquivo alterado a partir do byte 8")
    arquivo.close()

criaarquivocomvetor()
criaarquivoalteralinhas()
"""

arquivo = open('C:\\Users\\vinic\\AppData\\Local\\Temp\\arqTeste.txt', 'r')

def carregatodooarquivo():
    print("Leitura de todo o arquivo posicionado no inicio do arquivo: %s" %arquivo.tell())
    print(arquivo.read())
"""
def carregaarquivoapartirde():
    arquivo.seek(10)
    print("Leitura de todo o arquivo a partir do byte 10: %s" %arquivo.tell())
    print(arquivo.read())
"""
def carregaarquivoateofim():
    lista=[]
    print("Lendo varias linhas e armazenando numa lista")
    for linha in arquivo:
        lista.append(linha)
    arquivo.close()
    print("Exibe linha 2: %s" %lista[1])
    print("Exibe linha 3: %s" % lista[2])

criaarquivo()
carregaarquivoateofim()