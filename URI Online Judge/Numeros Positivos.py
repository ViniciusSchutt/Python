contador = 0
n = [None] * 6
def cont():
    for i in range(6):
        global n
        n[i] = int(input('n'))
        global contador
        if n[i]>0:
            contador = contador + 1
        if n[i] == 0:
            print("Valor inválido")
            exit()
        else:
            contador = contador

    return contador

cont()
print(f'{contador} valores positivos')