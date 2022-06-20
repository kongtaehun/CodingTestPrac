def getCal(nums, leng):
    count = 0
    for i in nums:
        count += i//leng
    return count


n, target = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))

start = 0
end = max(nums)

while start < end:
    mid = (start+end)//2
    now = getCal(nums, mid)
    if now < target:
        end = mid-1
    else:
        start = mid+1
print(start)
