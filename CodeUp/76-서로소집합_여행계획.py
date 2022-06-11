# 연결성을 바탕으로 같은 집합에 속해있으면 된다./
def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]

# 연결된 두링크를 입력받아
# 각각의 부모노드를 찾은다음에
# 부모노드의 크기가 작은 부모노드로 통일


def union_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a < b:
        parant[b] = a
    else:
        parant[a] = a


n, m = map(int, input().split())
board = []
# i가 to 노드
for i in range(n):
    board.append(list(map(int, input().split())))

graph = [[] for i in range(n+1)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            graph[i+1].append(j+1)

parant = [i for i in range(n+1)]

# union연산을 수행하여 연결된 노드끼리 루트노드를 설정
for i in range(1, n+1):
    for j in graph[i]:
        union_parant(parant, i, j)
result = True
plan = list(map(int, input().split()))
for i in range(len(plan)):
    if parant[plan[i]] != parant[plan[i+1]]:
        result = False
