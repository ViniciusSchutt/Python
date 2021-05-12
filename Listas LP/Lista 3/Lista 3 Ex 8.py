nome_alunos=[]
med_alunos=[]
sup7=[]
inf7=[]
x=0
while x<10:
    nome=str(input('Informe o nome do aluno: '))
    media=float(input('Informe a média do aluno: '))
    nome_alunos.append(nome)
    med_alunos.append(media)
    if media >=7:
        sup7.append(media)
    else:
        inf7.append(media)
    x+=1
for i in med_alunos:
    if i==max(med_alunos):
        n=med_alunos.index(i)
print('Média da classe: ',sum(med_alunos)/len(med_alunos))
print('Nº de notas superiores ou iguais a 7: ',len(sup7))
print('Nº de notas abaixo de 7: ',len(inf7))
print('Maior media: ',max(med_alunos),' Aluno: ', nome_alunos[n])