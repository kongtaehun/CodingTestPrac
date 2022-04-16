from collections import deque
n = 4
l = 10
r = 50
board = [[10, 100, 20, 90], [80, 100, 60, 70],
         [70, 20, 30, 40], [50, 20, 100, 10]]

# 힌트 ! 모든나라에 대하여 수행한다.
# 한 나라를 기준으로 연결된 조건에 맞는 주변인접국가들 선택
# 조건에 맞는 인접국가가 없을 떄 -1리턴
# x,y,국가와 동명가능한 국가가 있는지 없는지


def bfs(union, x, y, new_board_temp):
    # 상하좌우
    visited = [[0]*n for i in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([[x, y]])
    visited[x][y] = 1
    check = 0
    count = 1
    sum = new_board_temp[x][y]

    union[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 조건에 맞는 국가가 인접해있을 경우 q로 추가하여 찾음
            if visited[nx][ny] == 0 and abs(new_board_temp[x][y] - new_board_temp[nx][ny]) >= l and abs(new_board_temp[x][y] - new_board_temp[nx][ny]) <= r:
                q.append([nx, ny])
                count += 1
                sum += new_board_temp[nx][ny]
                union[nx][ny] = 1
                visited[nx][ny] = 1
                check = 1
    avg = int(sum/count)
    for i in range(n):
        for j in range(n):
            if union[i][j] == 1:
                union[i][j] = avg
    return check, union


union_check = 0
count = 0
while True:
    union = [[-1]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                check, union = bfs(union, i, j, board)
                union_check += check
    board = deepcopy(union)
    if union_check == 0:
        break
    else:
        count += 1
print(count)
