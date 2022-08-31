# 1로만들지 2로만들지에 따라서 다르다
if __name__ == '__main__':
    nums = list(map(int, list(input())))
    result = [0, 0]
    if nums[0] == 0:
        result[0] += 1
    else:
        result[1] += 1
    now = nums[0]
    for i in range(1, len(nums)):

        if nums[i] != now:
            result[nums[i]] += 1
            now = nums[i]
    print(min(result))
