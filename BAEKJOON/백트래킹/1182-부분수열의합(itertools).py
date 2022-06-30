from itertools import combinations


n, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0


for i in range(1, len(nums)+1):
    
    for j in list(combinations(nums, i)):
        if sum(j) == S:
            count += 1
print(count)
