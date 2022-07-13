##

def dfs(start, graph, visited):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, graph, visited)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(n):
        temp = list(map(int, input().split()))
        for idx, v in enumerate(temp):
            if v == 1:
                graph[i+1].append(idx+1)
    plan = list(map(int, input().split()))

    flag = True
    for i in range(len(plan)-1):
        visited = [0]*(n+1)
        dfs(plan[i], graph, visited)
        if visited[plan[i+1]] == 0:
            flag = False
            break

    print('YES' if flag else 'NO')
