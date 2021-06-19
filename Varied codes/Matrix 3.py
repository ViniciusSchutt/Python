m = [["Chibs", "Bobby", "Happy", "Jax", "Tara"], [5.5, 8.0, 3.5, 9.0, 8.5], [8.5, 6.0, 10.0, 8.5, 9.5]]
media = []
sera = []
x = 1
y = 0
while y < 5:
    n1 = m[x][y]
    n2 = m[x+1][y]+n1
    med = n2/2
    media.append(med)
    if med >= 6:
        situacao = "aprovado"
    else:
        situacao = "reprovado"
    sera.append(situacao)
    y += 1
busca = str(input("Procure um nome para verificar a situação do mesmo: "))
for i in m[0]:
    if busca == i:
        j = m[0].index(i)
        print("Aluno: ", i, "Posição: ", j)
        print("1ª nota: ", m[1][j], "2ª nota: ", m[2][j], "Média: ", media[j], "Situação: ", sera[j])
    if busca not in m[0]:
        print("Aluno não encontrado.")
        break
