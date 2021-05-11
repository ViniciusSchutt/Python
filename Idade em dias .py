dias = int(input())

anos = 0
meses = 0

while dias > 30:
    if dias - 365 >= 0:
        anos += 1
        dias -= 365

        if dias - 30 >= 0:
            meses += 1
            dias -= 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')