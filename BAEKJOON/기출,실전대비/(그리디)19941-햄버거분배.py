n, k = map(int, input().split())
nums = list(map(str, list(input())))
count = 0
for i in range(len(nums)):
    if nums[i] == 'H':
        for j in range(-k, k+1):
            if j == 0 or i+j < 0 or i+j >= n:
                continue
            else:
                if nums[i+j] == "P":
                    count += 1
                    nums[i+j] = 0
                    break
print(count)
