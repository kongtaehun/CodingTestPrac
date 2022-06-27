strr = input()
t = int(input())
q = []
dict = {}
for i in range(t):
    temp = list(map(str, input().split()))
    q.append(temp)
alphabat = [[0]*(len(strr)+1) for i in range(26)]
for i in range(1, len(strr)+1):
    for j in range(26):
        alphabat[j][i] = alphabat[j][i-1]
    alphabat[ord(strr[i-1])-97][i] = alphabat[ord(strr[i-1])-97][i-1]+1

for alp, start, end in q:
    print(alphabat[ord(alp)-97][int(end)+1] -
          alphabat[ord(alp)-97][int(start)])


