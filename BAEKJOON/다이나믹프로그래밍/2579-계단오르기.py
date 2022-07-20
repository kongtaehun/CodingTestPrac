# 현재 계단을 올라오는 방법은
# 2개전 계단에서 :두계단을 한번에 올라오는 경우
# 3개전 계단에서 :두계단을 한번에 올라오고 한계단으로 올라오는경우
# 둘중에 더 큰 값이 현재계단을 오르는 가장 큰점수
# 3개를 연속으로 밟으면 안되기때문에

n = int(input())

costs = []
for i in range(n):
    costs.append(int(input()))
dp = [0]*(n)
if n == 1:
    print(costs[0])
elif n == 2:
    print(costs[0]+costs[1])
elif n == 3:
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
