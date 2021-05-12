n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4)) / 10
print('Média: %0.1f' % media)

if media >= 7.0:
    print('Aluno aprovado')

if media < 5.0:
    print('Aluno reprovado')

if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    ex = float(input())
    print('Nota do exame: %0.1f' % ex)
    novamedia = (media + ex) / 2

    if novamedia >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %0.1f' % novamedia)
    else:
        print('Aluno aprovado')
        print('Media final: %0.1f' % novamedia)

''' outro formato
x = input().split()
n1, n2, n3, n4 = x
m = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
if m < 5.0:
    print('Aluno reprovado.')
if 5.0 <= m <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    m2 = (y + m) / 2
    if m2 >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(m2))
'''