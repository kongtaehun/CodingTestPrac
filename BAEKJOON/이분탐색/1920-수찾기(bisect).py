import sys
from bisect import bisect_left, bisect_right
from tabnanny import check
a = [1, 2, 3, 4, 5]
b = 6


input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
m = int(input())
answersNum = list(map(int, input().split()))
result = [0 for i in range(m)]
for i, v in enumerate(answersNum):
    checkIdx = bisect_right(num, v)-1
    if num[checkIdx] == v:
        result[i] = 1
    else:
        result[i] = 0


for i in result:
    print(i)
