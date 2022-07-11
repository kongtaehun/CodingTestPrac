import sys
input = sys.stdin.readline


dp = [[0]*3 for i in range(10001)]
dp[0] = [1, 0, 0]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, 10001):
    dp[i][0] = 1
    dp[i][1] = i//2
    dp[i][2] = sum(dp[i-3])

for i in range(int(input())):
    print(sum(dp[int(input())]))
