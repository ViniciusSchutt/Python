import sys

import pandas as pd
import matplotlib.pyplot as plt

dados = 0  # inicializando a variável dados globalmente para poder usar em mais de uma função
dataFrame = pd.read_csv(r"C:\Users\vinic\Downloads\Projeto ED.csv", delimiter=';')


pd.set_option('display.max_rows', None)  # para mostrar todas as linhas na tela
pd.set_option('display.max_columns', None)  # e todas as colunas
pd.set_option('display.width', 2000)  # valor alto de comprimento para garantir que a exibição não seja comprometida
# pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)  # sem limite para o comprimento das colunas


def graficos(dados):
    if dados == 1:
        plt.xlabel("Período")
        plt.ylabel("Expectativa de vida")
        BrasilAnos = (dataFrame.head(59)["Expectativa de vida"])
        BrasilExp = (dataFrame.head(59)["Brasil"])
        plt.plot(BrasilAnos, BrasilExp, label="Brasil")
        EUAAnos = (dataFrame.head(59)["Expectativa de vida"])
        EUAExp = (dataFrame.head(59)["EUA"])
        plt.plot(EUAAnos, EUAExp, label="EUA")
        plt.title('Comparação da evolução na expectativa de vida entre Brasil e EUA')
        plt.legend()
        plt.show()
        dados = graficos((int(input("1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "0 para sair.\n"))))

    if dados == 2:
        plt.xlabel("Período")
        plt.ylabel("Taxa de fertilidade")
        BrasilAnos = (dataFrame.head(59)["Taxa de fertilidade"])
        BrasilFert = (dataFrame.head(59)["Brasil1"])
        plt.plot(BrasilAnos, BrasilFert, label="Brasil")
        EUAAnos = (dataFrame.head(59)["Taxa de fertilidade"])
        EUAFert = (dataFrame.head(59)["EUA1"])
        plt.plot(EUAAnos, EUAFert, label="EUA")
        plt.title('Comparação da evolução na taxa de fertilidade entre Brasil e EUA')
        plt.legend()
        plt.show()
        dados = graficos((int(input("1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "0 para sair.\n"))))
    if dados == 3:
        plt.xlabel("Período")
        plt.ylabel("Renda anual (em milhares de reais)")
        BrasilAnos = (dataFrame.head(49)["Renda Nacional Líquida PC"])
        BrasilRenda = (dataFrame.head(49)["Brasil2"])
        plt.plot(BrasilAnos, BrasilRenda, label="Brasil")
        EUAAnos = (dataFrame.head(49)["Renda Nacional Líquida PC"])
        EUARenda = (dataFrame.head(49)["EUA2"])
        plt.plot(EUAAnos, EUARenda, label="EUA")
        plt.title('Comparação da evolução da renda nacional anual líquida per capita entre Brasil e EUA')
        plt.legend()
        plt.show()
        dados = graficos((int(input("1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "0 para sair.\n"))))
    if dados == 0:
        print("Até mais!")
        sys.exit()
    if dados != 1 and dados != 2 and dados != 3 and dados != 0:
        print("Entrada inválida!")
        dados = graficos((int(input("Por favor, digite:\n"
                                    "1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "0 para sair.\n"))))

# print(dataFrame.iloc[0:5, 0:3])  # metodo alternativo, caso a pessoa queira um período específico de pesquisa
# output some general information about the df


descricao = int(input("Para ver algumas informações e descrições sobre o dataFrame, digite 1, se não, digite 0.\n"))
if descricao == 1:
    print(dataFrame.info())
    print(dataFrame.describe(include=["object", "bool"]))
if descricao == 0:
    pass
else:
    pass

# dataFrame.sort_values(by="Total day charge", ascending=True).head() sort single column
# dataFrame.sort_values(by=["Churn", "Total day charge"], ascending=[True, False]).head() sort multiple columns
# dataFrame["Churn"].mean() calculando a média dos valores de uma coluna
# dataFrame.apply(np.max) colocando todos os valores pro maximo

info = str(input("Você pode pesquisar informações específicas digitando um dado (E, F, R, T, C ou G).\n"
                 "1: 'E', exibe infos sobre expectativa de vida no período.\n"
                 "2: 'F', exibe infos sobre expectativa de vida no período.\n"
                 "3: 'R', exibe infos sobre expectativa de vida no período.\n"
                 "4: 'T', exibe todas as informações de uma só vez, em sequência.\n"
                 "5: Adicionalmente, para ver uma lista de curiosidades com outros dados sobre os países, digite 'C'.\n"
                 "6: Ainda, se quiser visualizar gráficos comparando os dois países, digite 'G'.\n"
                 "7: Por fim, se quiser sair do programa, digite 'S'.\n"))

if info == 'E':
    print(dataFrame.loc[0:59, 'Expectativa de vida1':'br vs eua (x)'])
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))

if info == 'F':
    print(dataFrame.loc[0:59, 'Taxa de fertilidade1':'br vs eua (f)'])
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))

if info == 'R':
    print(dataFrame.loc[0:49, 'Renda1':'br vs eua (rl)'])
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))

if info == 'T':
    print(dataFrame.loc[0:59, 'Expectativa de vida1':'br vs eua (x)'])
    print(dataFrame.loc[0:59, 'Taxa de fertilidade1':'br vs eua (f)'])
    print(dataFrame.loc[0:49, 'Renda1':'br vs eua (rl)'])
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))

if info == 'C':
    print(dataFrame.loc[0:27, 'Curiosidades':'br vs eua'])
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))

if info == 'G':
    dados = graficos((int(input(
                   "Você pode visualizar os gráficos usando as seguintes opções: \n"
                   "1 para Expectativa de vida;\n"
                   "2 para Taxa de Fertilidade;\n"
                   "3 para Renda Nacional Líquida per capita.\n"
                   "0 para sair.\n"))))
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))

if info == 'S':
    print('Obrigado por usar o programa!\n')
    sys.exit()
else:
    print("Entrada inválida, por favor, digite novamente:\n")
    info = str(input("E= expect. vida, F= fert., R= renda, T= tudo, C= curiosidades, G= gráficos e S para sair.\n"))
