
x = input().split()
a, b = x

a = int(a)
b = int(b)

if b < 12 and a > 12:
    b = b + 24
    tempo = b - a
    print(f'O JOGO DUROU {tempo} HORA(S)')
if a < 12 and b > 12:
    tempo = b - a
    print(f'O JOGO DUROU {tempo} HORA(S)')
if a == b:
    print('O JOGO DUROU 24 HORA(S)')
