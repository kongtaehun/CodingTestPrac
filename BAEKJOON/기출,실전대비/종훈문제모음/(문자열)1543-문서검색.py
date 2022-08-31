a = list(input())
b = list(input())
size = len(b)
stk = []
idx = 0
cnt = 0
while idx+size <= len(a):
    if a[idx:idx+size] == b:
        idx += size
        cnt += 1
    else:
        idx += 1
print(cnt)
