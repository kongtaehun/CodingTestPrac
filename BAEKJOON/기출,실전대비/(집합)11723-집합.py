import sys
input = sys.stdin.readline
a = set()
for i in range(int(input())):
    temp = list(input().split())

    if temp[0] == 'add':
        a.add(int(temp[1]))
    elif temp[0] == 'remove':
        if int(temp[1]) in a:
            a.remove(int(temp[1]))
    elif temp[0] == 'check':
        if int(temp[1]) in a:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if int(temp[1]) in a:
            a.remove(int(temp[1]))
        else:
            a.add(int(temp[1]))
    elif temp[0] == 'all':
        a = set([i for i in range(1, 21)])
    elif temp[0] == 'empty':
        a = set()
