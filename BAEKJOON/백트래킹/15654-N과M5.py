from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

temp = list(permutations(nums, m))
temp.sort()
for i in temp:
    for j in i:
        print(j, end=' ')
    print()
