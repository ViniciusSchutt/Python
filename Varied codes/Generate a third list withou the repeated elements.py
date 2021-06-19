# Faça um programa que percorra duas listas e gere uma terceira lista sem os elementos
# repetidos. Mostrar na tela as 3 listas.

listaA = []
listaB = []
listaC = []
x = 1
while x > 0:
    print("Quando quiser encerrar o programa, digite 0.")
    a = int(input("Insira um número na lista A: "))
    if a > 0:
        listaA.append(a)
        listaC.append(a)
    else:
        x = 0
x = 1
while x > 0:
    print("Quando quiser encerrar o programa, digite 0.")
    b = int(input("Insira um número na lista B: "))
    if b > 0:
        listaB.append(b)
        listaC.append(b)
    else:
        x = 0


def remove_repetidos(listaC):
    l = []
    for i in listaC:
        if i not in l:
            l.append(i)
    l.sort()
    return l


listaC = remove_repetidos(listaC)
print(listaA)
print(listaB)
print(listaC)