

def spaceCheck(x, y, k):

    for a in range(x, x+k+1):
        for b in range(y, y+k+1):
            if board[a][b] != 1:
                return False
    return True


def bt(x, y, depth):
    global answer, box_cnt
    if x >= 10:
        answer = min(depth, answer)
        return
    if y >= 10:
        bt(x+1, 0, depth)
        return

    if board[x][y] == 1:
        for k in range(5):

            if box_cnt[k] == 0:
                continue
            if y+k >= 10 or x+k >= 10:
                continue
            if not spaceCheck(x, y, k):
                # print(k)
                break
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    board[i][j] = 0
            box_cnt[k] -= 1

            bt(x, y+k+1, depth+1)

            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    board[i][j] = 1
            box_cnt[k] += 1
    else:

        bt(x, y+1, depth)


if __name__ == '__main__':
    box_cnt = [5, 5, 5, 5, 5]
    answer = int(1e9)
    board = [list(map(int, input().split())) for i in range(10)]
    bt(0, 0, 0)
    if answer == int(1e9):
        print(-1)
    else:
        print(answer)
