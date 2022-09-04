import sys
input = sys.stdin.readline


def find(parant, x):
    if parant[x] != x:
        parant[x] = find(parant, parant[x])
    return parant[x]


def union(parant, a, b):
    a = find(parant, a)
    b = find(parant, b)
    if a != b:
        # 두 개가 연결되어있지 않을 때
        parant[b] = a
        # b의 값을 루트인 a에 더한다.
        cnt[a] += cnt[b]


for i in range(int(input())):
    f = int(input())
    parant = {}
    # a가 루트인 그룹의 요소개수
    cnt = {}
    for i in range(f):
        a, b = map(str, input().split())
        if a not in parant:
            parant[a] = a
            cnt[a] = 1
        if b not in parant:
            parant[b] = b
            cnt[b] = 1
        union(parant, a, b)
        # a의 루트에 해당하는 카운트
        print(cnt[parant[a]])
    # parant.values()중에서 a의 값의 개수

    # print(graph)
