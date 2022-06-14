import sys
input = sys.stdin.readline
n = int(input())
reserved_numbers = set(map(int, input().split()))
m = int(input())
answer_numbers = list(map(int, input().split()))


result = []
for i in answer_numbers:
    if i in reserved_numbers:
        print('1', end=' ')
    else:
        print('0', end=' ')
