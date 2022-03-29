n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)


count = 0
while True:
    if len(a) == 0:
        break
    if a[0] <= len(a):
        del a[:a[0]]
        count += 1
    else:
        break

print(count)
