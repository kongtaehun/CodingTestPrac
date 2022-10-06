

def getsatisfaction(board, students):
    result = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            if 0 <= j-1 < n and board[i][j-1] in students[board[i][j]]:
                cnt += 1
            if 0 <= j+1 < n and board[i][j+1] in students[board[i][j]]:
                cnt += 1
            if 0 <= i-1 < n and board[i-1][j] in students[board[i][j]]:
                cnt += 1
            if 0 <= i+1 < n and board[i+1][j] in students[board[i][j]]:
                cnt += 1
            if cnt != 0:
                result += 10**(cnt-1)
    return result


def setBoard(id, favorite):
    # 비어있는 칸 중에서 좋아하는 학생이 가장 많이 인접한칸들! 구하기
    candidate = []
    now_max = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt = 0
                blank_cnt = 0
                if 0 <= j-1 < n and board[i][j-1] in favorite:
                    cnt += 1
                elif 0 <= j-1 < n and board[i][j-1] == 0:
                    blank_cnt += 1
                if 0 <= j+1 < n and board[i][j+1] in favorite:
                    cnt += 1
                elif 0 <= j+1 < n and board[i][j+1] == 0:
                    blank_cnt += 1
                if 0 <= i-1 < n and board[i-1][j] in favorite:
                    cnt += 1
                elif 0 <= i-1 < n and board[i-1][j] == 0:
                    blank_cnt += 1
                if 0 <= i+1 < n and board[i+1][j] in favorite:
                    cnt += 1
                elif 0 <= i+1 < n and board[i+1][j] == 0:
                    blank_cnt += 1
                if cnt > now_max:
                    candidate = [(blank_cnt, i, j)]
                    now_max = cnt
                elif cnt == now_max:
                    candidate.append((blank_cnt, i, j))

    candidate.sort(key=lambda x: (-x[0], x[1], x[2]))
    board[candidate[0][1]][candidate[0][2]] = id


def printB(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()


if __name__ == '__main__':
    n = int(input())
    board = [[0]*n for i in range(n)]
    students = [[] for i in range(n**2+1)]
    for i in range(n**2):
        id, a, b, c, d = list(map(int, input().split()))
        favorite = set([a, b, c, d])
        students[id] = favorite
        setBoard(id, favorite)
        # printB(board)
    print(getsatisfaction(board, students))
