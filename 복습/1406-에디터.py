from collections import deque
# deque
# 왼쪽 stk 오른쪽 stk
# 커서를 왼쪽으로 옮기기 - Lstk pop Rstk appendleft
# 커서를 오른쪽으로 옮기기 - Lstk append Rstk popleft
# 삭제 - Lstk[-1] 삭제
# 삽입 - Lstk append

lStk = deque(list(input()))
rStk = deque()
for i in range(int(input())):
    a = list(map(str, input().split()))
    if a[0] == 'L':
        if len(lStk)!=0:
            rStk.appendleft(lStk.pop())
    elif a[0] == 'D':
        if len(rStk)!=0:
            lStk.append(rStk.popleft())
    elif a[0] == 'B':
        if len(lStk)!=0:
            lStk.pop()
    elif a[0] == 'P':
        lStk.append(a[1])

print(''.join(lStk+rStk))
