import sys

n = int(sys.stdin.readline())
allNum = [0]*10001
list = []
for i in range(n):
    temp = int(sys.stdin.readline())
    allNum[temp] += 1


for i in range(10001):
    if allNum[i] != 0:
        for x in range(allNum[i]):
            print(i)
