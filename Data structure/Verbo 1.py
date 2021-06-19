#Programa que realiza a conjugação de verbos

print("Informe um verbo qualquer: ")
verbo = list(input())

def funcaoSimples():
    pos = len(verbo) -2

    if verbo[pos] == 'a':
        verbo.pop()
        verbo.pop()
        verbo.append('o')
        print(f"Eu {''.join(verbo)}")

        verbo.pop()
        verbo.append('a')
        verbo.append('s')
        print(f"Tu {''.join(verbo)}")

        verbo.pop()
        print(f"Ele {''.join(verbo)}")

        verbo.append('m')
        verbo.append('o')
        verbo.append('s')
        print(f"Nós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.append('i')
        verbo.append('s')
        print(f"Vós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.append('m')
        print(f"Eles {''.join(verbo)}")

    if verbo[pos] == 'e':
        verbo.pop()
        verbo.pop()
        verbo.append('o')
        print(f"Eu {''.join(verbo)}")

        verbo.pop()
        verbo.append('e')
        verbo.append('s')
        print(f"Tu {''.join(verbo)}")

        verbo.pop()
        print(f"Ele {''.join(verbo)}")

        verbo.append('m')
        verbo.append('o')
        verbo.append('s')
        print(f"Nós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.append('i')
        verbo.append('s')
        print(f"Vós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.append('m')
        print(f"Eles {''.join(verbo)}")

    if verbo[pos] == 'i':
        verbo.pop()
        verbo.pop()
        verbo.append('o')
        print(f"Eu {''.join(verbo)}")

        verbo.pop()
        verbo.append('e')
        verbo.append('s')
        print(f"Tu {''.join(verbo)}")

        verbo.pop()
        print(f"Ele {''.join(verbo)}")

        verbo.append('m')
        verbo.append('o')
        verbo.append('s')
        print(f"Nós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.append('i')
        verbo.append('s')
        print(f"Vós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.append('m')
        print(f"Eles {''.join(verbo)}")

    if verbo[pos] == 'o':
        verbo.pop()
        verbo.append('n')
        verbo.append('h')
        verbo.append('o')
        print(f"Eu {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.append('õ')
        verbo.append('e')
        verbo.append('s')
        print(f"Tu {''.join(verbo)}")

        verbo.pop()
        print(f"Ele {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.append('o')
        verbo.append('m')
        verbo.append('o')
        verbo.append('s')
        print(f"Nós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.append('n')
        verbo.append('d')
        verbo.append('e')
        verbo.append('s')
        print(f"Vós {''.join(verbo)}")

        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.pop()
        verbo.append('e')
        verbo.append('m')
        print(f"Eles {''.join(verbo)}")


funcaoSimples()
