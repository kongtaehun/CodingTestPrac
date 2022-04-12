# 시간초과실패
import copy
from itertools import combinations
import time
start = time.time()
# 아이디어 : 3개의 벽을 설치하는 모든 경우의 수계산
# 입력
n, m = map(int, input().split())
graph = []
zero_index = []
two_index = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 2인 지점 찾기 (시작)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            two_index.append([i, j])


# 0인 지역의 인덱스를 가져와서
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_index.append([i, j])


# 3개를 설치하는 모든 조합을 구한다.(순서가 다를경우 같은 조합으로 생각)
comb_wall = list(combinations(zero_index, 3))

# DFS 함수(면적채우기)
#x = 시작노드


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if temp_graph[x][y] == 0:
        temp_graph[x][y] = 2
        dfs(temp_grph, x-1, y)
        dfs(temp_graph, x+1, y)
        dfs(temp_graph, x, y-1)
        dfs(temp_graph, x, y+1)
        return True
    return False

# 리스트의 0개수를 세는 함수


def zerocount(list):
    result = 0
    for i in list:
        result += i.count(0)
    return result


# 각 조합에서 설치한다. # BFS,DFS로 계산하여 2를 채운다.
count = []
for a, b, c in comb_wall:
    temp_graph = copy.deepcopy(graph)
    temp_graph[a[0]][a[1]] = 1
    temp_graph[b[0]][b[1]] = 1
    temp_graph[c[0]][c[1]] = 1
    for x, y in two_index:
        temp_graph[x][y] = 0
        dfs(temp_graph, x, y)
    count.append(zerocount(temp_graph))


# 리스트의 0의 개수를 센다.
print(max(count))


print("time :", time.time() - start)
