from collections import Counter


def checkThreeDirection(case):
    result = {}
    result['X'] = 0
    result['O'] = 0
    board = [['.']*(3) for i in range(3)]
    idx = 0
    # 3*3으로 변환
    for i in range(3):
        for j in range(3):
            board[i][j] = case[idx]
            idx += 1

    # 좌상단 -> 대각선, 가로, 세로
    if board[0][0] == 'X' or board[0][0] == 'O':
        # 대각선
        cnt = 0
        for i in range(3):
            if board[i][i] == board[0][0]:
                cnt += 1
        if cnt == 3:
            result[board[0][0]] += 1

        # 가로
        cnt = 0
        for i in range(3):
            if board[0][i] == board[0][0]:
                cnt += 1
        if cnt == 3:
            result[board[0][0]] += 1
        # 세로
        cnt = 0
        for i in range(3):
            if board[i][0] == board[0][0]:
                cnt += 1
        if cnt == 3:
            result[board[0][0]] += 1

    # 좌중단 -> 가로
    if board[1][0] == 'X' or board[1][0] == 'O':
        cnt = 0
        for i in range(3):
            if board[1][i] == board[1][0]:
                cnt += 1
        if cnt == 3:
            result[board[1][0]] += 1

    # 좌하단 -> 가로
    if board[2][0] == 'X' or board[2][0] == 'O':
        cnt = 0
        for i in range(3):
            if board[2][i] == board[2][0]:
                cnt += 1
        if cnt == 3:
            result[board[2][0]] += 1
    # 중상단 -> 세로
    if board[0][1] == 'X' or board[0][1] == 'O':
        cnt = 0
        for i in range(3):
            if board[i][1] == board[0][1]:
                cnt += 1
        if cnt == 3:
            result[board[0][1]] += 1
    # 우상단 => 세로, 대각선
    if board[0][2] == 'X' or board[0][2] == 'O':
        cnt = 0
        for i in range(3):
            if board[i][2] == board[0][2]:
                cnt += 1
        if cnt == 3:
            result[board[0][2]] += 1
        # 대각선
        cnt = 0
        for i in range(3):
            if board[i][2-i] == board[0][2]:
                cnt += 1
        if cnt == 3:
            result[board[0][2]] += 1
    return result

# 승자가 두명개가 있으면 안댐


def check(case):

    if 'X' not in case or 'O' not in case:
        return 'invalid'
    if '.' not in case:
        temp = dict(Counter(case))
        vic_team = checkThreeDirection(case)
        if (temp['X'] == temp['O'] or temp['X']-temp['O'] == 1) and (vic_team['O'] == 0 and vic_team['X'] == 0):
            return 'valid'
        if temp['X'] == temp['O'] and (vic_team['O'] >= 1 and vic_team['X'] == 0):
            return 'valid'

        if temp['X']-temp['O'] == 1 and (vic_team['X'] >= 1 and vic_team['O'] == 0):
            return 'valid'

    else:
        temp = dict(Counter(case))
        # o가 이겨야함
        if temp['X'] == temp['O']:
            vic_team = checkThreeDirection(case)
            if vic_team['O'] >= 1 and vic_team['X'] == 0:
                return 'valid'
        # x가 이겨야함
        if temp['X']-temp['O'] == 1:
            vic_team = checkThreeDirection(case)
            if vic_team['X'] >= 1 and vic_team['O'] == 0:
                return 'valid'

    return 'invalid'


if __name__ == '__main__':
    #   꽉찼을 때 : X가하나더 많아야함
    #   덜찼을 때 :
    #               1. 개수가 맞아야함 (둘의 개수가 같거나 X가 하나더 많아야함)
    #               2. 3방향에서 어떤하나가 완성이어야함
    while True:
        case = input()
        if case == 'end':
            break
        print(check(case))
