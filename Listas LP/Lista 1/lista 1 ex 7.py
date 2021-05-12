idades=[]
x=1
xx=0
while x:
    x=int(input('Digite uma idade ou 0 para mostrar a média de idades: '))
    if x:
        idades.append(x)
        xx=xx+1
        
print('A média de idade é: ', sum(idades)/xx)
