# 모든 컴퓨터를 연결하는데 필요한 최소비용 => 최소스피닝트리 => 크루스칼알고리즘
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


if __name__ == '__main__':
    n = int(input())
    graph = []
    parant = [i for i in range(n+1)]
    for i in range(int(input())):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    graph.sort()
    result = 0
    for e in graph:
        cost, a, b = e
        if find_parant(parant, a) != find_parant(parant, b):
            union_parant(parant, a, b)
            result += cost
    print(result)
