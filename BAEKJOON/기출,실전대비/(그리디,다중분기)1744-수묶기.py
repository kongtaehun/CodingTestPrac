

def solution():
    n = int(input())
    nums = [0]*(n)
    result = 0
    for i in range(n):
        nums[i] = int(input())
    # 길이가 1인 경우 예외
    # 음수의 개수가 홀수 개이고 0이 존재하면 절대값 가장 작은 음수를 0으로 압출
    nums.sort(reverse=True)
    negative_count = 0
    min_negative_idx = -1
    zero_count = 0
    zero_idx = -1
    for i in range(n):
        if nums[i] < 0:
            negative_count += 1
            if min_negative_idx == -1:
                min_negative_idx = i
        elif nums[i] == 0:
            zero_count += 1
            if zero_idx == -1:
                zero_idx = i
    if zero_count >= 1 and negative_count % 2 != 0:
        nums = nums[:min_negative_idx]+nums[min_negative_idx+1:]
        for i in range(len(nums)):
            if nums[i] == 0:
                nums = nums[:i]+nums[i+1:]
                n = len(nums)
                break

    new_nums = []
    # 0과 1제거
    for i in range(n):
        if nums[i] == 0:
            pass
        elif nums[i] == 1:
            result += 1
        else:
            new_nums.append(nums[i])
    nums = new_nums
    n = len(nums)

    #양수부분(홀수개 or 짝수개임)
    while True:
        if len(nums) >= 2:
            if nums[0] > 0 and nums[1] > 0:
                a = nums.pop(0)
                b = nums.pop(0)
                result += a*b
            else:
                break
        else:
            break

    # 음수부분
    while True:
        if len(nums) >= 2:
            if nums[-1] < 0 and nums[-2] < 0:
                a = nums.pop()
                b = nums.pop()
                result += a*b
            else:
                break
        else:
            break

    if nums:
        for i in nums:
            result += i
    print(result)


solution()
