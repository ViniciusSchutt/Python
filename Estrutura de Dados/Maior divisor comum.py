def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc(a, b)

a=int(input("Digite o valor do primeiro número: "))
b=int(input("Digite o valor do segundo número: "))

print("O MDC dos números eh: ", mdc(a, b))
