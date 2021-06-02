#Exercício 4: Faça um programa que preencha duas listas com 10 elementos cada. Depois
#percorra essas duas listas e gere uma terceira com números que se repetem
#nas duas listas. Mostre as tres listas na tela


lista1=[]
lista2=[]
lista3=[]
x=0

while x < 10:
    valoreslista1=(input("Próximo númeiro da 1ª lista: ", )) #entradas para 1ª lista
    lista1.append(valoreslista1)
    
    
    valoreslista2=(input("Próximo número da 2ª lista: ", )) #entradas para 2ª lista
    lista2.append(valoreslista2)
    
    x=x+1

lista3=list(set(lista1).intersection(lista2))
    
print(lista1)
print(lista2)
print(lista3)
