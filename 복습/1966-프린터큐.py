import sys
from collections import deque
input = sys.stdin.readline


def getOrder(nums, x):
    idx = [i for i in range(len(nums))]
    idxQ = deque(idx)
    q = deque(nums)
    result = []
    while q:

        now = q.popleft()
        now_idx = idxQ.popleft()
        if not q:
            result.append(now_idx)
            break

        if q and now >= max(q):
            result.append(now_idx)
        else:
            q.append(now)
            idxQ.append(now_idx)
    answer = list(result)
    answer_idx = answer.index(x)
    return answer_idx


t = int(input())
answer = []
for i in range(t):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    answer.append(getOrder(nums, x)+1)

for i in answer:
    print(i)
