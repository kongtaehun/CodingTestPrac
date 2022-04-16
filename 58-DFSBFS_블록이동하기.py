# 모범답안
# BFS로 푼다.
from collections import deque

# 1. 이동가능한 위치 경우의 수를 반환하는 함수

# 2. BFS구현
# 세번째인자는 cost
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
n = len(board)


def getAllMoveCase(pos, new_board):
    # 이동가능한 경우를 담는 리스트
    next_pos = []
    pos = list(pos)
    print(pos)
    x1 = pos[0][0]
    y1 = pos[0][1]
    x2 = pos[1][0]
    y2 = pos[1][1]

    # 상하좌우이동
    # 상
    if new_board[x1-1][y1] == 0 and new_board[x2-1][y1] == 0:
        next_pos.append({(x1-1, y1), (x2-1, y2)})
    # 하
    if new_board[x1+1][y1] == 0 and new_board[x2+1][y1] == 0:
        next_pos.append({(x1+1, y1), (x2+1, y2)})
    # 좌
    if new_board[x1][y1-1] == 0 and new_board[x2][y2-1] == 0:
        next_pos.append({(x1, y1-1), (x2, y2-1)})
    # 우
    if new_board[x1][y1+1] == 0 and new_board[x2][y2+1] == 0:
        next_pos.append({(x1, y1+1), (x2, y2+1)})
    # 가로로 있을 경우 회전,
    if x1 == x2:
        # 아래 두칸이 모두 비어있을 경우
        if new_board[x1+1][y1] == 0 and new_board[x2+1][y2] == 0:
            # 1번고정 아래로
            next_pos.append({(x1, y1), (x2+1, y2-1)})
            next_pos.append({(x1+1, y1+1), (x2, y2)})
        # 위의 두칸이 모두 비어있을 경우
        if new_board[x1-1][y1] == 0 and new_board[x2-1][y2] == 0:
            # 1번고정 아래로
            next_pos.append({(x1, y1), (x2-1, y2-1)})
            next_pos.append({(x1-1, y1+1), (x2, y2)})
    # 세로로 있는경우
    else:
        # 왼쪽 두칸이 모두 비어있을 경우
        if new_board[x1][y1-1] == 0 and new_board[x2][y2-1] == 0:
            # 1번고정 아래로
            next_pos.append({(x1, y1), (x2-1, y2-1)})
            next_pos.append({(x1+1, y1-1), (x2, y2)})
        # 오른쪽 두칸이 비어있는 경우
        if new_board[x1][y1+1] == 0 and new_board[x2][y2+1] == 0:
            # 1번고정 아래로
            next_pos.append({(x1, y1), (x2-1, y2+1)})
            next_pos.append({(x1+1, y1+1), (x2, y2)})
    return next_pos


# 주위에 1씩두르기
new_board = [[1]*(n+2) for i in range(n+2)]
for i in range(n):
    for j in range(n):
        new_board[i+1][j+1] = board[i][j]
for i in range(n+2):
    for j in range(n+2):
        print(new_board[i][j], end=' ')
    print()
pos = {(1, 1), (1, 2)}
q = deque()
q.append((pos, 0))
visited = []
visited.append(pos)
result_cost = 0
while q:
    pos, cost = q.popleft()

    if (n, n) in pos:
        result_cost = cost
        break

    for next_pos in getAllMoveCase(pos, new_board):
        if next_pos not in visited:
            visited.append(next_pos)
            q.append((next_pos, cost+1))
