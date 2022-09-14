import heapq
# 10,20,40이 있음
# 그리디? 작은거 먼저 푼다
nums = []
for i in range(int(input())):
    heapq.heappush(nums, int(input()))
result = 0
while len(nums) > 1:
    now = heapq.heappop(nums)
    next = heapq.heappop(nums)
    result += now+next
    heapq.heappush(nums, now+next)
    
print(result)
