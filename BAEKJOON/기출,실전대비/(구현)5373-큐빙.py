
def printBoard(board):
    for i in range(6):
        for x in range(3):
            for y in range(3):
                print(board[i][x][y], end=' ')
            print()
        print()


def rotate(direc, plane):
    # 시계구현
    if direc == '+':
        new_plane = list(map(list, zip(*plane[::-1])))
    # 반시계
    else:
        new_plane = list(map(list, zip(*plane)))[::-1]
    return new_plane


def sideRotate(direc, plane, sides):

    if direc == '+':
        [1, 0, 2, 3]
        temp = ['a', 'a', 'a']
        # 1면 - 값복사
        for i in range(3):
            temp[i] = cubic[sides[0]][i][-1]
        temp.reverse()
        # 5면 - 값붙혀넣기
        for i in range(3):

            cubic[sides[1]][-1][i], temp[i] = temp[i], cubic[sides[1]][-1][i]

        # 2면- 값붙혀넣기
        for i in range(3):

            cubic[sides[2]][i][0], temp[i] = temp[i], cubic[sides[2]][i][0]
        temp.reverse()
        # 4면 - 붙혀넣기
        for i in range(3):
            cubic[sides[3]][0][i], temp[i] = temp[i], cubic[sides[3]][0][i]
        # 1면-붙혀넣기
        for i in range(3):
            cubic[sides[0]][i][-1], temp[i] = temp[i], cubic[sides[0]][i][-1]
    else:
        temp = ['a', 'a', 'a']
        # 1면 - 값복사
        for i in range(3):
            temp[i] = cubic[sides[0]][i][-1]
        # 4면 - 값붙혀넣기
        for i in range(3):
            cubic[sides[3]][0][i], temp[i] = temp[i], cubic[sides[3]][0][i]
        temp.reverse()
        # 2면- 값붙혀넣기
        for i in range(3):
            cubic[sides[2]][i][0], temp[i] = temp[i], cubic[sides[2]][i][0]

        # 5면 - 붙혀넣기
        for i in range(3):
            cubic[sides[1]][-1][i], temp[i] = temp[i], cubic[sides[1]][-1][i]
        temp.reverse()
        # 1면-붙혀넣기
        for i in range(3):
            cubic[sides[0]][i][-1], temp[i] = temp[i], cubic[sides[0]][i][-1]


if __name__ == '__main__':
    answer = []
    for _ in range(int(input())):
        cubic = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
                 [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
                 [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
                 [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
                 [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
                 [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]]
        n = int(input())
        temp = list(map(str, input().split()))
        for i in range(n):
            temp[i] = list(temp[i])
            plane = temp[i][0]
            direc = temp[i][1]
            if plane == 'U':
                plane = 0
                sides = [1, 5, 2, 4]
                sideRotate(direc, plane, sides)
                cubic[plane] = rotate(direc, cubic[plane])
            elif plane == 'D':
                plane = 3
                sides = [2, 5, 1, 4]
                cubic[5] = list(map(list, zip(*cubic[5])))[::-1]
                cubic[5] = list(map(list, zip(*cubic[5])))[::-1]
                cubic[4] = list(map(list, zip(*cubic[4])))[::-1]
                cubic[4] = list(map(list, zip(*cubic[4])))[::-1]
                cubic[plane] = rotate(direc, cubic[plane])
                sideRotate(direc, plane, sides)
                cubic[5] = list(map(list, zip(*cubic[5][::-1])))
                cubic[5] = list(map(list, zip(*cubic[5][::-1])))
                cubic[4] = list(map(list, zip(*cubic[4][::-1])))
                cubic[4] = list(map(list, zip(*cubic[4][::-1])))

            elif plane == 'F':
                plane = 4
                # 1 -> 반시계
                cubic[1] = list(map(list, zip(*cubic[1])))[::-1]
                # 2-> 시계
                cubic[2] = list(map(list, zip(*cubic[2][::-1])))
                cubic[3] = list(map(list, zip(*cubic[3])))[::-1]
                cubic[3] = list(map(list, zip(*cubic[3])))[::-1]
                sides = [1, 0, 2, 3]
                sideRotate(direc, plane, sides)
                cubic[plane] = rotate(direc, cubic[plane])
                # 1 -> 반시계
                cubic[1] = list(map(list, zip(*cubic[1][::-1])))
                cubic[3] = list(map(list, zip(*cubic[3][::-1])))
                cubic[3] = list(map(list, zip(*cubic[3][::-1])))
                # 2-> 시계
                cubic[2] = list(map(list, zip(*cubic[2])))[::-1]
            elif plane == 'B':
                plane = 5
                # 1 -> 시계
                cubic[1] = list(map(list, zip(*cubic[1][::-1])))
                # 2-> 반시계
                cubic[2] = list(map(list, zip(*cubic[2])))[::-1]
                cubic[3] = list(map(list, zip(*cubic[3])))[::-1]
                cubic[3] = list(map(list, zip(*cubic[3])))[::-1]
                sides = [1, 3, 2, 0]
                sideRotate(direc, plane, sides)
                cubic[plane] = rotate(direc, cubic[plane])
                # 1 -> 반시계
                cubic[1] = list(map(list, zip(*cubic[1])))[::-1]
                # 2-> 시계
                cubic[2] = list(map(list, zip(*cubic[2][::-1])))
                cubic[3] = list(map(list, zip(*cubic[3][::-1])))
                cubic[3] = list(map(list, zip(*cubic[3][::-1])))
            elif plane == 'L':
                plane = 1
                cubic[5] = list(map(list, zip(*cubic[5])))[::-1]
                cubic[4] = list(map(list, zip(*cubic[4][::-1])))
                sides = [3, 5, 0, 4]
                sideRotate(direc, plane, sides)
                cubic[plane] = rotate(direc, cubic[plane])
                cubic[5] = list(map(list, zip(*cubic[5][::-1])))
                cubic[4] = list(map(list, zip(*cubic[4])))[::-1]
            elif plane == 'R':
                plane = 2
                cubic[5] = list(map(list, zip(*cubic[5][::-1])))
                cubic[4] = list(map(list, zip(*cubic[4])))[::-1]
                sides = [0, 5, 3, 4]
                cubic[plane] = rotate(direc, cubic[plane])

                sideRotate(direc, plane, sides)

                cubic[5] = list(map(list, zip(*cubic[5])))[::-1]
                cubic[4] = list(map(list, zip(*cubic[4][::-1])))

        for i in range(3):
            answer.append(''.join(cubic[0][i]))
        # printBoard(cubic)
    for i in answer:
        print(i)
