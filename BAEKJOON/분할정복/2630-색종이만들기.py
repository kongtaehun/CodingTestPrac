from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
one_result = 0
zero_result = 0

def getDivid(start, n):

    new_start1 = [start[0], start[1]]
    new_start2 = [start[0]+n, start[1]]
    new_start3 = [start[0], start[1]+n]
    new_start4 = [start[0]+n, start[1]+n]
    return new_start1, new_start2, new_start3, new_start4,


def getBoard(start, n, board):
    result = []
    for i in range(start[0], start[0]+n):
        temp = []
        for j in range(start[1], start[1] + n):
            temp.append(board[i][j])
        result.append(temp)

    return result

q = deque()
q.append(([0, 0], n))

while q:

    start, n = q.popleft()
    temp_board = getBoard(start, n, board)
    summ = sum(map(sum, temp_board))

    if summ == n*n or summ == 0:
        # 카운트증가
        if summ > 0:
            one_result += 1
        else:
            zero_result += 1
            # printArr(temp_board)
    else:
        # 4개로나누기
        n = int(n/2)
        s1, s2, s3, s4 = getDivid(start, n)
        q.append((s1, n))
        q.append((s2, n))
        q.append((s3, n))
        q.append((s4, n))
print(zero_result)
print(one_result)
