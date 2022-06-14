import sys


def getNGE(a, rightside):
    if max(rightside) <= a or len(rightside) == 0:
        return -1

    for i in rightside:
        if a < i:
            return i


input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
result = []
for i, v in enumerate(numbers):
    result.append(getNGE(v, numbers[i:]))
print(result)
