from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 양의 위치 사방으로 울타리를 설치한다.


def bfs(visited, board, q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'S':
                    return 0
                if visited[nx][ny] == 0 and board[nx][ny] == '.':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(str, input())) for i in range(n)]
    q = deque()
    visited = [[0]*(m)for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                for d in range(4):
                    if 0 <= i+dx[d] < n and 0 <= j+dy[d] < m:
                        if board[i+dx[d]][j+dy[d]] == '.':
                            board[i+dx[d]][j+dy[d]] = 'D'
            if board[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 1
    print(bfs(visited, board, q))
    for i in board:
        print(''.join(i))
