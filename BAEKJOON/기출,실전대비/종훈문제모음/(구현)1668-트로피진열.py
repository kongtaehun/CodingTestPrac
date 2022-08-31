# 오름차순의 개수를 센다

from collections import deque
n = int(input())
trophy = []
for i in range(n):
    trophy.append(int(input()))

now = trophy[0]
cnt = 0
for i in range(1, n):
    if trophy[i] > now:
        now = trophy[i]
        cnt += 1
print(cnt+1)
now = trophy[-1]
cnt = 0
for i in range(n-2, -1, -1):
    if trophy[i] > now:
        now = trophy[i]
        cnt += 1
print(cnt+1)
