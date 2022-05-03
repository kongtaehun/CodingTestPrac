# 크루스칼 한 결과

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


# 입력
all_cost = 0
n, m = map(int, input().split())
graph = []
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
    all_cost += c
parant = [i for i in range(n)]

graph.sort()

result = 0
for g in graph:
    cost, a, b = g
    if find_parant(parant, a) != find_parant(parant, b):
        union_parant(parant, a, b)
        result += cost
print(all_cost-result)
