import sys
from collections import deque
input = sys.stdin.readline


def setGraph(nodes):
    graph = [[] for i in range(len(nodes))]
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            dist = abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
            # 맥주 20병에 1000미터를 갈수 있으므로
            if dist <= 1000:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def bfs(visited, graph, start, end):

    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        now = q.popleft()
        if now == end:
            return True
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return False


if __name__ == '__main__':
    result = []
    t = int(input())
    for i in range(t):
        # ===============input
        ccount = int(input())
        home = list(map(int, input().split()))
        conv = []
        for i in range(ccount):
            conv.append(list(map(int, input().split())))
        festival = list(map(int, input().split()))

        # ===============preproc
        # home -> 0
        # cconv -> 1~ccount
        # festival -> ccount+1
        nodes = [home]+conv+[festival]
        graph = setGraph(nodes)
        visited = [0]*(ccount+2)

        # ===============mainproc
        # 출발점은 0
        # 도착점은 ccount+1
        result.append('happy' if bfs(visited, graph, 0, ccount+1) else 'sad')

    for i in result:
        print(i)
