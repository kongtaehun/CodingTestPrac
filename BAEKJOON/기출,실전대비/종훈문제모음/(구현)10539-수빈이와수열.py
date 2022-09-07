n = int(input())
b = list(map(int, input().split()))
a = [0]*(n)
now = b[0]*(1)
a[0] = now
for i in range(1, n):
    a[i] = b[i]*(i+1)-now
    now = now+a[i]
print(' '.join(list(map(str, a))))
