def decentNumber(n):
    x_max, x, y = n // 3, 0, 0
    for i in range(x_max, -1, -1):
        if (n-3*i) % 5 == 0:
            x, y = i*3, n-3*i
            print('5'*x+'3'*y)
            return
    print(-1)
#Simply try to maximize the number of 5's and place them before 3's   
