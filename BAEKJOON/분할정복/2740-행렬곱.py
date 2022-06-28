n, m = map(int, input().split())
board1 = []
for i in range(n):
    board1.append(list(map(int, input().split())))

board2 = []
m, k = map(int, input().split())
for i in range(m):
    board2.append(list(map(int, input().split())))

new_board = [[0]*k for i in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            new_board[i][j] += board1[i][x]*board2[x][j]

for i in range(n):
    for j in range(k):
        print(new_board[i][j], end=' ')
    print()
