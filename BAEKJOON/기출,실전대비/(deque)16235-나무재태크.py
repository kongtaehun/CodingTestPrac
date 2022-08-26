import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]


def start(trees, board, k):

    for i in range(k):
        dead = [[[] for i in range(n)] for i in range(n)]
        for x in range(n):
            for y in range(n):
                for z in range(len(trees[x][y])):
                    if board[x][y] < trees[x][y][z]:
                        for _ in range(z, len(trees[x][y])):
                            board[x][y] += trees[x][y].pop()//2
                        break
                    else:
                        board[x][y] -= trees[x][y][z]
                        trees[x][y][z] += 1

        for x in range(n):
            for y in range(n):
                for z in range(len(trees[x][y])):
                    if trees[x][y][z] % 5 == 0:
                        for i in range(8):
                            nx = x+dx[i]
                            ny = y+dy[i]
                            if 0 <= nx < n and 0 <= ny < n:
                                trees[nx][ny].appendleft(1)
                board[x][y] += a[x][y]
    result = 0
    for x in range(n):
        for y in range(n):
            result += len(trees[x][y])
    return result


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    board = [[5]*(n) for i in range(n)]
    trees = [[deque() for i in range(n)] for i in range(n)]
    for i in range(m):
        x, y, z = map(int, input().split())
        trees[x-1][y-1].append(z)
    # trees.sort(key=lambda x: x[2])
    print(start(trees, board, k))
