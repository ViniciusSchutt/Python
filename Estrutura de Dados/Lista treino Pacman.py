a = [int(input("Valor x0: ")), int(input("Valor y0: ")), int(input("Valor x1 (onde x1>x0): ")), int(input("Valor y1 (onde y1>yo): "))]
b = [int(input("Valor x0: ")), int(input("Valor y0: ")), int(input("Valor x1 (onde x1>x0): ")), int(input("Valor y1 (onde x1>x0): "))]

def pacman():
    for i in range (3):
        if b[i] == a[i]:
            result = 1
        elif b[i] - a[i] < 2:
            result = 1
        else:
            result = 0

    print(result)

pacman()



