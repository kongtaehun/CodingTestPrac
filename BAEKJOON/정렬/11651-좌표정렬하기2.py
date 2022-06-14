n = int(input())
num = []
for i in range(n):
    a, b = list(map(int, input().split()))
    num.append((a, b))

num.sort(key=lambda x: (x[1], x[0]))

for i in num:
    print(str(i[0])+' '+str(i[1]))
