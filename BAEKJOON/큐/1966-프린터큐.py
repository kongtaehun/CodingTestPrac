from collections import deque
n = int(input())
docN = []
idxDoc = []
importance = []
idxlist = []
for i in range(n):
    a, b = map(int, input().split())
    numbers = list(map(int, input().split()))
    docN.append(a)
    idxDoc.append(b)
    importance.append(numbers)
    idxlist.append([x for x in range(a)])

result = []
for k in range(n):
    q = deque(importance[k])
    idxq = deque(idxlist[k])
    count = 0
    while q:
        # 가장 큰값이 어야 빠져나감
        maxx = max(q)
        now = q.popleft()
        nowidx = idxq.popleft()
        if now == maxx:
            count += 1
            if nowidx == idxDoc[k]:
                result.append(count)
                break

        else:
            q.append(now)
            idxq.append(nowidx)

for i in result:
    print(i)
