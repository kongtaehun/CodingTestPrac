# 모듈러연산으로 오버플로우 피하기
# dp 점화식
#dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
N = 1000001
dp = [0]*N
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, N):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009


for i in range(int(input())):
    n = int(input())
    print(dp[n])
