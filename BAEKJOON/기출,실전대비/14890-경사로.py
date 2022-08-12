from re import L


def checkLine(line, l):
    now = line[0]

    i = 1
    while i < n:
        # -1이면 내리막
        diff = line[i]-now
        if line[i] == now:
            i += 1

        elif diff == -1:
            for leng in range(l):
                if i+leng >= n:

                    print(str(line)+"은", end=' ')
                    print("차이가 1이나지만 l의 범위가 넘어서 false")
                    return False
                if line[i] != line[i+leng]:
                    print(str(line)+"은", end=' ')
                    print("차이가 1이나지만 l을 만족하는 길이가 부족해서 false")
                    return False

            for a in range(l):
                if i+l+a < n and now == line[i+l+a]:
                    print(str(line)+"은", end=' ')
                    print("차이가 1이나지만 l의 범위도 만족하지만 다음 블럭이 오르막이라 false")
                    return False

            if i+l < n:
                i += l-1
                now = line[i]
            else:
                return True
        elif diff == 1:
            return True

        else:
            print(str(line)+"은", end=' ')
            print("차이가 2이상")
            return False
    return True


if __name__ == '__main__':
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    column_board = [[] for i in range(n)]
    cnt = 0
    for i in range(n):
        line_r = list(reversed(board[i]))
        if checkLine(board[i], l):
            if checkLine(line_r, l):
                print(board[i])
                cnt += 1

        temp = []
        for j in range(n):
            temp.append(board[j][i])

        line_r = list(reversed(temp))
        if checkLine(temp, l):
            if checkLine(line_r, l):
                print("이건 세로 : "+str(temp))
                cnt += 1

    print(cnt)
