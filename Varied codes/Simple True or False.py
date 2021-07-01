# Escreva uma função que receba como parâmetro uma lista com 10 nomes e um nome
# para pesquisa. Essa função deverá realizar uma busca do nome na lista, retornando
# TRUE se encontrar ou FALSE se não encontrar

i = 0
lista = []

while i < 10:
    nomes = str(input("Entre com os nomes: "))
    lista.append(nomes)
    i = i+1

nome = str(input("Verifique se um nome qualquer se encontra na lista escrevendo-o aqui: "))

if nome in lista:
    print("TRUE")
    
else:
    print("FALSE")
