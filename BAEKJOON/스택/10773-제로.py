from collections import deque
n = int(input())
nums = deque()
for i in range(n):
    inputnum = int(input())
    if inputnum == 0:
        nums.pop()
    else:
        nums.append(inputnum)

print(sum(nums))
