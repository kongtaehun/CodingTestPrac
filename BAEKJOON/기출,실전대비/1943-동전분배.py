# 투포인터로는 못풀거같다!
flag = 0


def bt(depth, start):
    global flag, answer, result
    if result == total_cash//2:
        flag == 1
        answer = 1
        return
    if result > total_cash//2 or flag == 1 or depth >= len(cashs)-1:
        return

    else:
        for i in range(start, len(cashs)):
            if visitied[i] == 0:
                visitied[i] = 1
                result += cashs[i]
                bt(depth+1, i)
                visitied[i] = 0
                result -= cashs[i]


for i in range(3):
    # 변수 ---------
    n = int(input())
    total_cash = 0
    cashs = []
    result = 0
    answer = 0

    # 입력 ----------
    for i in range(n):
        cash, cnt = map(int, input().split())
        temp = [cash]*cnt
        cashs += temp
        total_cash += cash*cnt
    cashs.sort(reverse=True)
    visitied = [0]*(len(cashs))
    bt(0, 0)
    print(answer)
# for i in result:
#     print(i)
