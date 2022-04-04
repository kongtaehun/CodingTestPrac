
from collections import deque

n = int(input())
board = [[0]*(n) for i in range(n)]
apple_n = int(input())
apple = []
for i in range(apple_n):
    a, b = list(map(int, input().split()))
    apple.append([a, b])
    board[a-1][b-1] = 1

direc_n = int(input())
direc = []
turn_indics = []
for i in range(direc_n):
    a, b = list(map(str, input().split()))
    direc.append([int(a), b])
    turn_indics.append(int(a))
# 종료조건
# 벽에 부딛혔을때
# 자기의 꼬리와 머리가 만났을 때
# +1


# false체크
def check(q, now_indic, board):
    listt = list(q)
    print(listt)

    # 꼬리들을 보드에 깔기
    for i in range(len(listt)):
        x, y = listt[i]
        board[x][y] = 2

    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    # 꼬리에 얼굴이 만나는지 검사
    if board[now_indic[0]][now_indic[1]] == 2:
        return 0

    return 1


a_now = 0
b_now = 0
# 우하좌상
now_direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
long = 1
# 몸에대한 정보
queue = deque()
queue.append([a_now, b_now])
count = 0
방향변수 = 0
몇번째방향전환 = 0
while True:

    count += 1
    # 몸길이를 늘리기
    a_now = a_now+now_direc[방향변수][0]
    b_now = b_now+now_direc[방향변수][1]
    # 범위 넘어가는지 검사
    if a_now > n-1 or b_now > n-1 or a_now < 0 or b_now < 0:
        break
    if board[a_now][b_now] == 0:
        # 보드에 사과가 없으면 한칸 줄이기
        queue.popleft()  # 선입선출

    # check
    result = check(queue, [a_now, b_now], board)
    queue.append([a_now, b_now])
    if result == 0:
        break

    # 방향전환
    if count in turn_indics:
        if direc[몇번째방향전환][1] == 'D':
            if 방향변수 != 3:
                방향변수 += 1
            else:
                방향변수 = 1
        else:
            if 방향변수 != 1:
                방향변수 -= 1
            else:
                방향변수 = 3
        몇번째방향전환 += 1
print(count)

# 검사

# 보드출력
# for i in range(n):
#     for j in range(n):
#         print(board[i][j], end=' ')
#     print()
