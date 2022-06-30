def bt(depth):
    if depth == n:
        for i in result:
            print(i, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if visited[i] == 0 and i not in result:
                visited[i] == 1
                result[depth] = i
                bt(depth+1)
                result[depth] = 0
                visited[i] = 0


n = int(input())
result = [0]*n
visited = [0]*(n+1)
bt(0)
