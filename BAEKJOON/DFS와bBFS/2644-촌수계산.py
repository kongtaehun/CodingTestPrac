def dfs(visited, graph, start, count):

    visited[start] = count
    for i in graph[start]:
        if visited[i] == -1:
            dfs(visited, graph, i, count+1)


if __name__ == '__main__':

    #============input============
    n = int(input())
    start, target = map(int, input().split())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1 for i in range(n+1)]


    #============cal============
    dfs(visited, graph, start, 0)
    print(visited[target])
