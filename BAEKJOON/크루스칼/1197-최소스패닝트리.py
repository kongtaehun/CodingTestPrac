# 크루스칼알고리즘
# 1. graph 입력형태에 유의
# 2. parant베열 선언과 정렬에 유의
def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]


def union_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    # 더작은거로 초기화
    if a < b:
        parant[b] = a
    else:
        parant[a] = b


if __name__ == '__main__':
    v, e = map(int, input().split())

    parant = [i for i in range(v+1)]
    graph = []
    for i in range(e):
        a, b, cost = map(int, input().split())
        graph.append((cost, a, b))
        # 양방향인지 고민해봐야함
    graph.sort()
    result = 0
    for i in graph:
        cost, a, b = i
        if find_parant(parant, a) != find_parant(parant, b):
            union_parant(parant, a, b)
            result += cost
    print(result)
