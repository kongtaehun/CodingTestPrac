m, n, h = map(int, input().split())
board = []
for k in range(h):
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split())))
    board.append(temp)
print()
