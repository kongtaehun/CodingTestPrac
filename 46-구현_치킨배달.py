# 입력
#home = [x좌표, y좌표, 최소거리, 치킨집x, 치킨집y]
from itertools import combinations


n, m = list(map(int, input().split()))
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
chick = []
home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append([i, j, n*2])
        elif board[i][j] == 2:
            chick.append([i, j])


# 거리 구하는 함수


def distance(home_x, home_y, chik_x, chik_y):
    return abs(chik_x-home_x) + abs(chik_y-home_y)


# 각집의 최소 치킨거리 구하기
# 각 집의 치킨집과 거리
home_chick = []
for hm in range(len(home)):
    for ch in range(len(chick)):
        if home[hm][2] > distance(home[hm][0], home[hm][1], chick[ch][0], chick[ch][1]):
            home[hm][2] = distance(home[hm][0], home[hm]
                                   [1], chick[ch][0], chick[ch][1])
            temp = [chick[ch][0], chick[ch][1], distance(
                home[hm][0], home[hm][1], chick[ch][0], chick[ch][1])]
    home_chick.append(temp)
print(home_chick)


# 각치킨집이 갖는 집의 개수
# 치킨집이 갖는 집의 개수랑 총 거리
chick_home = [[0, 0] for i in range(len(chick))]

for x, y, cost in home_chick:
    chick_home[chick.index([x, y])][0] += 1
    chick_home[chick.index([x, y])][1] += cost
print(chick_home)

# 정렬 후 m개만 연산
temp = sorted(chick_home, reverse=True)[:m]
result = 0
for i in range(m):
    result = result + temp[i][1]
print(result)

# 조합을 이용
# 입력
#home = [x좌표, y좌표, 최소거리, 치킨집x, 치킨집y]
n, m = list(map(int, input().split()))
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
chick = []
home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append([i, j])
        elif board[i][j] == 2:
            chick.append([i, j])

# 모든 치킨집 중에서 m개의 치킨집을 뽑았을 경우 리스트
candidates = list(combinations(chick, m))

# 후보 조합에서 치킨거리의 값 게산


def get_sum(candidate):
    result = 0
    for hx, hy in home
