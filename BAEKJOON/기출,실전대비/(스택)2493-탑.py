from collections import deque
# 스택으로 구현하면 더쉬워진다는...

n = int(input())
nums = list(map(int, input().split()))
result = [0]*n
stk = deque()
stk.append((nums[0], 0))
for i in range(1, len(nums)):

    while stk:
        if stk[-1][0] >= nums[i]:
            result.append(stk[-1][1]+1)
            break
        else:
            stk.pop()
    if not stk:
        result.append(0)
    stk.append((nums[i], i))

print(" ".join(map(str, result)))
