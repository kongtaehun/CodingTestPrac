import copy
h, w = map(int, input().split())
nums = list(map(int, input().split()))
nums_origin = copy.deepcopy(nums)
# 왼쪽 공백 벽부터 출발
empty_wall = h-nums[0]
for i in range(len(nums)):
    temp = h-nums[i]-empty_wall
    if temp <= 0:
        empty_wall = h - nums[i]
        nums[i] = h-nums[i]-empty_wall
    else:
        nums[i] = temp

# 오른쪽도 초기화
empty_wall = nums[-1]

for em in range(1, empty_wall+1):
    for i in range(len(nums)-1, -1, -1):

        if 1 <= nums[i]:
            nums[i] -= 1
        else:
            break


print(sum(nums[1:-1]))
