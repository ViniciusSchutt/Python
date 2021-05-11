#Criar um algoritmo que leia o destino do passageiro.
#Imprimir o preço da passagem de acordo com a tabela abaixo.
#Região norte IDA 500 IDA E VOLTA 950
#Região nordeste IDA 350 IDA E VOLTA 650
#Região centro-oeste IDA 300 IDA E VOLTA 550
#Região Sul IDA 200 IDA E VOLTA 350

regiao=str(input("Qual o destino desejado? "))

if regiao=="norte" or regiao =="Norte" or regiao =="NORTE":
    print("O valor só de ida é R$ 500, enquanto de ida e volta é R$ 950")

elif regiao=="nordeste" or regiao=="Nordeste" or regiao=="NORDESTE":
    print("O valor só de ida é R$ 350, enquanto ida e volta é R$ 650")

elif regiao=="centro-oeste" or regiao=="Centro-Oeste" or regiao=="CENTRO-OESTE":
    print("O valor só de ia é R$ 300, enquanto ida e volta é R$ 500")

elif regiao=="sul" or regiao=="Sul" or regiao=="SUL":
    print("O valor só de ida é R$ 200, enquanto ida e volta é R$ 350")

else:
    print("Região inválida, por favor, digite novamente!")
