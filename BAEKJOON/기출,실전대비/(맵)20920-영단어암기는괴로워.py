n, m = map(int, input().split())
dic = dict()
for i in range(n):
    strr = input()
    if len(strr) >= m:

        if strr in dic:
            dic[strr][2] += 1
        else:
            dic[strr] = [strr, len(strr), 1]

temp = list(dic.values())
temp.sort(key=lambda x: (-x[2], -x[1], x[0]))


for i in temp:
    print(i[0])
