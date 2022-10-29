n = int(input())
nums = list(map(int, input().split()))
# 음수도 가능
dp = [0]*(2002)
for i in nums:
    dp[i+1000] = 1

for i in range(2002):
    if dp[i] == 1:
        print(i-1000,end = ' ')
