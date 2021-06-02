vcompra = float(input("Qual o valor da compra? :"))

if vcompra < 20:
    vvenda = vcompra*1.45

else:
    vvenda = vcompra*1.3

lucro = vvenda-vcompra

print("O lucro e o valor da venda são, respectivamente: R$", lucro, "e R$", vvenda)
