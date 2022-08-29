import sys
input = sys.stdin.readline

# 나머지값을 구하는 문제이면 중간중간에 최대한 많이 나머지 연산을 넣어주는 것이 좋다
# (오버플로우가 발생할 수 있기 때문에!)
# 모듈러연산은 분배법칙이 성립하므로 아무리 많이해도 값은 같다.
dp = [[0, 0, 0] for i in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
dp[4] = [2, 0, 1]
for n in range(5, 100001):
    dp[n][0] = (dp[n-1][1]+dp[n-1][2]) % 1000000009
    dp[n][1] = (dp[n-2][0]+dp[n-2][2]) % 1000000009
    dp[n][2] = (dp[n-3][0]+dp[n-3][1]) % 1000000009
for i in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
