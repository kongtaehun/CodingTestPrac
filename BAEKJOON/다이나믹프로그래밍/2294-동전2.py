
# bfs는 메모리 초과이다.
from collections import deque
dp = []
q = set()
n, k = map(int, input().split())
nums = []
for i in range(n):
    a = int(input())
    nums.append(a)
    q.add((a, 1))


def bfs():
    while q:
        now, count = q.pop()
        for i in range(n):
            q.add((nums[i]+now, count+1))
            if nums[i]+now == k:
                return count+1


print(bfs())
