# 입력
n = 4
l = 10
r = 50
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


# 사방탐색을 위한 이동방향 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visited):
    global unionCnt, unionIdxm, unionSum, already_have_union
    visited[x][y] = 1
    unionIdx.append([x, y])
    already_have_union[x][y] = 1
    unionCnt += 1
    unionSum += board[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] == 0 and abs(board[x][y]-board[nx][ny]) >= l and abs(board[x][y]-board[nx][ny]) <= r:
            dfs(nx, ny, visited)


total = 0
while True:
    already_have_union = [[0]*n for i in range(n)]  # 이미계산한Union 제외위한

    # 업데이트를 위한 리스트
    all_union_idx = []
    all_union_value = []
    cnt = 0
    # 모든점들에 대해서 Union
    for i in range(n):
        for j in range(n):
            # union계산이 되지않은 국가에 대해서만 계산
            print(already_have_union)
            if already_have_union[i][j] == 0:
                unionSum = 0
                unionCnt = 0
                unionIdx = []
                visited = [[0]*n for i in range(n)]
                dfs(i, j, visited)
                if unionCnt >= 2:
                    cnt += 1
                print(unionIdx)
                # 업데이트위한리스트에 append
                all_union_idx.append(unionIdx)
                all_union_value.append(int(unionSum//unionCnt))

    # 반복문탈출
    if cnt == 0:
        break
    print()
    print(all_union_idx)
    print(all_union_value)
    total += 1
    # board업데이트
    for i in range(len(all_union_idx)):
        for j in all_union_idx[i]:
            board[j[0]][j[1]] = all_union_value[i]
    print(board)
print(total)
