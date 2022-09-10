

def dfs(visited, start, graph, depth):
    global flag
    if flag == 1:
        return
    if depth == 5:
        flag = 1
        return

    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(visited, i, graph, depth+1)
            visited[i] = 0


if __name__ == '__main__':
    # 깊이가 4인경우
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*(n)
    for i in range(n):
        flag = 0
        visited[i] = 1
        dfs(visited, i, graph, 1)
        visited[i] = 0
        if flag == 1:
            break

    print(flag)
