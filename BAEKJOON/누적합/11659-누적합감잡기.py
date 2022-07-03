n, m = map(int, input().split())
nums = list(map(int, input().split()))
summ = 0
for i in range(len(nums)):
    summ += nums[i]
    nums[i] = summ

q = []
for i in range(m):
    a, b = map(int, input().split())
    q.append((a, b))

for i in q:
    if (i[0]-1) == 0:
        print(nums[(i[1]-1)])
    else:
        print(nums[(i[1]-1)]-nums[(i[0]-2)])
