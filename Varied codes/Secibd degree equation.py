# Crie uma função que receba três valores, 'a', 'b' e 'c', que são os coeficientes de uma
# equação do segundo grau e retorne o valor do delta, que é dado por 'b² - 4ac’.

import math

print("Esse programa calcula e retorna o valor de Delta de uma "
      "função do segundo grau. Por favor siga as instruções a seguir.")
a = int(input("Qual o valor do coeficiente 'a' da função? "))
b = int(input("Qual o valor do coeficiente 'b' da função? "))
c = int(input("Qual o valor do coeficinete 'c' da função? "))

delta = ((b*b)-(4*a*c))

print("O valor de Delta desta equação é: ", delta)
