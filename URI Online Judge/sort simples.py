a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print(a)
    print(b)
    print(c)

if a < c < b:
    print(a)
    print(c)
    print(b)

if b < a < c:
    print(b)
    print(a)
    print(c)

if b < c < a:
    print(b)
    print(c)
    print(a)

if c < a < b:
    print(c)
    print(a)
    print(b)

if c < b < a:
    print(c)
    print(b)
    print(a)

print('')
print(a)
print(b)
print(c)

''' outra forma
x = input().split()
a, b, c = x
a = int(a)
b = int(b)
c = int(c)


if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b
print(f)
print(e)
print(d)
print()
print(a)
print(b)
print(c)

'''
