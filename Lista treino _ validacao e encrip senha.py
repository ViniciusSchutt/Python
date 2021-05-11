alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto.split(' ')
especiais = '!@#$%¨&*()_+-[{}]?/:;,´`='
especiais.split(' ')
numeros = '0123456789'
numeros.split(' ')
senha = str(input("Digite uma senha com no mínimo 25 e no máximo 30 chars: "))
senha.split(' ')
senhacifrada=[]

def validacao():
    quaosegura = len(senha)
    if 24 < quaosegura < 31:
        print('TESTE ZERO, please wait... Ok.')
    else:
        print('Quantidade de caracteres insuficiente, sem preguiça na próxima vez.')
        exit()

    teste1 = 0
    for i in range(3):
        if str.isupper(senha[i]):
            teste1 = teste1 + 1
        else:
            teste1 = teste1

    if teste1 >= 3:
        print('TESTE 1, please wait... Ok.')
    else:
        print('Senha inválida no primeiro teste, comece de novo.')
        exit()

    j = 6
    teste2 = 0
    for j in range (11):
        if str.islower(senha[j]):
            teste2 = teste2 + 1
        else:
            teste2 = teste2

    if teste2 >= 4:
        print('TESTE 2, plase wait... Ok. Tá indo bem, coragem seje ome!')
    else:
        print('Senha inválida no segundo teste, comece de novo.')
        exit()

    k = 12
    teste3 = 0
    for k in range(17):
        if senha[k] in numeros:
            teste3 = teste3 + 1
        else:
            teste3 = teste3

    if teste3 >= 3:
        print('TESTE 3, holy... Ok.')
    else:
        print('Senha inválida no terceiro teste, comece de novo.')
        exit()

    l = 18
    teste4 = 0
    for l in range(23):
        if senha[l] in especiais:
            teste4 = teste4 + 1
        else:
            teste4 = teste4

    if teste4 >= 3:
        print('TESTE 4!!!, please wait... "Zelda treasure song effect" e quase ia esquecendo, senha aprovada! ;)')
    else:
        print('Senha inválida no quarto teste, comece de novo.')
        exit()

def cifra():
    for i in range(len(senha)):
        letra = senha[i]
        if letra in alfabeto:
            pos = alfabeto.index(letra)
            senhacifrada.append(alfabeto[pos + 3])

        elif letra in numeros:
            pos = numeros.index(letra)
            senhacifrada.append(alfabeto[pos + 2])

        elif letra in especiais:
            pos = especiais.index(letra)
            senhacifrada.append(alfabeto[pos + 2])

    print(f"Sua senha original eh: {''.join(senha)}. Sua senha cifrada eh: {''.join(senhacifrada)}.")

validacao()
cifra()


