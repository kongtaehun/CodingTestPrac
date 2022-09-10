n, l, k = map(int, input().split())
probs = []
for i in range(n):
    a, b = map(int, input().split())
    probs.append((b, a))
probs.sort()

grade = 0
cnt = 0
for a, b in probs:
    if a <= l:
        grade += 140
    if a > l and b <= l:
        grade += 100

    if cnt >= k:
        break

print(grade)
