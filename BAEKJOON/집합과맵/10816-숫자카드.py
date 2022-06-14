from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
reserved_numbers = list(map(int, input().split()))
m = int(input())
answer_numbers = list(map(int, input().split()))


numbers_dict = dict(Counter(reserved_numbers))
keys = set(numbers_dict.keys())

result = []
for i in answer_numbers:
    if i in keys:
        print(numbers_dict[i], end=' ')

    else:
        print(0, end=' ')
