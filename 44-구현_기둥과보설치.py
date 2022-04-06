# 풀이하지 못함 !
# 매번 전체의 구조물을 확인하는게 더 효율적이고 빠르다.
# 실패

# 1. 보
# 양끝이 보
# 한쪽 끝이 기둥
# 2. 기둥
# 바닥에 붙어있거나()
# 보의 한쪽과 연결되어 있거나
# 기둥과 연결되어있어야함

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
               [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

# board만들기
# 첫번째는 기둥 두번째는 보
board_0 = [[0]*(n+1) for i in range(n+1)]
board_1 = [[0]*(n+1) for i in range(n+1)]


# 검사하는 함수


def check(좌표x, 좌표y, 기둥인지보인지, 추가삭제):
    # 추가할 때
    if 추가삭제 == 1:
        # 기둥일 때
        if 기둥인지보인지 == 0:
            # 바닥에 붙어있는경우 가능
            if 좌표y == 0:
                # 기둥을 설치
                board_0[좌표x][좌표y] = 1
                board_0[좌표x][좌표y+1] = 2
                return True
            # 해당위치에 보가 있다.
            elif board_1[좌표x][좌표y] == 1:
                board_0[좌표x][좌표y] = 1
                board_0[좌표x][좌표y+1] = 2
                return True
            # 해당위치에 기둥이 있다.
            elif board_0[좌표x][좌표y] == 1:
                board_0[좌표x][좌표y] = 1
                board_0[좌표x][좌표y+1] = 2
                return True
            # 나머지경우는 불가능
            else:
                return False
        # 보일 경우
        elif 기둥인지보인지 == 1:
            # 양쪽끝이 보인 경우
            if board_1[좌표x][좌표y] == 1 and board_1[좌표x+1][좌표y] == 1:
                board_1[좌표x][좌표y] = 1
                board_1[좌표x+1][좌표y] = 2
                return True
            # 한쪽 끝이 기둥인 경우
            elif board_0[좌표x][좌표y] == 1 or board_0[좌표x+1][좌표y] == 1:
                board_1[좌표x][좌표y] = 1
                board_1[좌표x+1][좌표y] = 2
                return True
            else:
                return False
            # 추가할 때
    elif 추가삭제 == 0:
        # 기둥일 때
        if 기둥인지보인지 == 0:
            # 위아래 기둥
            [좌표y-1][좌표x]

        # 보일 경우
        elif 기둥인지보인지 == 1:
            # 양쪽끝이 보인 경우
            if board_1[좌표x][좌표y] == 1 and board_1[좌표x+1][좌표y] == 1:
                board_1[좌표x][좌표y] = 1
                board_1[좌표x+1][좌표y] = 2
                return True
            # 한쪽 끝이 기둥인 경우
            elif board_0[좌표x][좌표y] == 1 or board_0[좌표x+1][좌표y] == 1:
                board_1[좌표x][좌표y] = 1
                board_1[좌표x+1][좌표y] = 2
                return True
            else:
                return False


# 하나씩 체크하기
for i in build_frame:
    check(i[0], i[1], i[2], i[3])

for i in range(n+1):
    for j in range(n+1):
        print(board_1[i][j], end=' ')
    print()
