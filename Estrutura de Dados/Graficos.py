import sys

import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv(r"C:\Users\vinic\Downloads\Projeto ED.csv", delimiter=';')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
# pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)

print(dataFrame.loc[0:26, 'Curiosidades':'br vs eua'])

"""
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
                                    "3 = Renda Nacional Líquida per capita;\n"
                                    "0 = sair.\n"))))
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


dados = graficos((int(input("Visualize gráficos comparando informações entre Brasil e EUA, digitando: \n"
                            "1 para Expectativa de vida;\n"
                            "2 para Taxa de Fertilidade;\n"
                            "3 para Renda Nacional Líquida per capita.\n"
                            "0 para sair.\n"))))
                            """
