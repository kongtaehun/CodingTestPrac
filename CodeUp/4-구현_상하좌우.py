n = int(input())
t = list(map(str, input().split()))
x = 0
y = 0
for i in t:
    if i == 'R' and y < n:
        y = y+1
    elif i == 'L' and y > 0:
        y = y-1
    elif i == 'U' and x > 0:
        x = x-1
    elif i == 'D' and x < n:
        x = x+1
print('%d %d' % (x+1, y+1))
