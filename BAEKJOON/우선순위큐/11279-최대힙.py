import sys
import heapq
input = sys.stdin.readline
q = []
n = int(input())
for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(q) == 0:
            print(0)
        else:
            popval = -heapq.heappop(q)
            print(popval)
    else:
        heapq.heappush(q, -temp)
