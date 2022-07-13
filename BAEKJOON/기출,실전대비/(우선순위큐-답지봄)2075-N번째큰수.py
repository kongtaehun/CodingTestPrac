#길이를 유지하면서 큐유지

import heapq
import sys
input = sys.stdin.readline
q = []
n = int(input())


arr = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(q, arr[i])

for i in range(n-1):
    temp = list(map(int, input().split()))
    for i in range(n):
        if temp[i] > q[0]:
            heapq.heappop(q)
            heapq.heappush(q, temp[i])

print(heapq.heappop(q))
