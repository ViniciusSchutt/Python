#Ler o nome e o salário bruto de 5 pessoas
#Imprimir o nome e a alíquota do imposto de renda (estrutura de seleção encadeada)

for i in range (1, 6, 1):
    nome=str(input("Digite seu nome: "))
    salario=int(input("E seu salário: "))
    if salario <= 600:
        aliquota = 0
        print("Senhor(a): ", nome)
        print("Alíquota do imposto de renda: Isento, R$:", aliquota)
    if salario > 600 and salario <= 1500:
        ir = 0.1
        aliquota = salario * ir
        print("Senhor(a): ", nome)
        print("Segue sua alíquota do imposto de renda: R$", aliquota)
    if salario > 1500:
        ir = 0.15
        aliquota = salario * ir
        print("Senhor(a): ", nome)
        print("Segue sua alíquota do imposto de renda: R$", aliquota)

