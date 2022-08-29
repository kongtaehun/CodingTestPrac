def cal(a, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = abs(a[i][j]-1)


def check(a, b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, list(input()))) for i in range(n)]
    b = [list(map(int, list(input()))) for i in range(n)]
    cnt = 0

    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                cal(a, i, j)
                cnt += 1
    if check(a, b):
        print(cnt)
    else:
        print(-1)
