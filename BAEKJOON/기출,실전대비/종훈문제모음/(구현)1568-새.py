if __name__ == '__main__':
    n = int(input())
    now = 1
    cnt = 0
    while n > 0:
        cnt += 1
        n -= now
        now += 1
        if now > n:
            now = 1
    print(cnt)
