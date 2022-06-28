n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())
count = 0


start = 0
end = n-1
# start와 end가 같으면 안댐
while start < end:
    temp = nums[start]+nums[end]
    if temp > x:
        end -= 1
    elif temp < x:
        start += 1
    if temp == x:
        count += 1
        end -= 1
        start += 1


print(count)
