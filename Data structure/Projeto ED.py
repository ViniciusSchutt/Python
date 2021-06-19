import sys
# from typing import Any, Union

# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = 0  # inicializando a variável dados globalmente para poder usar em todas as funções
pergunta = 0  # mesmo caso
dataFrame = pd.read_csv(r"C:\Users\vinic\Downloads\Projeto ED.csv", delimiter=';')

html = dataFrame.to_html()  # criação do arquivo de saída dos dados
text_file = open("Projeto ED.html", "w")
text_file.write(html)
text_file.close()

# funções de ordenação que não foram executadas porque perderia o sentido dos dados
# dataFrame.sort_values(by="br vs eua", ascending=True).head() sort single column
# dataFrame.sort_values(by=["Brasil", "EUA"], ascending=[True, False]).head() sort multiple columns
# dataFrame.apply(np.max) colocando todos os valores pro maximo

# criando uma lista com os anos do período como valores para iterar sobre e usar na função de infos pontuais
periodo = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969,
           1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,
           1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
           1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
           2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
           2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]


pd.set_option('display.max_rows', None)  # para mostrar todas as linhas na tela
pd.set_option('display.max_columns', None)  # e todas as colunas
pd.set_option('display.width', 2000)  # valor alto de comprimento para garantir que a exibição não seja comprometida
# pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)  # sem limite para o comprimento das colunas


# função que exibe os gráficos e recebe 'dados' como argumento
def graficos(dados):
    if dados == 1:
        plt.xlabel("Período")
        plt.ylabel("Expectativa de vida")
        BrasilAnos = (dataFrame.head(59)["Expectativa de vida"])
        BrasilExp = (dataFrame.head(59)["brE"])
        plt.plot(BrasilAnos, BrasilExp, label="Brasil")
        EUAAnos = (dataFrame.head(59)["Expectativa de vida"])
        EUAExp = (dataFrame.head(59)["euaE"])
        plt.plot(EUAAnos, EUAExp, label="EUA")
        plt.title('Comparação da evolução da expectativa de vida entre Brasil e EUA no período (1960-2019)')
        plt.legend()
        plt.show()
        dados = graficos((int(input("Visualize outros gráficos, digitando:"
                                    "1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "4 para voltar ao menu anterior e continuar usando o programa;\n"
                                    "0 para sair.\n"))))
    if dados == 2:
        plt.xlabel("Período")
        plt.ylabel("Taxa de fertilidade")
        BrasilAnos = (dataFrame.head(59)["Taxa de fertilidade"])
        BrasilFert = (dataFrame.head(59)["brF"])
        plt.plot(BrasilAnos, BrasilFert, label="Brasil")
        EUAAnos = (dataFrame.head(59)["Taxa de fertilidade"])
        EUAFert = (dataFrame.head(59)["euaF"])
        plt.plot(EUAAnos, EUAFert, label="EUA")
        plt.title('Comparação da evolução na taxa de fertilidade entre Brasil e EUA')
        plt.legend()
        plt.show()
        dados = graficos((int(input("Visualize outros gráficos, digitando:"
                                    "1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "4 para voltar ao menu anterior e continuar usando o programa;\n"
                                    "0 para sair.\n"))))
    if dados == 3:
        plt.xlabel("Período")
        plt.ylabel("Renda anual (em milhares de reais)")
        BrasilAnos = (dataFrame.head(49)["Renda Nacional Líquida PC"])
        BrasilRenda = (dataFrame.head(49)["brR"])
        plt.plot(BrasilAnos, BrasilRenda, label="Brasil")
        EUAAnos = (dataFrame.head(49)["Renda Nacional Líquida PC"])
        EUARenda = (dataFrame.head(49)["euaR"])
        plt.plot(EUAAnos, EUARenda, label="EUA")
        plt.title('Comparação da evolução da renda nacional anual líquida per capita entre Brasil e EUA')
        plt.legend()
        plt.show()
        dados = graficos((int(input("Visualize outros gráficos, digitando:"
                                    "1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "4 para voltar ao menu anterior e continuar usando o programa;\n"
                                    "0 para sair.\n"))))
    if dados == 4:
        pergunta = int(input("Continuar pesquisando? Digite 1 para sim e 0 para não: \n"))
        if pergunta == 1:
            info = infoIsolada(str.upper(input(
                "Você pode pesquisar informações específicas digitando: \n"
                "1: 'E' p/ expectativa de vida no período.\n"
                "2: 'F' p/ taxa de fertilidade no período.\n"
                "3: 'R' p/ renda no período.\n"
                "4: 'T' p/ visualizar todas as informações.\n"
                "5: 'C' p/ ver curiosidades com diversos dados sobre os países.\n"
                "6: 'G' p/ visualizar gráficos comparando os dados.\n"
                "7: 'OK' p/ buscar informações de um único ano ou ajustar períodos de pesquisa.\n"
                "8: 'S' p/ sair.\n")))
        if pergunta == 0:
            print("Obrigado.\n")
            sys.exit()
        else:
            pergunta = int(input("Entrada inválida. Digite 1 para pesquisar ou 0 para sair.\n"))

    if dados == 0:
        print("Obrigado por usar o programa, até mais!")
        sys.exit()

    if dados != 1 and dados != 2 and dados != 3 and dados != 0:
        dados = graficos((int(input("Entrada inválida, para visualizar outros gráficos, tente:"
                                    "1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita;\n"
                                    "4 para voltar ao menu anterior e continuar usando o programa;\n"
                                    "0 para sair.\n"))))


# criando a função que retorna informações pontuais, de anos únicos ou períodos especificados pelo usuário, ano como arg
def infoPontual(ano):
    refinar = str.upper(input(
                        "1: Depois de escolhido um ano, você pode refinar sua pesquisa. Para isso, use:\n"
                        "2: '0' (zero) p/ não adicionar detalhes, ou:\n"
                        "3: '1' Se quiser dar um zoom e visualizar períodos menores. Dessa forma, o primeiro ano\n"
                        "4: digitado assume posição de ano inicial, então você só precisa digitar um segundo ano para\n"
                        "5: criar um período detalhado de pesquisa entre ano inicial e ano final.\n"
                        "6: 'E' p/ ver somente infos de expectativa de vida desse ano.\n"
                        "7: 'F' p/ ver somente infos de fertilidade desse ano.\n"
                        "8: 'R' p/ ver somente infos de renda desse ano.\n"
                        "9: 'S' p/ sair.\n"
                        "10: 'Z' p/ voltar a seção anterior e continuar usando o programa.\n"))

    if refinar == 'S':
        print("Obrigado por usar o programa, boa noite!\n")
        sys.exit()

    if refinar == '0':
        for i in range(len(periodo)):  # para i dentro do range do periodo
            if periodo[i] == ano:  # quando o valor da posicao i de periodo for igual ao ano digitado pelo usuário:
                a = periodo[i]  # a variável 'a' (nome genérico) recebe o valor dessa posição da lista período
                pos = periodo.index(a)  # variavel posição recebe o valor do indice 'a' da lista período (de 0 a 59)
                print(dataFrame.iloc[pos, 0:9])  # então imprime exatamente essa posição (linha) nas cols de 0 a 9
        refinar = str.upper(input(
            "1: '1', Se quiser dar um zoom e visualizar períodos menores. Dessa forma, o primeiro ano\n"
            "2: digitado assume posição de ano inicial, então você só precisa digitar um segundo ano para\n"
            "3: criar um período detalhado de pesquisa (por exemplo, de 1992 a 2002).\n"
            "4: 'E' p/ ver somente infos de expectativa de vida desse ano.\n"
            "5: 'F' p/ ver somente infos de fertilidade desse ano.\n"
            "6: 'R' p/ ver somente infos de renda desse ano.\n"
            "7: 'S' p/ sair.\n"
            "8: 'Z' p/ voltar a seção anterior e continuar usando o programa.\n"))

    if refinar == '1':
        ano2 = int(input("Digite o segundo ano:\n"))
        for i in range(len(periodo)):  # mesmo caso do if anterior
            if periodo[i] == ano:
                a = periodo[i]
                pos1 = periodo.index(a)
            if periodo[i] == ano2:
                b = periodo[i]
                pos2 = periodo.index(b)
        print(dataFrame.iloc[pos1:pos2 + 1, 0:9])  # só que agora com duas posições, criando um período manipulado
        refinar = str.upper(input(
            "1: 'E' p/ ver somente infos de expectativa de vida desse ano.\n"
            "2: 'F' p/ ver somente infos de fertilidade desse ano.\n"
            "3: 'R' p/ ver somente infos de renda desse ano.\n"
            "4: 'S' p/ sair.\n"
            "5: 'Z' para voltar a seção anterior e continuar usando o programa.\n"))

    if refinar == 'E':
        for i in range(len(periodo)):
            if periodo[i] == ano:
                a = periodo[i]
                pos = periodo.index(a)
                print(dataFrame.iloc[pos, 0:3])  # somente as primeiras colunas, que são de expectativa de vida
        refinar = str.upper(input(
            "1: '0' (zero) p/ não adicionar detalhes, ou:\n"
            "2: '1' Se quiser dar um zoom e visualizar períodos menores. Dessa forma, o primeiro ano\n"
            "3: digitado assume posição de ano inicial, então você só precisa digitar um segundo ano para\n"
            "4: criar um período detalhado de pesquisa entre ano inicial e ano final.\n"
            "5: 'F' p/ ver somente infos de fertilidade desse ano.\n"
            "6: 'R' p/ ver somente infos de renda desse ano.\n"
            "7: 'S' p/ sair.\n"
            "8: 'Z' para voltar a seção anterior e continuar usando o programa.\n"))

    if refinar == 'F':
        for i in range(len(periodo)):
            if periodo[i] == ano:
                a = periodo[i]
                pos = periodo.index(a)
                print(dataFrame.iloc[pos, 3:6])  # somente as colunas de taxa de fertilidade
        refinar = str.upper(input(
            "1: '0' (zero) p/ não adicionar detalhes, ou:\n"
            "2: '1' Se quiser dar um zoom e visualizar períodos menores. Dessa forma, o primeiro ano\n"
            "3: digitado assume posição de ano inicial, então você só precisa digitar um segundo ano para\n"
            "4: criar um período detalhado de pesquisa entre ano inicial e ano final.\n"
            "5: 'E' p/ ver somente infos de expectativa de vida desse ano.\n"
            "6: 'R' p/ ver somente infos de renda desse ano.\n"
            "7: 'S' p/ sair.\n"
            "8: 'Z' para voltar a seção anterior e continuar usando o programa.\n"))

    if refinar == 'R':
        for i in range(len(periodo)):
            if periodo[i] == ano:
                a = periodo[i]
                pos = periodo.index(a)
                print(dataFrame.iloc[pos, 6:9])  # somente as colunas de renda
        refinar = str.upper(input(
            "1: '0' (zero) p/ não adicionar detalhes, ou:\n"
            "2: '1' Se quiser dar um zoom e visualizar períodos menores. Dessa forma, o primeiro ano\n"
            "3: digitado assume posição de ano inicial, então você só precisa digitar um segundo ano para\n"
            "4: criar um período detalhado de pesquisa entre ano inicial e ano final.\n"
            "5: 'E' p/ ver somente info sobre expectativa de vida desse ano.\n"
            "6: 'F' p/ ver somente info de fertilidade desse ano.\n"
            "7: 'S' p/ sair.\n"
            "8: 'Z' para voltar a seção anterior e continuar usando o programa.\n"))

    if refinar == 'Z':
        pergunta = int(input("Continuar pesquisando? Digite 1 para sim e 0 para não: \n"))
        if pergunta == 1:
            info = infoIsolada(str.upper(input(
                "Você pode pesquisar informações específicas digitando: \n"
                "1: 'E' p/ expectativa de vida no período.\n"
                "2: 'F' p/ taxa de fertilidade no período.\n"
                "3: 'R' p/ renda no período.\n"
                "4: 'T' p/ visualizar todas as informações.\n"
                "5: 'C' p/ ver curiosidades com diversos dados sobre os países.\n"
                "6: 'G' p/ visualizar gráficos comparando os dados.\n"
                "7: 'OK' p/ buscar informações de um único ano ou ajustar períodos de pesquisa.\n"
                "8: 'S' p/ sair.\n")))
        if pergunta == 0:
            print("Até!\n")
            sys.exit()
        else:
            pergunta = int(input("Entrada inválida. Digite 1 para pesquisar ou 0 para sair.\n"))


# criando a função que exibe informações isoladas ou todas de uma vez, assim como curiosidades, recebe info como arg
def infoIsolada(info):
    if info == 'E':
        print(dataFrame.loc[0:59, 'Expectativa de vida1':'br vs eua (x)'])
        info = infoIsolada(str.upper(input(
                               "Info: \n'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))

    if info == 'F':
        print(dataFrame.loc[0:59, 'Taxa de fertilidade1':'br vs eua (f)'])
        info = infoIsolada(str.upper(input(
                               "Info: \n'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))

    if info == 'R':
        print(dataFrame.loc[0:49, 'Renda1':'br vs eua (rl)'])
        info = infoIsolada(str.upper(input(
                               "Info: \n'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))

    if info == 'T':
        print(dataFrame.loc[0:59, 'Expectativa de vida1':'br vs eua (x)'])
        print(dataFrame.loc[0:59, 'Taxa de fertilidade1':'br vs eua (f)'])
        print(dataFrame.loc[0:49, 'Renda1':'br vs eua (rl)'])
        info = infoIsolada(str.upper(input(
                               "Info: \n'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))

    if info == 'C':
        print(dataFrame.loc[0:27, 'Curiosidades':'br vs eua'])
        print("Expectativa de vida (lengovidade) média no Brasil:")
        print(dataFrame["brE"].mean())
        print("Expectativa de vida (lengovidade) média nos Estados Unidos:")
        print(dataFrame["euaE"].mean())
        print("Taxa de fertilidade média no Brasil:")
        print(dataFrame["brF"].mean())
        print("Taxa de fertilidade média nos Estados Unidos:")
        print(dataFrame["euaF"].mean())
        print("Renda nacional líquida per capita média no Brasil:")
        print(dataFrame["brR"].mean())
        print("Renda nacional líquida per capita média nos Estados Unidos:")
        print(dataFrame["euaR"].mean())

        info = infoIsolada(str.upper(input(
                               "Info: \n'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))

    if info == 'G':
        dados = graficos((int(input("Você pode visualizar os gráficos usando as seguintes opções: \n"  # chama f grafs
                                    "1 para Expectativa de vida;\n"
                                    "2 para Taxa de Fertilidade;\n"
                                    "3 para Renda Nacional Líquida per capita.\n"
                                    "0 para sair.\n"))))
        info = infoIsolada(str.upper(input(
                               "Info: \n'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))

    if info == 'OK':
        ano = infoPontual(int(input("Ditite um ano: \n")))

    if info == 'S':
        print('Obrigado por usar o programa!\n')
        sys.exit()

    else:
        print("Entrada inválida, por favor, tente:\n")
        info = infoIsolada(str.upper(input(
                               "'E' p/ expect. vida; 'F' p/ fert; 'R' p/ renda; 'T' p/ tudo;\n"
                               "'C' p/ curiosidades; 'OK' p/ prosseguir; 'G' p/ gráficos; 'S' p/ sair.\n")))


pergunta = int(input("Esse programa compara informações sobre população brasileira e americana. Digite:\n"
                     "1 para pesquisar;\n"
                     "2 para ver informações e descrições sobre o dataframe;\n"
                     "0 para sair.\n"))
if pergunta == 1:
    info = infoIsolada(str.upper(input(
                 "Você pode pesquisar informações específicas digitando: \n"
                 "1: 'E' p/ expectativa de vida no período.\n"
                 "2: 'F' p/ taxa de fertilidade no período.\n"
                 "3: 'R' p/ renda no período.\n"
                 "4: 'T' p/ visualizar todas as informações.\n"
                 "5: 'C' p/ ver curiosidades com diversos dados sobre os países.\n"
                 "6: 'G' p/ visualizar gráficos comparando os dados.\n"
                 "7: 'OK' p/ buscar informações de um único ano ou ajustar períodos de pesquisa.\n"
                 "8: 'S' p/ sair.\n")))

if pergunta == 2:
    print(dataFrame.info())
    print(dataFrame.describe(include=["object", "bool"]))
    info = infoIsolada(str.upper(input(
        "Você pode pesquisar informações específicas digitando: \n"
        "1: 'E' p/ expectativa de vida no período.\n"
        "2: 'F' p/ taxa de fertilidade no período.\n"
        "3: 'R' p/ renda no período.\n"
        "4: 'T' p/ visualizar todas as informações.\n"
        "5: 'C' p/ ver curiosidades com diversos dados sobre os países.\n"
        "6: 'G' p/ visualizar gráficos comparando os dados.\n"
        "7: 'OK' p/ buscar informações de um único ano ou ajustar períodos de pesquisa.\n"
        "8: 'S' p/ sair.\n")))
if pergunta == 0:
    print("Até!\n")
    sys.exit()
else:
    pergunta = int(input("Entrada inválida. Digite 1 para pesquisar, 2 para infos ou 0 para sair.\n"))
