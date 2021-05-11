#Informar dois números e efetuar a adição. Caso o valor somado seja maior ou igual a 10, este deverá ser mostrado
#somando-se a ele mais 5; caso o valor somado não seja maior que 10, este deverá ser apresentado
#subtraindo-se 7.

num=int(input("Digite o primeiro número: "))
ndois=int(input("Digite o segundo número: "))
soma=num+ndois
if soma>9:
resultado=soma+5
else:
resultado=soma-7
print("O valor é: ", resultado)
