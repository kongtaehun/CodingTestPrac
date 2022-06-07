
import heapq
def solution(scoville, K):

    q = []
    for i in scoville:
        heapq.heappush(q,i)
    
    count = 0
    while True:
        first = heapq.heappop(q)
        if first >= K:
            return count
        elif len(q) ==0 and first < K:
            return -1
        second = heapq.heappop(q)
        new = first+second*2

        count +=1
        heapq.heappush(q,new)