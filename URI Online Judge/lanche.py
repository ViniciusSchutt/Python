
cod = int(input())
qtd = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0

if cod == 1:
    a = qtd*4.00
if cod == 2:
    b = qtd*4.50
if cod == 3:
    c = qtd*5.00
if cod == 4:
    d = qtd*2.00
if cod == 5:
    e = qtd*1.50

total = a+b+c+d+e

print('Total = %0.2f'%total)