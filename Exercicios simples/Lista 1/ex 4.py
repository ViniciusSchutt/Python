#4)Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme (3-ótimo;2-bom;1-regular)
#Faça  um  programa  que  receba  a  idade  e  a  opinião  de  um  número  indeterminado  de
#pessoas. Para finalizar a entrada deve ser digitado uma idade negativa ou zero. Calcule e mostre:
#A média das idades das pessoas que responderam ótimo;
#A quantidade de pessoas que responderam regular;
#A quantidade de pessoas que responderam bom.

media=0
qtd=0
qtd1=0
qtd2=0

idade=int(input("Olá, qual é a sua idade? "))
          
while idade>0:
    
    opiniao=str(input("Deixe sua opinião sobre o filme, ele foi: Ótimo, bom ou regular?: "))
    if opiniao=="ótimo" or opiniao=="Ótimo" or opiniao=="ÓTIMO":
        qtd=qtd+1
        media=media+idade
    elif opiniao=="bom" or opiniao=="Bom" or opiniao=="BOM":
        qtd1=qtd1+1
    elif opiniao=="regular" or opiniao=="Regular" or opiniao=="REGULAR":
        qtd2=qtd2+1
    else:
        print("Opinião inválida. Você deve digitar/escrever somente entre as seguintes opções: Ótimo, bom ou regular. Tente de novo!")

    idade=int(input("Qual é a sua idade?"))
print("A média das pessoas que responderam 'ótimo' é: ", media/qtd)
print("A quantidade de pessoas que responderam 'regular' é: ", qtd2)
print("A quantidade de pessoas que responderam 'bom' é: ", qtd1)
