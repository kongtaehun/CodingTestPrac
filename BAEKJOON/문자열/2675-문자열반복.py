for i in range(int(input())):
    n, strr = map(str, input().split())
    for i in strr:
        for _ in range(int(n)):
            print(i, end='')
    print()
