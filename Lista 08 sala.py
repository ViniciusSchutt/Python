
def funcoesSimples():
     print("Informe uma frase qualquer: ")
     nome = str(input())

     print("A frase informada foi:", nome)
     qtdchar = len(nome)

     frase = nome
     frase.split(" ")
     qtdpalavras = 1
     nespacos = 0
     for i in range(len(nome)):
        if frase[i].isspace():
            qtdpalavras = qtdpalavras + 1
            nespacos = nespacos + 1
     print(qtdpalavras)
     print(nespacos)

     qtdchar = qtdchar - nespacos
     nvogais = 0
     nconsoantes = 0
     qta, qte, qti, qto, qtu = 0, 0, 0, 0, 0

     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     alphabet.split(" ")
     frasecifrada = []

     for i in range(len(nome)):
         if nome[i] == 'a' or nome[i] == 'e' or nome[i] == 'i' or nome[i] == 'o' or nome[i] == 'u':
             nome=alphabet
             frasecifrada.append(nome[i + 3])
         elif nome[i] == ' ':
             nome=alphabet
             frasecifrada.append(nome[i])
         elif nome[i] == 'b' or nome[i] == 'c' or nome[i] == 'd' or nome[i] == 'f':
             nome=alphabet
             frasecifrada.append(nome[i - 6 + 26])
         else:
             nome=alphabet
             frasecifrada.append(nome[i - 6])

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
     print(f"A quantidade de vogais que se repetem são: A={qta} E={qte} I={qti} O={qto} U={qtu}")
     print(f"A frase normal eh: '{nome}' e a frase cifrada eh: '{''.join(frasecifrada)}'")


funcoesSimples()
