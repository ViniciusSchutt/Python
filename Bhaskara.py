A = float(input())
B = float(input())
C = float(input())

if A == 0.0 or (B**2 - 4*A*C) <0:
    print('Impossível calcular')

else:
    D = (B**2 - 4*A*C)
    R1 = (- B + (B**2 - 4*A*C)**(1/2))/(2*A)
    R2 = (- B - (B**2 - 4*A*C)**(1/2))/(2*A)
    print('R1 = %0.5f' % R1)
    print('R2 = %0.5f' % R2)