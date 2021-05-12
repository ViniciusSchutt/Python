#03 o banco XXX concederá um crédito especial aos seus clientes de acordo com o salário médio no último ano. Elaborar um algoritmo que leia o saldo médio do
#cliente e calcule o valor do crédito de acordo com a tabela a seguir. Imprimir uma mensagem informando o saldo médio e o valor do crédito.
#SALDO MEDIO           PERCENTUAL
#de 0 a 500.00         nenhum crédito
#de 500.01 a 1000.00   30% do valor do saldo médio
#De 1000.01 a 3000.00  40% do valor do saldo médio
#Acima de 3000.00      50% do valor do saldo médio

saldomedio=float(input("Saudações cliente, como vai? Por favor, informe seu saldo médio: "))

if saldomedio > 0 and saldomedio <=500.00:
    credito=0
    print("Sentimos muitíssimo informar senhor(a) mas, com esse saldo, não há crédito a ser concedido, lamentavelmente. Mas não desanime!")

elif saldomedio > 500.00 and saldomedio <= 1000.00:
    credito=saldomedio*0.3
    print("'Chá-Ching $*-*$' - Congratulações! O valor do seu crédito especial é de: R$", credito)

elif saldomedio > 1000.01 and saldomedio <= 3000.00:
    credito=saldomedio*0.4
    print("'Chá-Ching $*-*$' - Congratulações! O valor do seu crédito especial é de: R$", credito)

elif saldomedio > 3000.00:
    credito=saldomedio*0.5
    print("'Chá-Ching $*-*$' - Congratulações! O valor do seu crédito especial é de: R$", credito)

else:
    print("Valor de crédito inválido, o senhor(a) pode ter digitando um valor negativo! Tente novamente!")
