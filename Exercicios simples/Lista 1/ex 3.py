i=0
qtdM=0
qtdF=0
qtd_dois_anos=0
qtd_total=int(input('Informe quantidade de crianças no período: '))
while i<qtd_total:
    sex=str(input('Informe o sexo da criança (M - masculino; F - feminino;'))
    if sex=='M' or sex=='m' or sex=='F' or sex=='f':
        if sex == 'M' or sex=='m':
            qtdM=qtdM+1
        else:
            qtdF=qtdF+1
        idade=int(input('Informe quantos meses a criança viveu: '))
        if idade<=24:
            qtd_dois_ano=qtd_dois_anos+1
        i=i+1
    else:
        print('Valor inválido. Insira um valor válido para continuar.')
        
mdM=(qtdM/qtd_total)*100
mdF=(qtdF/qtd_total)*100
mdPeriodo=(qtd_dois_anos/qtd_total)*100

print('Porcentagem de óbitos masculinos: ', mdM)
print('Porcentagem de óbitos femininos: ', mdF)
print('Porccentagem de óbitos de até 24 meses: ', mdPeriodo)
