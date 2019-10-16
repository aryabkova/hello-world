def palindrom(n):
    n = str(n)
    if len(n) == 4:
        if n == n[::-1]:
            print("палиндром")
        else:
            print("не палиндром")
    elif len(n) == 3:
        n = '0' + n
        if n == n[::-1]:
            print("палиндром")
        else:
            print("не палиндром")
    elif len(n) == 2:
        n = '00' + n
        if n == n[::-1]:
            print("палиндром")
        else:
            print("не палиндром")
    elif len(n) == 1:
        n = '000' + n
        if n == n[::-1]:
            print("палиндром")
        else:
            print("не палиндром")
    else:
        print("введите число < 10000")
palindrom(330)
palindrom(4554)
palindrom(0)
palindrom(23)
palindrom(10000)