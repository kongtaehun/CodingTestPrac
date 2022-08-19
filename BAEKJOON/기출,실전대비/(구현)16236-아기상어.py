from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 10초부근에러


def bfs(board, visited, X, Y, cnt):
    global size
    possible_list = []
    q = deque()
    q.append((X, Y, cnt))
    visited[X][Y] = 1
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] <= size:
                    if board[nx][ny] == 0 or board[nx][ny] == size:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt+1))
                    elif board[nx][ny] < size:
                        possible_list.append((nx, ny, cnt+1))
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt+1))

    if len(possible_list) >= 1:
        possible_list.sort(key=lambda x: (x[2], x[0], x[1]))
        board[possible_list[0][0]][possible_list[0][1]] = 0
        return possible_list[0][2], possible_list[0][0], possible_list[0][1]
    else:
        return 0, -1, 0


def printBoard(board, x, y, size, cnt):
    print("========================")
    print(size, cnt)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == x and j == y:
                print("*", end=' ')
            else:
                print(board[i][j], end=' ')
        print()
    print("-----------------------")


if __name__ == '__main__':
    # 아기상어의 처음크기는 2
    size = 2
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                X = i
                Y = j
                break

    cnt = 0
    eat_cnt = 0
    answer = 0
    while True:
        visited = [[0]*(n) for i in range(n)]
        cnt, X, Y = bfs(board, visited, X, Y, cnt)
        # printBoard(board, X, Y, size, cnt)
        eat_cnt += 1
        if X == -1:
            print(answer)
            break
        else:
            if eat_cnt == size:
                size += 1
                eat_cnt = 0
        answer = cnt
    # print(cnt)
