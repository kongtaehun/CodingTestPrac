n = int(input())
nums = [list(map(int, input().split())) for i in range(n)]
for i in range(n-2, -1, -1):
    for j in range(len(nums[i])):
        nums[i][j] = max(nums[i+1][j]+nums[i][j], nums[i+1][j+1]+nums[i][j])

print(nums[0][0])
