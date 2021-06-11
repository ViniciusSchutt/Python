"""
O programa recebe uma frase qualquer e retorna vários dados a respeito dela,
como a quantidade de letras da frase, o número de vogais e consoantes, a quantidade
de palavras da frase, a quantidade de vogais que se repetem e a frase em forma
cifrada.
"""
print("Informe uma frase qualquer: ")
nome = str(input())

def funcoesSimples():
     print("A frase informada foi:", nome)
     qtdchar = len(nome) #quantidade de caracteres

     frase = nome
     frase.split(" ")
     qtdpalavras = 1 #quantidade de palavras
     nespacos = 0 #numero de espaços
     for i in range(len(nome)):
        if frase[i].isspace():
            qtdpalavras = qtdpalavras + 1
            nespacos = nespacos + 1

     qtdchar = qtdchar - nespacos
     nvogais = 0 #número de vogais
     nconsoantes = 0 #número de consoantes
     qta, qte, qti, qto, qtu = 0, 0, 0, 0, 0 #qts são variáveis para armazenar a quantidade de vogais

     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     alphabet.split(" ")
     frasecifrada = []

     for i in range(len(nome)):
         if nome[i] == 'a' or nome[i] == 'e' or nome[i] == 'i' or nome[i] == 'o' or nome[i] == 'u':
             letra = nome[i]
             if letra in alphabet:
                 pos = alphabet.index(letra)
                 frasecifrada.append(alphabet[pos + 3])

         elif nome[i] == ' ':
             frasecifrada.append(' ')

         elif nome[i] == 'b' or nome[i] == 'c' or nome[i] == 'd' or nome[i] == 'f':
             letra = nome[i]
             if letra in alphabet:
                 pos = alphabet.index(letra)  #pos se refere ao índice da letra no alfabeto
                 frasecifrada.append(alphabet[pos - 6 + 26])
         else:
             letra = nome[i]
             if letra in alphabet:
                 pos = alphabet.index(letra)
                 frasecifrada.append(alphabet[pos - 6])

     for i in range(len(nome)):
        if frase[i] == 'A' or frase[i] == 'a':
            nvogais = nvogais + 1
            qta = qta + 1
        elif frase[i] == 'E' or frase[i] == 'e':
            nvogais = nvogais + 1
            qte = qte + 1
        elif frase[i] == 'I' or frase[i] == 'i':
            nvogais = nvogais + 1
            qti = qti + 1
        elif frase[i] == 'O' or frase[i] == 'o':
            nvogais = nvogais + 1
            qto = qto + 1
        elif frase[i] == 'U' or frase[i] == 'u':
            nvogais = nvogais + 1
            qtu = qtu + 1
        else:
            nconsoantes = nconsoantes + 1

     nconsoantes = nconsoantes - nespacos
     print("A qtd de letras é %i" % qtdchar)
     print("O numero de vogais eh: ", nvogais)
     print("O numero de consoantes eh: ", nconsoantes)
     print("A quantidade de palavras eh: ", qtdpalavras)
     print(f"A quantidade de vogais que se repetem eh: A={qta} E={qte} I={qti} O={qto} U={qtu}")
     print(f"A frase normal eh: '{''.join(nome)}' e a frase cifrada eh: '{''.join(frasecifrada)}'")

funcoesSimples()


