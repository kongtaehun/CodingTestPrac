# t = 2
# n = 3
# m = 4
# list1 = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
n2 = 4
m2 = 4
list2 = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]


# dp테이블에 담겨야하는 내용 = 현재 픽셀의 최대값(전단계픽셀들과 계산하여)
d = []
for i in range(n2):
    d.append(list2[i:i+4])

# 현재값 기준으로 전단계의 3개의 합하여 최대인 값


def makemax(n, m):
    if m == 0:
        return d[n][m]
    if n == 0:
        a = d[n][m] + d[n][m-1]
        b = d[n][m] + d[n+1][m-1]
        return max(a, b)
    elif n == n2-1:
        a = d[n][m] + d[n][m-1]
        b = d[n][m] + d[n-1][m-1]
        return max(a, b)
    else:
        a = d[n][m] + d[n][m-1]
        b = d[n][m] + d[n-1][m-1]
        c = d[n][m] + d[n+1][m-1]
        return max(a, b, c)


for i in range(n2):
    for j in range(m2):
        d[i][j] = makemax(i, j)

print(max(max(d)))
