
strr = input()
strset = set()
for i in range(1, len(strr)+1):
    start = 0
    while start+i <= len(strr):
        strset.add(strr[start:start+i])
        start += 1
print(len(strset))
