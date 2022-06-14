n = int(input())
members = []
for i in range(n):
    age, name = map(str, input().split())
    members.append((i, int(age), name))
members.sort(key=lambda x: (x[1], x[0]))
for i in members:
    print(str(i[1]) + ' ' + i[2])
