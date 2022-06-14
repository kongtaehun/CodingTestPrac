import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = set()
for i in range(n):
    S.add(input())


strSet = []
for i in range(m):
    strSet.append(input())


count = 0
for i in strSet:
    if i in S:
        count += 1


print(count)
