import sys
input = sys.stdin.readline
n, m = map(int, input().split())

N = set()
M = set()
for i in range(n):

    N.add(input().strip())
for i in range(m):
    temp = input().strip().split(',')

    for strr in temp:
        if strr in N:
            N.remove(strr)
    print(len(N))
