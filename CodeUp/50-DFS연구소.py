# 정답
n, m = map(int, input().split())
data = []  # 초기맵
temp = [[0]*m for i in range(n)]  # 벽을 설치한ㄷ뉘 맵

for i in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스가 퍼지게하는 함수(x,y는 시작위치)
# temp는 벽을 설치한 임시 그래프리스트


def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵의 0의 개수를 세는 메소드


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# dfs를 이용하여 울타리를 설치하면서 매번 안전영역의 크기 계산


def dfs(count):
    # 울타리가 3
    global result
    if count == 3:
        # 울타리가 3개가 설치되었을 때 temp에 graph를 매핑
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 시작위치에서 바이러스 전파시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 울타리 설치하기
    # 전부다 확인하면서 0 인곳에 울타리를 설치한다.
    # 모든 경우를 확인하는것
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                # 재귀적으로 울타리하나씩늘려가면서 확인
                # 재귀함수안에서 다시 이곳에 와서 모든 0을 탐색한다.
                # 3개가 끝나면 함수가 종료되어 하나씩 벽을 제거
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
# 왜더 느리지???
