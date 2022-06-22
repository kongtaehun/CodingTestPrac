from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, flag, start):
    q = deque()
    q.append((start, 0))
    flag[start] = 0
    while q:
        now, flag_int = q.popleft()
        next_flag_int = 1 if flag_int == 0 else 0
        for i in graph[now]:
            if flag[i] == -1:
                flag[i] = next_flag_int
                q.append((i, next_flag_int))
            elif flag[i] == 0:
                if next_flag_int == 1:

                    return False
            elif flag[i] == 1:
                if next_flag_int == 0:

                    return False
    return True


t = int(input())
result = []
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    flag = [-1 for i in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        # 무방향성 고려안해줬음
        graph[a].append(b)
        graph[b].append(a)

    # 비연결 그래프도 생각 : 연결그래프일 경우만 생각했음!
    result = "YES"
    for i in range(1, v+1):
        if flag[i] == -1:
            if not bfs(graph, flag, i):
                result = "NO"
                break
    print(result)
