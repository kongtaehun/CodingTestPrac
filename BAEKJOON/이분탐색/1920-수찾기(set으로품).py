import sys
input = sys.stdin.readline

n = int(input())
num = set(map(int, input().split()))
m = int(input())
answersNum = list(map(int, input().split()))

result = [0 for i in range(m)]
for i, v in enumerate(answersNum):
    if v in num:
        result[i] = 1
for i in result:
    print(i)
