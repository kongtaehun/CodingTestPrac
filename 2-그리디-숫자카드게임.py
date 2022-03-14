n, m = map(int, input().split())
board = []
each_min = []
for i in range(n):
    temp = list(map(int, input().split()))
    each_min.append(min(temp))
    board.append(temp)

print(max(each_min))
