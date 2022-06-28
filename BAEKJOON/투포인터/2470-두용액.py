# 같은 양의 두 용액을 혼합한 용액의 틈성 = 각 용액 특성값의 합
# 두개의 용액을 혼합하여 특성값 0 에 가깝게
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

start = 0
end = n-1
now = [start, end]
while start < end:
    temp_val = nums[start]+nums[end]
    now_val = nums[now[0]]+nums[now[1]]
    if abs(temp_val) < abs(now_val):
        now = [start, end]
        if temp_val < 0:
            start += 1
        else:
            end -= 1
    else:
        if temp_val < 0:
            start += 1
        else:
            end -= 1

print(nums[now[0]], nums[now[1]])
