#치킨거리는 bfs로 안구해도 되고(인덱스계산으로 가능하다.)

from collections import deque
import copy
from itertools import combinations
import sys
input = sys.stdin.readline
Non = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()

# todo : board의 치킨집을 제거하고 board 반환, 치킨집좌표리스트반환


def getChikenLocation(board, n):
    chicken_location = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                chicken_location.append((i, j))
                board[i][j] = 0
    return chicken_location, board
# todo : board에 치킨집을 입력하고 새로운 board로반환


def setNewChickenLocation(board, chickens, n):
    new_board = copy.deepcopy(board)
    for i in chickens:
        new_board[i[0]][i[1]] = 2
    return new_board


# todo : 집에 위치에서 탐색하여 치킨거리를 구하기
    # 가장 가까운 치킨집 만났을 떄 break

def getTotalChickenDistance(board, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                visited = [[0]*n for i in range(n)]
                count += bfs(board, visited, i, j)
                # print("==============")
                # print(i, j)
                # printArr(visited)
                # print("==============")
    return count


def bfs(board, visited, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == 2:
            return visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


if __name__ == '__main__':
    # =========input=========
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    # =========preproc=========
    chicken_locations, board = getChikenLocation(board, n)

    # =========mainproc=========
    min_chicken_distance = Non
    for chickens in list(combinations(chicken_locations, m)):
        new_board = setNewChickenLocation(board, chickens, n)
        total_chicken_distance = getTotalChickenDistance(new_board, n)
        min_chicken_distance = min(
            min_chicken_distance, total_chicken_distance)
    print(min_chicken_distance)
