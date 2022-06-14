from collections import deque
n = int(input())
q = deque()
for i in range(n):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)
print(q[0])
