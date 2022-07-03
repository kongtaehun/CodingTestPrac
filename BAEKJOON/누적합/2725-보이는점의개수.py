import sys
input = sys.stdin.readline


def calM(x, y):
    return x/y


dp = [0]*(1001)
inclinations = set()
dp[1] = 3
dp[2] = 5
inclinations.add(calM(1, 2))
for i in range(3, 1001):
    count = 0
    for j in range(1, i):
        inclination = calM(j, i)
        if inclination not in inclinations:
            count += 1
            inclinations.add(inclination)
    dp[i] = dp[i-1]+(2*count)


t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])
