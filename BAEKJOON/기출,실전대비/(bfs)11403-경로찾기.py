# 자기자신에서 자기자신으로 가는 예외
# bfs로 노드마다 방문하면서 확인
import copy
from collections import deque


def bfs(graph, visited, start):
    q = deque()
    q.append(start)
    # 원래 bfs는 출발지점을 방문으로 바로 초기화해주지만
    # 해당문제에서는 그래프를통해 출발지점 방문해야지만 출발지점방문으로 간주한다.
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


if __name__ == '__main__':
    n = int(input())
    graph = [[] for i in range(n)]
    for from_node in range(n):
        temp = list(map(int, input().split()))
        for to_node in range(n):
            if temp[to_node] == 1:
                graph[from_node].append(to_node)

    result = []
    for from_node in range(n):
        visited = [0]*(n)
        bfs(graph, visited, from_node)
        result.append(copy.deepcopy(visited))

    for i in result:
        for j in i:
            print(j, end=' ')
        print()
