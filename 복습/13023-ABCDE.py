# 그래프의 깊이가 4사람
flag = False


def bt(depth, graph, now, visited):
    global flag
    if flag == True:
        return
    if depth == 5:
        flag = True
        return
    else:
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                bt(depth+1, graph, i, visited)
                visited[i] = 0


def solution():
    global flag
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(n)
    answer = False
    for i in range(n):
        flag = False
        bt(0, graph, i, visited)
        if flag:
            answer = True
            break
    if answer:
        print(1)
    else:
        print(0)


solution()
