n = int(input())

costs = []
for i in range(n):
    costs.append(int(input()))
dp = [0]*(n)
if n == 1:
    print(costs[0])
elif n == 2:
    print(costs[0]+costs[1])
elif n==3:
    dp[0] = costs[0]
    dp[1] = costs[0]+costs[1]
    print(max(costs[1]+costs[2], dp[0]+costs[2]))

else:
    dp[0] = costs[0]
    dp[1] = costs[0]+costs[1]
    dp[2] = max(costs[1]+costs[2], dp[0]+costs[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2]+costs[i], dp[i-3]+costs[i-1]+costs[i])
    print(dp[-1])
