def find_team(parant, x):
    if parant[x] != x:
        parant[x] = find_team(parant, parant[x])
    return parant[x]


def union_team(parant, a, b):
    a = find_team(parant, a)
    b = find_team(parant, b)
    if a < b:
        parant[b] = a
    else:
        parant[a] = b


# 학생노드
n, m = map(int, input().split())
parant = [i for i in range(n+1)]
result = []
for i in range(m):
    typ, a, b = map(int, input().split())
    if typ == 0:
        union_team(parant, a, b)
    else:
        aa = find_team(parant, a)
        bb = find_team(parant, b)

        result.append("YES" if aa == bb else "NO")
for i in range(len(result)):
    print(result[i], end=' ')
