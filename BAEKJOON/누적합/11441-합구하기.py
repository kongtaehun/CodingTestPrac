n = int(input())
nums = list(map(int, input().split()))
summ = 0
for i in range(len(nums)):
    summ += nums[i]
    nums[i] = summ
m = int(input())
q = []
for i in range(m):
    a, b = map(int, input().split())
    q.append((a, b))

for a, b in q:
    print(nums[b-1] - (0 if a-2 < 0 else nums[a-2]))
