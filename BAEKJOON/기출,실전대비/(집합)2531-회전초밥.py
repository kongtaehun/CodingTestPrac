n, d, k, c = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))


result = 0
for i in range(len(nums)):
    temp_set = set()
    for kk in range(k):
        temp_set.add(nums[(i+kk) % len(nums)])
    temp_set.add(c)
    result = max(len(temp_set), result)
print(result)
