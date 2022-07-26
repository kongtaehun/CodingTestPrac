# 크루스칼?!
# 최소 스패닝 트리를 찾은 다음에
# 포함된 경로 중 가장 비용이 큰 경로를 없앤다.
import sys
input = sys.stdin.readline


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
    n, m = map(int, input().split())
    graph = []
    parant = [i for i in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        # 양방향이라고 반대로 해줄 필요없다(연결의 의미이므로)
        graph.append((c, a, b))
    graph.sort()

    result = 0
    max_cost = 0
    for edge in graph:
        cost, a, b = edge
        if find_parant(parant, a) != find_parant(parant, b):
            union_parant(parant, a, b)
            result += cost
            max_cost = max(cost, max_cost)
    print(result-max_cost)
