# 규칙은 (n-2)+(n-3)임
# 입력
t = int(input())
result = []

# 파도반수열


def w(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = w(n-2)+w(n-3)
        return dp[n]


for i in range(t):
    dp = [0 for i in range(101)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    n = int(input())
    result.append(w(n))

for i in range(t):
    print(result[i])
