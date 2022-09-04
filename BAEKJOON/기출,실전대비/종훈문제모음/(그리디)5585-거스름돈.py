a = int(input())
a = 1000-a
cash = [500, 100, 50, 10, 5, 1]
cnt = 0
for m in cash:
    cnt += a//m
    a = a % m
print(cnt)
