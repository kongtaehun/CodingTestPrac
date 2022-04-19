# 입력
n = 4
l = 10
r = 50
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global union_count, union_sum, unions_idx
    unions_idx.append([x, y])
    union_count += 1
    if type(board[x][y]) is list:
        temp = board[x][y][0]
    elif type(board[x][y]) is int:
        temp = board[x][y]
    union_sum += temp
    already_calcul[x][y] = 0
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if visited[nx][ny] == 0 and abs(temp2-temp) <= r and abs(temp2-temp) >= l:
                dfs(nx, ny)


total_count = 0
result = 1
# 연합의 국가개수가 2개이상인 연합이 하나도없으면 종료
while result != 0:
    # 국가개수가 2개이상인 연합의 개수
    result = 0
    # board를 업데이트하기위한 리스트
    # 연합의 최대치 = n의 제곱
    update_nation = [[] for i in range(n*n)]
    update_ingu = [[] for i in range(n*n)]
    unionID = 0
    already_calcul = [[0]*n for i in range(n)]
    # 모든점에 대하여 맵을 업데이트하기위한 리스트 초기화
    for i in range(n):
        for j in range(n):

            # 한점에 대한 계산
            # 연합의 고유번호
            unionID += 1
            # 이국가가 있는 연합에 있는 나라들 인덱스
            unions_idx = []
            union_sum = 0
            union_count = 0
            visited = [[0]*n for i in range(n)]
            if already_calcul[i][j] == 0:
                dfs(i, j)
                # 연합의 국가 개수가 크기가 1보다 작으면 문을 열지 않은거임
                if len(unions_idx) >= 1:
                    result += 1
                update_nation[unionID-1].append(unions_idx)
                update_ingu[unionID-1].append(int(union_sum//union_count))

    # 모든점의 탐색이 끝났을 떄
    if result > 0:
        # 연합의 국가 개수가 2개이상인 지역이 있었으면 totalcount 올려줌
        total_count += 1
    print(update_ingu)
    # 지도 업데이트
    for i in range(unionID):
        board[update_nation[i][0][0][0]
              ][update_nation[i][0][0][1]] = update_ingu[i]

