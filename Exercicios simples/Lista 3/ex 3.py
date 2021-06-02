lista=[['José',350.0,900.0,420.0],['Pamela',550.0,210.0,350.0],['Thaiane',800.0,300.0,150.0],['Elisa',200.0,550.0,720.0],['Dante',300.0,400.0,500.0]]
matriz1=[]
matriz2=[]
matriz3=[]
mv=[]
x=0
while x<5:
    f=0
    y=1
    while y<4:
        f=f+lista[x][y]
        y+=1
    mv.append(f)
    x+=1
i=0
while i<5:
    mv1=lista[i][1]
    matriz1.append(mv1)
    i+=1
i=0
while i<5:
    mv2=lista[i][2]
    matriz2.append(mv2)
    i+=1
i=0
while i<5:
    mv3=lista[i][3]
    matriz3.append(mv3)
    i+=1

print("Valor total vendido por cada vendedor: ")
print(lista[0][0],": ",mv[0])
print(lista[1][0],": ",mv[1])
print(lista[2][0],": ",mv[2])
print(lista[3][0],": ",mv[3])
print(lista[4][0],": ",mv[4])
print("Maior venda no 1º mês: ", max(matriz1))
print("Menor venda no 3º mês: ", min(matriz3))
print('TOTAL VENDIDO P/ MÊS:')
print("1º mês: ", sum(matriz1))
print("2º mês: ", sum(matriz2))
print("3º mês: ", sum(matriz3))
