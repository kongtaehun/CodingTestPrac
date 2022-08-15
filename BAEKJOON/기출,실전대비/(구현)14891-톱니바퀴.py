from collections import deque

GEAR_CNT = 4


def allGearsRotate(gears, gear_num, direc):
    # 왼쪽방향으로 회전실시
    now = gears[gear_num][6]
    left_side = 0
    for i in range(gear_num-1, -1, -1):
        if now != gears[i][2]:
            left_side += 1
            now = gears[i][6]
        else:
            break
    now_direc = direc
    # print("왼쪽" + str(left_side))
    for i in range(gear_num-1, gear_num-left_side-1, -1):
        gearRotate(gears[i], -now_direc)
        now_direc = -now_direc

    # 오른쪽 방향으로 실시
    now = gears[gear_num][2]
    right_side = 0

    for i in range(gear_num+1, GEAR_CNT):
        if now != gears[i][6]:
            right_side += 1
            now = gears[i][2]
        else:
            break
    now_direc = direc
    # print("오른쪽" + str(right_side))
    for i in range(gear_num+1, gear_num+right_side+1):
        # print(str(i)+"번쨰회전")
        gearRotate(gears[i], -now_direc)
        now_direc = -now_direc
    # 나 회전
    gearRotate(gears[gear_num], direc)


def getScore(gears):
    score = 0
    for i in range(GEAR_CNT):
        score += gears[i][0]*(2**i)
    return score


def gearRotate(gear, direc):
    if direc == 1:
        # 시계방향 -> 맨끝에 있는것을 빼소 맨앞으로
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())


# 돌아가는 것을 구현하기 위해서 뎈을 이용
if __name__ == '__main__':
    gears = [deque(list(map(int, list(input())))) for i in range(GEAR_CNT)]
    k = int(input())
    for i in range(k):
        gear_num, direc = map(int, input().split())
        allGearsRotate(gears, gear_num-1, direc)
        # print(gears)
    print(getScore(gears))
