
x = float(input())

if 0 < x <= 400.00:
    reajuste = x*0.15
    newx = x + reajuste
    print('Novo salario: %0.2f'%newx)
    print('Reajuste ganho: %0.2f'%reajuste)
    print('Em percentual: 15 %')

if 400.00 < x <= 800.00:
    reajuste = x*0.12
    newx = x + reajuste
    print('Novo salario: %0.2f'%newx)
    print('Reajuste ganho: %0.2f'%reajuste)
    print('Em percentual: 12 %')

if 800.00 < x <= 1200.00:
    reajuste = x*0.10
    newx = x + reajuste
    print('Novo salario: %0.2f'%newx)
    print('Reajuste ganho: %0.2f'%reajuste)
    print('Em percentual: 10 %')

if 1200.00 < x <= 2000.00:
    reajuste = x*0.07
    newx = x + reajuste
    print('Novo salario: %0.2f'%newx)
    print('Reajuste ganho: %0.2f'%reajuste)
    print('Em percentual: 7 %')

if x > 2000.00:
    reajuste = x*0.04
    newx = x + reajuste
    print('Novo salario: %0.2f'%newx)
    print('Reajuste ganho: %0.2f'%reajuste)
    print('Em percentual: 4 %')