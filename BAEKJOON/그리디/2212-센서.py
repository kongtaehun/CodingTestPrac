n = int(input())
k = int(input())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
diff = []
for i in range(len(nums)-1):
    diff.append(nums[i+1]-nums[i])
diff.sort(reverse=True)
print(sum(diff[k-1:]))
