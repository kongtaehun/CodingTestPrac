string = list(input())
chrs = [[0, i] for i in range(91)]
for i in string:
    ch = ord(i)
    if ord(i) >= 97:
        ch -= 32
    chrs[ch][0] += 1

chrs.sort(reverse=True)
if chrs[0][0] == chrs[1][0]:
    print('?')
else:
    print(chr(chrs[0][1]))
