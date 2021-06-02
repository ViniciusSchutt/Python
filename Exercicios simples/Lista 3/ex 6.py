m=[[3,2,4,6,2,20,24,100,98,108],[349,406,38,9,72,239,405,754,23,1],[20,39,300,432,974,102,84,2,233,543],[123,32,312,321,975,129,329,443,102,199],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]
ms=[[],[],[],[],[],[],[],[],[],[]]
l7=[]
z=0
y=0
while z<10:
    x=0
    while x<6:
        n=m[x][y]
        ms[z].append(n)
        x+=1
    y+=1
    z+=1
x=0
while x<10:
    l=sum(ms[x])
    l7.append(l)
    x+=1
m.append(l7)
print('RESULTADOS:')
print('1ª coluna: ',l7[0])
print('2ª coluna: ',l7[1])
print('3ª coluna: ',l7[2])
print('4ª coluna: ',l7[3])
print('5ª coluna: ',l7[4])
print('6ª coluna: ',l7[5])
print('7ª coluna: ',l7[6])
print('8ª coluna: ',l7[7])
print('9ª coluna: ',l7[8])
print('10ª coluna: ',l7[9])
