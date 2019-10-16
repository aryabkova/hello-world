def deleteduplicates(a):
    b = []
    for i in a:
        if a.count(i) >= 2 and i not in b:
            b.append(i)
        elif a.count(i) == 1:
            b.append(i)
    print(b)
a = [2, 'cat', 7, 2, 9, 'cat', 7, 42]
deleteduplicates(a)