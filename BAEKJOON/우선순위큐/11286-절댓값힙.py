import sys
import heapq
input = sys.stdin.readline
q = []
n = int(input())
for i in range(n):
    temp = int(input())

    # 0입력
    if temp == 0:
        if len(q) == 0:
            print(0)
        else:
            popval = heapq.heappop(q)
            print(popval[1])

    # 숫자 push
    else:
        heapq.heappush(q, (abs(temp), temp))
