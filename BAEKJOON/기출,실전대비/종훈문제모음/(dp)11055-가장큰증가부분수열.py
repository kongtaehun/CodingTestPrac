# 가장 최근의 작은 수를 dp에서 꺼낸다.
n = int(input())
nums = list(map(int, input().split()))
dp = [0]*(n)
dp[0] = nums[0]

for i in range(n):
    # 나보다 작은 거중에 Max를 구한다.
    dp[i] = nums[i]
    max_dp = 0
    for j in range(i, -1, -1):
        if nums[i] > nums[j]:
            max_dp = max(dp[j], max_dp)
    dp[i] += max_dp
print(max(dp))
