x = input().split()
a, b, c, d = x

a = int(a) // hora inicial
b = int(b) // minuto inicial
c = int(c) // hora final
d = int(d) // minuto final

if c < 12 and a < 12 and d != b and c - a >= 2:
    horas = c - a
    if d < b:
        minutos = (d - b) + 60
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
    else:
        minutos = d - b
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

if c < 12 and a > 12 and c - a >= 2:
    c = c + 24
    horas = c - a

    if d < b:
        minutos = (d - b) + 60
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

    if d == b or d > b:
        minutos = d - b
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

if a < 12 and c > 12:
    horas = c - a
    if d < b:
        minutos = (d - b) + 60
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

    if d == b or d > b:
        minutos = d - b
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

if c - a <= 1 and d < b:
    horas = 0
    minutos = (d - b) + 60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

if a == b == c == d:
    horas = 0
    minutos = 0
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

'''Outra forma
x = input().split()
hi, mi, hf, mf = x

hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
    if mi == mf:
        h = 24
        m = 0
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))
'''
