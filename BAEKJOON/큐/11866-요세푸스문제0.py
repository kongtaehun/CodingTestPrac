from collections import deque
n, k = map(int, input().split())
num = deque()
for i in range(n):
    num.append(i+1)
result = []
while len(num) > 0:
    for i in range(k-1):
        num.append(num.popleft())
    result.append(num.popleft())
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(str(result[len(result)-1])+'>')
