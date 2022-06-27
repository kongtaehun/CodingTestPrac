import sys
input = sys.stdin.readline


n, k = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]*n
prefix_sum[0] = nums[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1]+nums[i]
result = []
for i in range(k):
    start, end = map(int, input().split())
    if start == 1:
        result.append(prefix_sum[end-1])
    else:
        result.append(prefix_sum[end-1] - prefix_sum[start-2])

for i in result:
    print(i)
