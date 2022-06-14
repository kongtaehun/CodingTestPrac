from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
stk = deque()
for i in range(n):
    commands = list(map(str, input().split()))
    if commands[0] == 'push':
        stk.append(commands[1])
    elif commands[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif commands[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == 'top':

        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])

    elif commands[0] == 'size':
        print(len(stk))
