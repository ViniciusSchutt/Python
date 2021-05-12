#crie um algoritmo que receba a idade e o estado civil de acordo com os códigos: 1 = casado |2 = solteiro |3 = Viúvo |4 = Divorciado
#calcule e imprima:
#A quantidade de pessoas casadas
#A quantidade de pessoas solteiras
#A média das idades das pessoas viúvas
#A porcentagem de pessoas divorciadas

qntcasados = 0 #quantidade de casados
qntsolteiros = 0 #quantidade de solteiros
somaviuvos = 0 #soma das idades dos viúvos
mediaviuvos = 0 #media da idade dos viúvos
porcdivorciados = 0 #porcentagem de divorciados
nd = 0 #número de divorciados
nv = 0 # número de viúvos
total = 0 #total de entradas de pessoas

idade=int(input("Digite a idade: "))

while idade > 0:
        cod=int(input("Digite 1 para Casado, 2 para Solteiro, 3 para Viúvo e 4 para Divorciado: "))
        total = total + 1
        if cod == 1:
            qntcasados = qntcasados + 1
            idade=int(input("Digite a idade: "))
        elif cod == 2:
            qntsolteiros = qntsolteiros + 1
            idade=int(input("Digite a idade: "))
        elif cod == 3:
            nv = nv + 1
            somaviuvos = somaviuvos + idade
            mediaviuvos = somaviuvos / nv
            idade=int(input("Digite a idade: "))
        elif cod == 4:
            nd = nd + 1
            porcdivorciados = (nd / total) * 100
            idade=int(input("Digite a idade: "))
    
print("A quantidade de pessoas casadas é: ", qntcasados)
print("A quantidade de pessoas solteiras é: ", qntsolteiros)
print("A media das idades das pessoas viúvas é: ", mediaviuvos)
print("A porcentagem de pessoas divorciadas é: %", porcdivorciados)
