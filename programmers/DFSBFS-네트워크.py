def dfs(graph, start, visited, check):
    visited[start] = check
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited, check)


def solution(n, computers):
    check = 1
    visited = [0 for i in range(n)]
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    print(graph)
    for i in range(n):
        if visited[i] == 0:
            dfs(graph, i, visited, check)
            check += 1

    return max(visited)
