# 1. 2차원 DP테이블
# 2. 현재 비교하는 문자와 같을 경우 위에서 +1
if __name__ == '__main__':
    a = input()
    b = input()
    dp = [[0]*(len(b)+1) for i in range(len(a)+1)]

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])
