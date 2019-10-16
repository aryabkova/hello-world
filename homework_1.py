def parking(day,hour):
    if 19.00 <= hour < 21.00:
        print('both')
    if  (0 < hour < 19.00 and day%2 ==0) or (21 < hour < 24.00 and day%2 !=0):
        print('right')
    if  (0 < hour < 19.00 and day%2 !=0) or (21 < hour < 24.00 and day%2 ==0):
        print('left')

parking(8, 19.30)
parking(9, 19.20)
parking(16, 7.15)
parking(23, 22.22)
