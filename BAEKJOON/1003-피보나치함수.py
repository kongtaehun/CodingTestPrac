
n = int(input())
board = []
for i in range(n):
    board.append(int(input()))


def fibonacci(a):
    if dp1[a] != 0:
        return dp1[a]
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        dp1[a] = fibonacci(a-1) + fibonacci(a-2)
        dp0[a+1] = fibonacci(a-1) + fibonacci(a-2)
        return fibonacci(a-1) + fibonacci(a-2)


for i in range(n):
    if board[i] == 2:
        print('1 1')

    else:
        dp1 = [0 for _ in range(max(board)+2)]
        dp0 = [0 for _ in range(max(board)+3)]
        dp0[0] = 1
        dp0[1] = 0
        dp1[0] = 0
        dp1[1] = 1
        fibonacci(board[i])
        print(str(dp0[board[i]])+' '+str(dp1[board[i]]))
