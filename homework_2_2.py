print('Введите количество решений (n):')
n = int(input())
homedist = 0
alldist = 0
for i in range (1, n+1):
    alldist = alldist + 1/i
    if i % 2 != 0:
        homedist = homedist + 1/i
    elif i % 2 == 0:
        homedist = homedist - 1/i
print('Расстояние до дома равно', homedist, 'км')
print('Общий пройденный путь равен', alldist, 'км')
