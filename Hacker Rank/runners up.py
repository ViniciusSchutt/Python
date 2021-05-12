#Exercicio runners up 

n = int(input())

nums = map(int, input().split()) # usando mapas, como lista, e split pra ficar separado
print(sorted(list(set(nums)))[-2]) #depois faz o set, que nao deixa repetir, e busca a posição -2, que é o penultimo da lista crescente
