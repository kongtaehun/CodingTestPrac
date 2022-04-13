# 아이디어: 초기 큐에 낮은번호 순서대로 먼저 입력 후 BFS 실행하면
# 한차례씩 순서대로 가능하다.

from collections import deque
'''
#입력
n,k = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
'''

n = 3
k = 3
board = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
s = 1
x = 2
y = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 바이러스의 위치 리스트
# 0은 제외 k+1까지
k_list = [[] for i in range(k+1)]
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            k_list[board[i][j]].append((i, j, 0))
print(k_list)

for i in range(1, k+1):
    print(k_list[i][0])

# 처음시간
stop_s = 0

q = deque([k_list[1][0]])
for i in range(2, k+1):
    q.append(k_list[i][0])

while q:

    x, y, stop = q.popleft()
    print(stop)
    if stop == s:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] == 0:
            temp = stop+1
            board[nx][ny] = board[x][y]
            q.append([nx, ny, temp])

print(board)
