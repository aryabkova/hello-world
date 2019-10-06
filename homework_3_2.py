#сложение:
def plus(a, b):
    if len(a) < len(b):
        while len(a) < len(b):
            a.insert(0, 0)
    elif len(a) > len(b):
        while len(a) > len(b):
            b.insert(0, 0)
    sum = []
    aa = a[::-1]
    bb = b[::-1]
    c = 0
    for i in range(len(aa)):
        if aa[i] + bb[i] + c >= 10:
            sum.append(aa[i] + bb[i] + c - 10)
            c = 1
        elif aa[i] + bb[i] + c < 10:
            sum.append(aa[i] + bb[i] + c)
            c = 0
    if c == 1:
        sum.append(1)
    print(sum[::-1])
a = [8, 9, 8, 3]
b = [2, 7, 2, 1]
plus(a, b)
x = [8, 9, 8]
y = [2, 7, 2, 1]
plus(x, y)
z = [8, 9, 8, 3]
v = [2, 7]
plus(z, v)

#Вычитание:
def minus(a, b):
    if len(a) < len(b):
        while len(a) < len(b):
            a.insert(0, 0)
        raz = []
        c = 0
        aa = a[::-1]
        bb = b[::-1]
        for i in range(len(aa)):
            if bb[i] > aa[i]:
                raz.append(bb[i] - aa[i] - c)
                c = 0
            elif bb[i] < aa[i]:
                raz.append(bb[i] + 10 - aa[i] - c)
                c = 1
        print('минус', raz[::-1])
    elif len(a) > len(b):
        while len(a) > len(b):
            b.insert(0, 0)
        raz = []
        c = 0
        aa = a[::-1]
        bb = b[::-1]
        for i in range(len(aa)):
            if aa[i] > bb[i]:
                raz.append(aa[i] - bb[i] - c)
                c = 0
            elif aa[i] < bb[i]:
                raz.append(aa[i] + 10 - bb[i] - c)
                c = 1
        print(raz[::-1])
a = [8, 9, 8, 3]
b = [7, 2, 5]
minus(a, b)
x = [8, 3]
y = [7, 2, 5]
minus(x, y)
