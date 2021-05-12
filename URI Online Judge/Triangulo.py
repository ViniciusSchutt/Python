
x = input().split()
a, b, c = x

a = float(a)
b = float(b)
c = float(c)

if a+b > c and a+c> b and b+c > a:
    perimetro = a+b+c
    print('Perimetro = %0.1f'%perimetro)

else:
    area = ((a+b)/2)*c
    print('Area = %0.1f'%area)

