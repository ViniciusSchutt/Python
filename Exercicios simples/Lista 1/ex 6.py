numero=int(input('Informe um número para o fatorial: '))
x=numero
fat=1
while x>0:
    print('{}' .format(x))
    fat *= x
    x -=1
    
print('O resultado do fatoreal é {}' .format(fat))
