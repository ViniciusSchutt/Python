"""
# 01 construir um progama para eleger um representante da classe. Serão fornecidos
# os nomes de dois candidatos e a quantidade de votos de cada um. Exibir qual
# candidato ganhou. Suponha que um dos candidados sempre terá um número maior
# de votos. Utilizar estrutura de seleção composta
"""

print("Esse programa irá identificar qual dos dois candidatos recebeu mais votos ")

candidato1=str(input("Digite o nome do primeiro candidato: "))
candidato2=str(input("Digite o nome do segundo candidato: "))

votosc1=int(input("Quantos votos recebeu o primeiro candidato? "))
votosc2=int(input("Quantos votos recebeu o segundo candidato? "))

if votosc1 > votosc2:
    print("O candidato vencedor é: ", candidato1)

else:
    print("O candidato vencedor é: ", candidato2)
