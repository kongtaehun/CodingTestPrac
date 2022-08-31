dic = {}
for i in range(int(input())):
    temp = input()
    if temp in set(dic.keys()):
        dic[temp] += 1
    else:
        dic[temp] = 0
max_val = max(dic.values())
result = []
for key in dic.keys():
    if dic[key] == max_val:
        result.append(key)
result.sort()

print(result[0])
