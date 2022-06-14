from collections import deque


def check(strr):
    stk = deque()
    for i in strr:
        if i == '(':
            stk.append(1)
        else:
            if len(stk) == 0:
                return False
            else:
                stk.pop()
    if len(stk) == 0:
        return True
    else:
        return False


n = int(input())
result = []
for i in range(n):
    result.append(check(input()))

for i in result:
    if i:
        print('YES')
    else:
        print('NO')
