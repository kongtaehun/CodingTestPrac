import heapq
import sys
input = sys.stdin.readline
rightQ = []
leftQ = []
n = int(input())


for i in range(n):
    a = int(input())
    if len(rightQ) == len(leftQ):
        heapq.heappush(leftQ, -a)
    else:
        heapq.heappush(rightQ, a)

    if len(rightQ) > 0 and len(leftQ) > 0:
        if -leftQ[0] > rightQ[0]:
            rv = heapq.heappop(rightQ)
            lv = -heapq.heappop(leftQ)
            heapq.heappush(rightQ, lv)
            heapq.heappush(leftQ, -rv)
    print(-leftQ[0])
