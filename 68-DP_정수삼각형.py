n = int(input())
list_ = []

for i in range(0, n):
    list_.append(list(map(int, input().split())))


def makemax(x, y):
    if x == 0:
        return list_[x][y]
    if y == 0:  # 맨 왼쪽일 경우
        return list_[x][y] + list_[x-1][y]  # -행 위의 -1열, 0열
    elif y == len(list_[x])-1:  # 맨 오른쪽일경우
        return list_[x][y] + list_[x-1][y-1]
    else:
        a = list_[x][y] + list_[x-1][y]
        b = list_[x][y] + list_[x-1][y-1]
        return max(a, b)


for i in range(n):
    for j in range(len(list_[i])):
        list_[i][j] = makemax(i, j)
print(max(max(list_)))
