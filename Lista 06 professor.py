vtLinhas = []

def Insere():
    for linha in range(10):
        vtColunas = []
        for coluna in range(4):
            vtColunas.insert(coluna, int(0))
        vtLinhas.insert(linha, vtColunas)

def Exibe():
    for linha in range(10):
        for coluna in range(4):
            print(vtLinhas[linha][coluna], end="")

def Reserva():
    resp="S"
    qtdlugaresocupados = int(0)
    percentualocupados = float(0)
    totalvenda = float(0)
    while resp == "S":
        print(" Informe a linha: ")
        linha = int(input())
        print(" Informe a coluna: ")
        coluna = int(input())
        if (vtLinhas[linha][coluna] == 0):
            vtLinhas[linha][coluna] = 1
            qtdlugaresocupados = qtdlugaresocupados+1
            percentualocupados = (qtdlugaresocupados*100)/40
            if ((coluna==0) or (coluna==3)):
                totalvenda = totalvenda+110
            else:
                totalvenda = totalvenda+100
        else:
            print("Lugar ocupado!")
        Exibe()
        print("Quantidade de lugares ocupados:", qtdlugaresocupados)
        print(f"Percentual de ocupação: {percentualocupados}")
        print(f"Quantidade de lugares vazios:{(40-qtdlugaresocupados)}")
        print(f"Total de vendas de passagens: {totalvenda}")
        print("Deseja ocupar outra poltrona?")
        resp=input()


Insere()
Exibe()
Reserva()