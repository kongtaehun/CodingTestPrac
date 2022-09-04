def check(nums):
    cnt = 0
    for i in range(7):
        if nums[i] < nums[i+1]:
            cnt += 1

    if cnt == 7:
        return 'ascending'
    cnt = 0
    for i in range(7):
        if nums[i] > nums[i+1]:
            cnt += 1
    if cnt == 7:
        return 'descending'
    else:
        return 'mixed'


nums = list(map(int, input().split()))
print(check(nums))
