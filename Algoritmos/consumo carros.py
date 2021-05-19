# Cálculo do consumo de combustpivel de carros de acordo com percurso e tipo do veículo

km = float(input("Informe o percurso em quilômetros "))
tipo = str(input("Escolha o tipodo carro: A - 8km, B-9km e C-12km "))

if tipo =="A" or tipo =="a":
    consumo = km/8
elif tipo =="B" or tipo =="b":
    consumo = km/9
elif tipo =="C" or tipo =="c":
    consumo = km/12
else:
    print("Tipo de carro inválido")
print("Consumo de combustível: ", consumo)
