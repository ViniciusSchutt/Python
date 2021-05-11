#Os votos são informados através de código. Os dados utilizados obedecem à seguinte codificação: 
#• 1, 2 e 3 = voto para os respectivos candidatos; 
#• 4 = voto nulo; 
#• 5 = voto em branco; 

#Elaborar um algoritmo que calcule e imprima: 
#• Total de votos de cada candidato. 
#• Total de votos nulos. 
#• Total de votos em branco. 
#• Percentual dos votos em branco e nulos sobre o total. 

#O algoritmo encerra quando se digita um número fora do intervalo da faixa de 1 a 5.

c1 = 0
c2 = 0
c3 = 0
nulos = 0
brancos = 0

voto=int(input("Digite seu voto: 1 para votar no 1º candidato, 2 para o 2º, 3 para o 3º, 4 para votar nulo e 5 para votar em branco: "))

while voto > 0 and voto < 6:
    
    if voto == 1:
        c1 = c1 + 1
        voto=int(input("Digite seu voto: 1 para votar no 1º candidato, 2 para o 2º, 3 para o 3º, 4 para votar nulo e 5 para votar em branco: "))

    if voto == 2:
        c2 = c2 + 1
        voto=int(input("Digite seu voto: 1 para votar no 1º candidato, 2 para o 2º, 3 para o 3º, 4 para votar nulo e 5 para votar em branco: "))

    if voto == 3:
        c3 = c3 + 1
        voto=int(input("Digite seu voto: 1 para votar no 1º candidato, 2 para o 2º, 3 para o 3º, 4 para votar nulo e 5 para votar em branco: "))

    if voto == 4:
        nulos = nulos + 1
        voto=int(input("Digite seu voto: 1 para votar no 1º candidato, 2 para o 2º, 3 para o 3º, 4 para votar nulo e 5 para votar em branco: "))

    if voto == 5:
        brancos = brancos + 1
        voto=int(input("Digite seu voto: 1 para votar no 1º candidato, 2 para o 2º, 3 para o 3º, 4 para votar nulo e 5 para votar em branco: "))

percentbrancosenulos = ((brancos+nulos)/(c1+c2+c3+brancos+nulos))*100

print("Os totais de votos dos candidatos é: Candidato 1: ", c1,"Candidato 2:", c2, "Candidato 3:", c3,"Total de nulos: ", nulos,"Total de brancos:", brancos)
print("A porcentagem de votos em branco e nulos sobre o total é de: ", percentbrancosenulos,"%")

    
    

