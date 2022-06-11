# 입력
n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(int, input().split())))
link = []
for i in range(n):
    for j in range(i, n):
        cost = min(abs(temp[i][0]-temp[j][0]), abs(temp[i][1] -
                                                   temp[j][1]), abs(temp[i][2]-temp[j][2]))
        link.append((cost, i, j))

parant = [i for i in range(n)]


def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]


def union_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a < b:
        parant[b] = a
    else:
        parant[a] = b


link.sort()
result = 0
for g in link:
    cost, a, b = g
    if find_parant(parant, a) != find_parant(parant, b):
        union_parant(parant, a, b)
        result += cost
print(result)
