dp = [[[0]*(101) for i in range(101)] for i in range(101)]


def w(a, b, c):
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        dp[a][b][c] = w(20, 20, 20)
        return w(20, 20, 20)
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1)-w(a-1, b-1, c-1)
        return dp[a][b][c]


input_list = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    input_list.append([a, b, c])

for i in range(len(input_list)):
    print(
        f"w({int(input_list[i][0])}, {int(input_list[i][1])}, {int(input_list[i][2])}) = {w(input_list[i][0],input_list[i][1],input_list[i][2])}")
