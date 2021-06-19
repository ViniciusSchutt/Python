matriz = [[], [], [], []]
nprimos = []
x = 0
while x < 4:
    y = 0
    while y < 3:
        matriz[x].append(int(input("Informe os números que irão compor a matriz: ")))
        y += 1
    x += 1
x = 0
while x < 4:
    y = 0
    while y < 3:
        for i in matriz[x]:
            if i == 1:
                y += 1
            elif i == 2 or i == 3 or i == 5 or i == 7:
                nprimos.append(i)
                y += 1
            elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                y += 1
            else:
                nprimos.append(i)
                y += 1
        x += 1
print(matriz)
print(nprimos)
print("Soma dos elementos da 2ª e 4ª linhas: ", sum(matriz[1])+sum(matriz[3]))
print("Soma dos números primos: ", sum(nprimos))
