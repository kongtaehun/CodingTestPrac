import sys

n = int(sys.stdin.readline())
allNum = [0]*10001
for i in range(n):

    allNum[int(sys.stdin.readline())] += 1


for i in range(10001):
    if allNum[i] != 0:
        for x in range(allNum[i]):
            print(i)
