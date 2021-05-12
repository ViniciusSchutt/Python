#Escreva um programa que prencha uma lista com os nomes de 5 vendedores, preencha tbm uma outra lista com total vendido po cada vendedor.
#Cada vendedor recebe 15% de comissão sobre as vendas. Faça os seguintes cálculos e mostre os resultados na tela: (2 pontos)
# a. uma listagem com o nome e o valor de comissão de cada vendedor (vendas * 0,15) (2 pontos)
# b. o total de comissão pago pela empresa (5 vendedores) (1 ponto)
# c. a media das vendas (bruto) (1 ponto)
# d. a quantidade de vendedores que venderam abaixo da média (2 pontos)
# e. o maior valor de comissão e o nome do vendedor que recebeu

vendedores=[] #Primeira lista para os nomes dos vendedores
total_vendas=[] #Segunda lista, para suas vendas totais
comissao=[]  #Suas comissões
nomeEcomissao=[] #Lista para o item A
total_comissao=[] #Lista para o item B
vendas_abaixo=[] #Lista para o item D


x=0 #Contador
while x < 5: #Enquanto o contador for menor que 5, para uma lista de 5 pessoas/vendedores
    nome=str(input("Digite o nome do vendedore: ", )) #Solicitação dos nomes
    vendas=int(input("Digite o total de vendas: ", )) #E o total de seuas vendas
    css=vendas*0.15 #Calculo simples da comisão
    vendedores.append(nome) 
    total_vendas.append(vendas)
    nomeEcomissao.append(nome)
    nomeEcomissao.append(css)
    total_comissao.append(css)
    comissao.append(css)
    media=sum(total_vendas)/ len(total_vendas) #Calculo da media das vendas
    if vendas <= media: #Se o valor das vendas de 1 vendedor for menor que a media, ele entra para a lista daqueles que venderam abaixo da media
        vendas_abaixo.append(vendas)
    if css == max(comissao): #Identifica quem teve a menor comissão
        maiorcss=css
        melhorvdd=nome #E o melhor vendedor, ja que supostamente aquele que mais vende é o melhor
    x+=1
    

print("O nome e o valor de comissão de cada vendedor, respectivamente: ", nomeEcomissao)
print("O somatório das comissões pago pela empresa é: ", sum(total_comissao))
print("A média bruta das vendas: ", media)
print("E a quantidade de vendedores que performaram abaixo dessa media foi de: ", len(vendas_abaixo))
print("O maior valor de comissão é de: R$ ", maiorcss, "Do vendedor: ", melhorvdd)

