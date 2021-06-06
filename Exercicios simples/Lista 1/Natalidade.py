i = 0
qtdM = 0
qtdF = 0
qtd_dois_anos = 0
qtd_total = int(input('Informe quantidade de crianças no período: '))
while i < qtd_total:
    sex = str(input('Informe o sexo da criança (M - masculino; F - feminino)'))
    if sex == 'M' or sex == 'm' or sex == 'F' or sex == 'f':
        if sex == 'M' or sex == 'm':
            qtdM = qtdM+1
        else:
            qtdF = qtdF+1
    else:
        print('Valor inválido. Insira um valor válido para continuar.')
        
nM = (qtdM/qtd_total)*100
nF = (qtdF/qtd_total)*100


print('Porcentagem de nascidos masculinos: ', nM)
print('Porcentagem de nascidos femininos: ', nF)

