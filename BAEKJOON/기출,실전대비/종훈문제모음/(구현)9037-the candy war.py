
for i in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    answer = 0
    # 사전보충
    for i in range(n):
        if c[i] % 2 != 0:
            c[i] += 1
    while True:
        flag = 1
        for i in range(1, n):
            if c[i] != c[0]:
                flag = 0
                break
        if flag == 1:
            break
        new_c = [0]*(n)
        for i in range(n):
            if i == n-1:
                new_c[0] = c[i]//2
                c[i] = c[i]//2
            else:
                new_c[i+1] = c[i]//2
                c[i] = c[i]//2

        for i in range(n):
            c[i] += new_c[i]
            if c[i] % 2 != 0:
                c[i] += 1
        # print(c, new_c)
        answer += 1
        flag = 1
        for i in range(1, n):
            if c[i] != c[0]:
                flag = 0
                break
        if flag == 1:
            break
    print(answer)
