from collections import Counter


if __name__ == '__main__':
    nums = list(input())
    temp = dict(Counter(nums))
    cnt0 = 0
    cnt1 = 0
    if '0' in nums:
        cnt0 = temp['0'] // 2
    if '1' in nums:
        cnt1 = temp['1'] // 2

    # 앞에서부터 1을 제거
    now = 0
    while cnt1 > 0:
        if nums[now] == '1':
            nums.pop(now)
            cnt1 -= 1
            continue
        now += 1

    # 뒤에서부터 0을 제거
    now = len(nums)-1
    while cnt0 > 0:

        if nums[now] == '0':
            nums.pop(now)
            cnt0 -= 1

        now -= 1
    for i in nums:
        print(i, end='')
