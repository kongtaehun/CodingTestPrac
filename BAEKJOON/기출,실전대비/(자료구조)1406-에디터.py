# 두개의 스택을 이용하여
# 두번쨰 수택의 top이 cursor이다.

from collections import deque


stk1 = deque(list(input()))
stk2 = deque()
for i in range(int(input())):
    command = list(map(str, input().split()))
    # 커서는 현재위치에 오른쪽에 있다고 생각
    if command[0] == 'L':
        # 이동
        if len(stk1) > 0:
            stk2.appendleft(stk1.pop())

    elif command[0] == 'D':
        if len(stk2) > 0:
            stk1.append(stk2.popleft())
    elif command[0] == 'B':
        if len(stk1) > 0:
            stk1.pop()

    elif command[0] == 'P':
        stk1.append(command[1])
    # print(stk1, stk2)
print(''.join(stk1) + ''.join(stk2))
