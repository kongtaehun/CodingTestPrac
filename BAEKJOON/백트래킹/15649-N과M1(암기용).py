def dfs(x):
    if x == m:
        print(result)
    else:
        for i in range(1, n+1):
            if visited[i] == 0:
                visited[i] = 1
                result[x] = i
                dfs(x+1)
                visited[i] = 0
                result[x] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0]*(m)
    visited = [0]*(n+1)
    dfs(0)
