from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
result = []

answer = [-1 for i in range(n)]

stk = deque()
stk.append(0)
idx = 1
while idx < n:
    if len(stk) != 0 and numbers[idx] > numbers[stk[-1]]:
        answer[stk.pop()] = numbers[idx]
    else:
        stk.append(idx)
        idx += 1
