def printB(blue, green, x, y, t):
    print(x, y, t)
    red = [[0]*4 for i in range(4)]
    if t == 1:
        red[x][y] = 1
    elif t == 2:
        red[x][y] = 1
        red[x][y+1] = 1
    else:
        red[x][y] = 1
        red[x+1][y] = 1
    for i in range(4):
        print(red[i], end='   ')
        print(blue[i])
    print()
    for i in green:
        print(i)
    print()


def moveTile(blue, green):
    blue_flag = [0, 0]
    green_flag = [0, 0]
    for i in range(2):
        for j in range(4):
            if blue[j][i] == 1:
                blue_flag[i] = 1
            if green[i][j] == 1:
                green_flag[i] = 1

    for _ in range(blue_flag[0]+blue_flag[1]):
        for j in range(4):
            blue[j].pop()
            blue[j] = [0]+blue[j]
    # 반시계방향 회전
    if green_flag[0]+green_flag[1] > 0:
        green = list(map(list, zip(*green)))[::-1]
        for _ in range(green_flag[0]+green_flag[1]):
            for j in range(4):
                green[j].pop()
                green[j] = [0] + green[j]
        green = list(map(list, zip(*green[::-1])))

    return blue, green


def calGrade(blue, green):
    global answer
    for i in range(2, 6):
        blue_cnt = 0
        green_cnt = 0
        for j in range(4):
            if blue[j][i] == 1:
                blue_cnt += 1
            if green[i][j] == 1:
                green_cnt += 1

        if blue_cnt == 4:
            for j in range(4):
                blue[j] = [0] + blue[j][:i] + blue[j][i+1:]
            answer += 1

        if green_cnt == 4:
            green = list(map(list, zip(*green)))[::-1]
            for j in range(4):
                green[j] = [0] + green[j][:i] + green[j][i+1:]
            answer += 1
            green = list(map(list, zip(*green[::-1])))

    return blue, green


def stackBlue(x, t, blue):
    flag = 0
    if t == 1:
        for i in range(6):

            if blue[x][i] == 1:
                blue[x][i-1] = 1
                flag = 1
                break
        if flag == 0:
            blue[x][5] = 1

    elif t == 2:
        for i in range(6):
            if blue[x][i] == 1:
                blue[x][i-1] = 1
                blue[x][i-2] = 1
                flag = 1
                break
        if flag == 0:
            blue[x][5] = 1
            blue[x][4] = 1
    else:
        for i in range(6):
            if blue[x][i] == 1 or blue[x+1][i] == 1:
                blue[x][i-1] = 1
                blue[x+1][i-1] = 1
                flag = 1
                break
        if flag == 0:
            blue[x][5] = 1
            blue[x+1][5] = 1


def stackGreen(y, t, green):
    flag = 0
    if t == 1:
        for i in range(6):

            if green[i][y] == 1:
                green[i-1][y] = 1
                flag = 1
                break
        if flag == 0:
            green[5][y] = 1

    elif t == 3:
        for i in range(6):
            if green[i][y] == 1:
                green[i-1][y] = 1
                green[i-2][y] = 1
                flag = 1
                break
        if flag == 0:
            green[5][y] = 1
            green[4][y] = 1
    elif t == 2:
        for i in range(6):

            if green[i][y] == 1 or green[i][y+1] == 1:
                green[i-1][y] = 1
                green[i-1][y+1] = 1
                flag = 1
                break
        if flag == 0:
            green[5][y] = 1
            green[5][y+1] = 1


if __name__ == '__main__':
    green = [[0]*4 for i in range(6)]
    blue = [[0]*6 for i in range(4)]
    answer = 0

    for i in range(int(input())):
        t, x, y = map(int, input().split())
        stackBlue(x, t, blue)
        stackGreen(y, t, green)
        blue, green = calGrade(blue, green)
        blue, green = moveTile(blue, green)
        # printB(blue, green, x, y, t)
    cnt = 0
    for i in range(6):
        for j in range(4):
            cnt += blue[j][i]
            cnt += green[i][j]
    print(answer)
    print(cnt)
