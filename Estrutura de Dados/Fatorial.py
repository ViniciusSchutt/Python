#Calculo do fatorial de um número
def loop(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat


def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) * n

n = 5
rec=loop(n)
print("Com loop: ", rec)
res=f(n)
print("Com recursividade: ", res)





