# 메모리초과발생 : dp내의 중복된 요소 빼기 위해 set사용

n, s, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [set([s])]+[set() for i in range(n)]
for i in range(n):
    for j in list(dp[i]):
        if j+nums[i] <= m:
            dp[i+1].add(j+nums[i])
        if 0 <= j-nums[i]:
            dp[i+1].add(j-nums[i])

if len(dp[-1]) == 0:
    print(-1)
else:
    print(max(dp[-1]))
