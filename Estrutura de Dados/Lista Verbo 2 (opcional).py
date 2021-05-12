
aluno1=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno2=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno3=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno4=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno5=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno6=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno7=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno8=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno9=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]
aluno10=[str(input("Nome do aluno: ")), int(input("Ano de matrícula: ")), int(input("Em que semestre está: ")), int(input("N inicial da matrícula"))]

alunos=[aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]

for i in range(len(alunos)):
    print(f'O aluno(a) {alunos[i][0]}, matriculado(a) no ano de {alunos[i][1]}, no {alunos[i][2]} semestre, possui o seguinte RA: {alunos[i][3]+alunos[i][2]+alunos[i][1]}')
