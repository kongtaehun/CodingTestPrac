# 최소스패닝트리이면 크루스칼
import math


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


def getDistance(now, another):
    return math.sqrt(math.pow(another[0]-now[0], 2)+math.pow(another[1]-now[1], 2))


if __name__ == '__main__':
    n = int(input())
    star = [list(map(float, input().split())) for i in range(n)]
    graph = []
    for now in range(len(star)):
        for another in range(len(star)):
            if now != another:
                graph.append(
                    (getDistance(star[now], star[another]), now, another))

    graph.sort()
    parant = [i for i in range(n)]
    result = 0
    for i in graph:
        cost, a, b = i
        if find_parant(parant, a) != find_parant(parant, b):
            union_parant(parant, a, b)
            result += cost
    print("%0.2f" % result)
