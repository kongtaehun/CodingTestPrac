from collections import deque
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))


result = []
stk = deque()
idx = 0
now = 1
stk.append(now)
result.append('+')
while idx < n:
    if len(stk) == 0:
        now += 1
        stk.append(now)
        result.append('+')
    elif stk[-1] == num[idx]:
        stk.pop()
        idx += 1
        result.append('-')
    else:
        if stk[-1] > num[idx]:
            result = -1
            break
        now += 1
        stk.append(now)
        result.append('+')

if result == -1:
    print("NO")
else:
    for i in result:
        print(i)
