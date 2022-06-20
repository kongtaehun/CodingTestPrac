from collections import deque
n = int(input())
nums = list(map(int, input().split()))

stk = deque()
result = [-1 for i in range(n)]
stk.append(0)
for i in range(1, n):
    while stk and nums[stk[-1]] < nums[i]:
        result[stk.pop()] = nums[i]
    stk.append(i)
print(result)
