from collections import deque
import sys
input = sys.stdin.readline
q = deque()
for i in range(int(input())):
    a = list(map(str, input().split()))
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    # print(q)
