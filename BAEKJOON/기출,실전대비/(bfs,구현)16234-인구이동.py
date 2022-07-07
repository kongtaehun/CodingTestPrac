from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(visited, board, x, y, union_num):
    q = deque()
    q.append((x, y))
    visited[x][y] = union_num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    if l <= abs(board[nx][ny]-board[x][y]) <= r:
                        visited[nx][ny] = union_num
                        q.append((nx, ny))


def distribute(board, visited):
    max_union = max(map(max, visited))
    union_peopls = [0]*(max_union+1)
    union_count = [0]*(max_union+1)
    for i in range(n):
        for j in range(n):
            union_peopls[visited[i][j]] += board[i][j]
            union_count[visited[i][j]] += 1
    for i in range(n):
        for j in range(n):
            board[i][j] = union_peopls[visited[i]
                                       [j]]//union_count[visited[i][j]]
    return board


if __name__ == '__main__':
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    visited = [[-1]*(n) for i in range(n)]
    answer = 0
    while True:

        # 오늘하루 연합국가 배열 visited 초기화
        visited = [[-1]*(n) for i in range(n)]
        union_count = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == -1:
                    bfs(visited, board, i, j, union_count)
                    union_count += 1
        if union_count == n*n:
            break
        answer += 1
        # 연합국가 인구배분
        board = distribute(board, visited)

    print(answer)
