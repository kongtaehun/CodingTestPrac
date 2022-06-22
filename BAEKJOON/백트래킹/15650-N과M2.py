n, m = map(int, input().split())
nums = [0]*(m)
visited = [0]*(n+1)


def dfs(depth, start):
    if depth == m:
        for i in range(m):

            print(nums[i], end=' ')
        print()
    else:
        for i in range(start, n+1):
            if visited[i] == 0:
                visited[i] = 1
                nums[depth] = i
                dfs(depth+1, i)
                visited[i] = 0
                nums[depth] = 0


dfs(0, 1)
