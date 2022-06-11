n = int(input())
board = []
for i in range(n):
    board.append(list(input()))

visited = [[0]*(n) for i in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global count
    if x >= 0 and y >= 0 and x < n and y < n:
        if visited[x][y] == 0 and board[x][y] == '1':
            visited[x][y] = 1
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)


total_count = 0
ingu = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == '1':
            count = 0
            dfs(i, j)

            total_count += 1
            ingu.append(count)


print(total_count)
new_ingu = sorted(ingu)
for i in range(len(new_ingu)):
    print(new_ingu[i])
