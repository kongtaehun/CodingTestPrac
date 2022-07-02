def bt(depth, start):
    if depth == m:
        print(result)
    else:
        for i in range(start, n+1):
            if visited[i] == 0:
                visited[i] = 1
                result[depth] = i
                bt(depth+1, i)
                visited[i] = 0
                result[depth] = i


n, m = map(int, input().split())
result = [0]*m
visited = [0]*(n+1)
bt(0, 0)
