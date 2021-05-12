#5=Escreva uma função que receba como parâmetro a nota de um estudante, converte o
#valor de nota para um conceito (A, B, C, D, E e F). Imprima o resultado dentro da função.

nota=int(input("Entre com a nota do estudante (valores de 0 a 90): "))

a='A'
b='B'
c='C'
d='D'
e='E'
f='F'

while nota >=0 and nota<=90:
    
    if nota>=0 and nota<=15:
        conceito=f
        print("O conceito do aluno é: ", conceito)
        break
    elif nota>15 and nota<=30:
        conceito=e
        print("O conceito do aluno é: ", conceito)
    elif nota>30 and nota<=45:
        conceito=d
        print("O conceito do aluno é: ", conceito)
        break
    elif nota>45 and nota<=60:
        conceito=c
        print("O conceito do aluno é: ", conceito)
        break
    elif nota>60 and nota<=75:
        conceito=b
        print("O conceito do aluno é: ", conceito)
        break
    elif nota>75 and nota <=90:
        conceito=a
        print("O conceito do aluno é: ", conceito)
        break
        
        

    
