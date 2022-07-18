def dfs(visited, graph, start):
    global result
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(visited, graph, i)
        # 사이클이 발생하였을 경우 i는 사이클
        elif visited[i] == 1:
            result.append(i)


if __name__ == '__main__':
    n = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(n):
        a = int(input())
        graph[a].append(i+1)
    temp = []
    result = []

    for i in range(1, n+1):
        visited = [0]*(n+1)
        dfs(visited, graph, i)
        print(result)

    print(len(result))
    result = list(set(result))
    result.sort()
    for i in result:
        print(i)
