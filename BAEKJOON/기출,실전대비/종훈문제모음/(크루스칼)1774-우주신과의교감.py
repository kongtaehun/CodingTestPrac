import math
# 최소스패닝트리 만들기!


def getCost(a, b):
    x1, y1 = coords[a][0], coords[a][1]
    x2, y2 = coords[b][0], coords[b][1]
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]


def union_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a > b:
        parant[a] = b
    else:
        parant[b] = a


if __name__ == '__main__':
    n, m = map(int, input().split())
    coords = [(0, 0)]
    parant = [i for i in range(n+1)]
    for i in range(n):
        a, b = map(int, input().split())
        coords.append((a, b))

    for i in range(m):
        a, b = map(int, input().split())
        # union해서 연결해주기!
        union_parant(parant, a, b)

    graph = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            graph.append((getCost(i, j), i, j))
    graph.sort()

    result = 0
    for i in graph:
        cost, a, b = i
        if find_parant(parant, a) != find_parant(parant, b):
            union_parant(parant, a, b)
            result += cost

    print("%0.2f" % (result))
    # print("%0.2f" % (result-origin_result))
    # print(math.ceil((result-origin_result)))
