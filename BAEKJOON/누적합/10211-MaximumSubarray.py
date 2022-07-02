t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    summ = 0
    for i in range(len(nums)):
        summ += nums[i]
        nums[i] = summ
    maxx = -int(1e9)
    for i in range(n):
        maxx = max(nums[i], maxx)
        for j in range(0, i):
            maxx = max(nums[i]-nums[j], maxx)
    print(maxx)
