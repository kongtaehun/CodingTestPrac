import heapq
q = []
heapq.heappush(q, (4, 1))
heapq.heappush(q, (1, 1))
print(heapq.heappop(q))
