# find
def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]

# union


def union_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a < b:
        parant[b] = a
    else:
        parant[a] = b


n, m = map(int, input().split())
parant = [i for i in range(n+1)]

edges = []
costsum = 0


# 간선정보 받기
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


# 간선을 비용순으로 정렬
edges.sort()

costlast = 0
# 간선을 하나씩확인하며 사이클인지아닌지 확인
for i in edges:
    if find_parant(parant, i[1]) != find_parant(parant, i[2]):
        union_parant(parant, i[1], i[2])
        costsum = costsum+i[0]
        costlast = i[0]


print(costsum-costlast)
