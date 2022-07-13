import sys
input = sys.stdin.readline

a = [0]*(100001)
n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
results = []
for i in range(n):
    a = [0]*(100001)
    count = 0
    for i in range(i, n):
        a[nums[i]] += 1
        if a[nums[i]] > k:
            results.append(count)
            break
        else:
            count += 1

results.append(count)
print(max(results))
