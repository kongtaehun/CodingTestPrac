

def pickBook(nums):

    neg_mx = [0, 0]
    pos_mx = [0, 0]
    # 음수 양수 중 가장 긴거리를 가진 쪽구하기
    for i in range(len(nums)):
        if nums[i] < 0:
            if nums[i] < neg_mx[0]:
                neg_mx[0] = nums[i]
                neg_mx[1] = i
        else:
            if nums[i] > pos_mx[0]:
                pos_mx[0] = nums[i]
                pos_mx[1] = i

    last_elements = []
    if abs(neg_mx[0]) > abs(pos_mx[0]):
        last_elements.append(neg_mx[0])
        nums = nums[:neg_mx[1]] + nums[neg_mx[1]+1:]
        for i in range(m-1):
            if len(nums) <= 0:
                break
            second_val = min(nums)
            if second_val > 0:
                break
            second_idx = nums.index(second_val)
            nums = nums[:second_idx] + nums[second_idx+1:]
            last_elements.append(second_val)
    else:
        last_elements.append(pos_mx[0])
        nums = nums[:pos_mx[1]] + nums[pos_mx[1]+1:]
        for i in range(m-1):
            if len(nums) <= 0:
                break
            second_val = max(nums)
            if second_val < 0:
                break
            second_idx = nums.index(second_val)
            nums = nums[:second_idx] + nums[second_idx+1:]
            last_elements.append(second_val)
    return nums, last_elements


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums, last_elements = pickBook(nums)
    result = 0
    if last_elements[0] < 0:
        result += abs(min(last_elements))
    else:
        result += abs(max(last_elements))

    while len(nums) != 0:
        nums, pick_elements = pickBook(nums)
        if pick_elements[0] < 0:
            result += abs(min(pick_elements))*2
        else:
            result += abs(max(pick_elements))*2
    print(result)
