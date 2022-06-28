import copy
import sys
sys.setrecursionlimit(10**8)


def setBoard(height, temp_board):
    for i in range(n):
        for j in range(n):
            if height >= temp_board[i][j]:
                temp_board[i][j] = 0
    return temp_board


def dfs(temp_board, x, y):
    temp_board[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and temp_board[nx][ny] != 0:
            dfs(temp_board, nx, ny)


if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        temp = list(map(int, input().split()))
        board.append(temp)
    max_count = 0
    min_height = min(map(min, board))
    max_height = max(map(max, board))

    for height in range(min_height-1, max_height):
        count = 0
        temp_board = copy.deepcopy(board)
        temp_board = setBoard(height, temp_board)
        for i in range(n):
            for j in range(n):
                if temp_board[i][j] != 0:
                    dfs(temp_board, i, j)
                    count += 1
        max_count = max(max_count, count)

    print(max_count)
