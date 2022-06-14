n = int(input())
strlist = set()
for i in range(n):
    strr = input()
    strlist.add((len(strr), strr))
strlist = list(strlist)
strlist.sort(key=lambda x: (x[0], x[1]))
for i in strlist:
    print(i[1])
