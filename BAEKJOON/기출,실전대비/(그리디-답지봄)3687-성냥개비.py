
import math

dp = [[0], [0], [1], [7], [4], [2], [6], [8], [1, 0],
      [1, 8], [2, 2], [2, 0], [2, 8], [6, 8], [8, 8]]
orders = [-2, -2, -5, -5, -5, -6, -7]
order_nums = [1, 1, 2, 2, 2, 6, 8]
for i in range(int(input())):
    n = int(input())
    biggest = []
    # 가장 큰값
    if n % 2 == 0:
        for i in range(n//2):
            biggest.append(1)
    else:
        biggest.append(7)
        for i in range((n-3)//2):
            biggest.append(1)
    # 가장작은값
    if n >= 15:
        temp = [8 for _ in range(math.ceil(n/7))]
        if n % 7 == 1:
            temp[0] = 1
            temp[1] = 0
        elif n % 7 == 2:
            temp[0] = 1
        elif n % 7 == 3:
            temp[0] = 2
            temp[1] = 0
            temp[2] = 0
        elif n % 7 == 4:
            temp[0] = 2
            temp[1] = 0
        elif n % 7 == 5:
            temp[0] = 2
        elif n % 7 == 6:
            temp[0] = 6
        smallest = temp
    else:
        smallest = dp[n]

    print(''.join(list(map(str, smallest))), ''.join(list(map(str, biggest))))
