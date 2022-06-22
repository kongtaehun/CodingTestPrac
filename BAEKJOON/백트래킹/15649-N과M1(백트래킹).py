n, m = map(int, input().split())
visited = [0]*(n+1)
arr = [0]*(m+1)
# x는 현재 숫자의 크기


def dfs_bt(x):
    # 종료조건
    if x == m+1:
        for i in range(1, m+1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if visited[i] == 0:
                visited[i] = 1
                arr[x] = i
                dfs_bt(x+1)
                arr[x] = 0
                visited[i] = 0


dfs_bt(1)
