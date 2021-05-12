#Fazer um algoritmo que leia uma determinada quantia dada em reais e converta para uma das seguintes moedas:
#D ou d: dólar - E ou e: euro - L ou l: libra esterlina.

reais=float(input('Informe a quantia em reais "))
moeda=str(input("Informe a moeda: D ou d> dólar - E ou e: euro - L ou l: libra esterlina "))
if moeda =="D" or moeda == "d":
    taxa = float(input("Informe a taxa do dólar "))
    conversao=reais/taxa
    print("Valor cnvertido em dólar ", conversao)
elif moeda == "E" or moeda =="e":
    taxa = float(input("Informe a taxa do euro "))
    conversao=reais/taxa
    print("Valor converido em euro ", conversao)
elif moeda =="L" or moeda == "l":
    taxa = float(input("Informe a taxa da libra "))
    conversao=reais/taxa
    print("Valor convertido em libra ", conversao)
else:
    print("Moeda inválida")
