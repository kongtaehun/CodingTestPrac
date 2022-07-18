
flag = 1


def dc(n, x, y, count):
    global result, flag

    if flag == 0:
        return

    if n == 1 and x == r and y == c:
        result = count
        flag = 0
        return
    elif n == 1:
        return
    else:
        if x <= r < x+n//2 and y <= c < y+n//2:
            dc(n//2, x, y, count)
        elif x <= r < x+n//2 and y+n//2 <= c < N:
            dc(n//2, x, y+n//2, count+((n//2)**2))
        elif x+n//2 <= r < N and y <= c < y+n//2:
            dc(n//2, x+n//2, y, count+2*((n//2)**2))
        elif x+n//2 <= r < N and y+n//2 <= c < N:
            dc(n//2, x+n//2, y+n//2, count+3*((n//2)**2))


if __name__ == '__main__':
    n, r, c = map(int, input().split())
    N = 2**(n)
    n = 2**(n)
    result = 0
    count = 0
    dc(n, 0, 0, 0)
    print(result)
