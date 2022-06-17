# ======== input ========
m, n, k = map(int, input().split())
board = [[] for i in range(k)]
for i in range(k):
    for i in range(n):
        board[i].append(list(map(int, input().split())))

print(board)
