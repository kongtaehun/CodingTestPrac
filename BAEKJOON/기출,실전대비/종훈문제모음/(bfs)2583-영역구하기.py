from collections import deque, Counter
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(board, visited, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [[0]*(m) for i in range(n)]
    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for y in range(x1, x2):
            for x in range(y1, y2):
                board[x][y] = 1


    visited = [[0]*(m) for i in range(n)]
    answer= []
    for x in range(n):
        for y in range(m):
            if visited[x][y] == 0 and board[x][y] == 0:
                temp = bfs(board, visited, x, y)
                answer.append(temp)
    answer.sort()
    print(len(answer))
    for i in answer:
        print(i,end = ' ')