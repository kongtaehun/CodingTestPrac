n = 4
l = 10
r = 50
board = [[10, 100, 20, 90], [80, 100, 60, 70],
         [70, 20, 30, 40], [50, 20, 100, 10]]

# DFS로 풀어볼까?


start_x = 0
start_y = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(start_x, start_y, visited):
    global count, sum, union_visited
    count += 1
    sum = sum + board[start_x][start_y]
    visited[start_x][start_y] = 1
    union_visited[start_x][start_y] = 1
    union["포함국가"].append([start_x, start_y])
    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            return False
        if visited[nx][ny] == -1 and abs(board[start_x][start_y]-board[nx][ny]) >= l and abs(board[start_x][start_y]-board[nx][ny]) <= r:
            dfs(nx, ny, visited)
    return True


dd = 0
total_count = 0
while dd < 3:
    final_list = []
    union_visited = [[-1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            visited = [[-1]*n for i in range(n)]
            sum = 0
            count = 0
            union = {}
            union["포함국가"] = []
            dfs(i, j, visited)
            union["인구수"] = int(sum/count)
            final_list.append(union)
    for i in final_list:
        for x in i['포함국가']:
            board[x[0]][x[1]] = i['인구수']
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    # if n*n == len(final_list):
    #     break
    dd += 1
    total_count += 1
print(total_count)
#또실패