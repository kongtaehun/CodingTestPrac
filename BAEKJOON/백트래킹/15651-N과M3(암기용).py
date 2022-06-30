def dfs(x):
    if x == m:
        print(result)
    else:
        for i in range(1, n+1):
            result[x] = i
            dfs(x+1)
            result[x] = 0


n, m = map(int, input().split())
result = [0]*(m)
dfs(0)
