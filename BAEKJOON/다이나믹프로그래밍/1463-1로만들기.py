n = int(input())
dp = [0]*(n+1)
if n == 1:
    print(1)
elif n == 2 or n == 3:
    print(1)
else:

    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        temp = []
        temp.append(1+dp[i-1])
        if i % 3 == 0:
            temp.append(1+dp[i // 3])
        if i % 2 == 0:
            temp.append(1+dp[i // 2])
        dp[i] = min(temp)

print(dp[-1])
