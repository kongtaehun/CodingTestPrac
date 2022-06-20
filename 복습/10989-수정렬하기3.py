import sys
input = sys.stdin.readline

n = int(input())
sortednum = [0 for i in range(10001)]
for i in range(n):
    sortednum[int(input())] += 1
for i, v in enumerate(sortednum):
    
        for x in range(v):
            print(i)
