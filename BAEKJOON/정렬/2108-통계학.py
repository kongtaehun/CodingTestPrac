from collections import Counter
import sys


def getInput():
    input = sys.stdin.readline
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    numbers.sort()
    return numbers, n


def getMode(numbers, n):
    mode_dict = dict(Counter(numbers))
    mode_list = []
    for i in mode_dict.keys():
        mode_list.append((mode_dict[i], i))
    mode_list.sort(reverse=True, key=lambda x: (x[0], - x[1]))
    print(mode_list)
    mode = mode_list[0][1]
    if len(mode_list) > 1 and mode_list[0][0] == mode_list[1][0]:
        mode = mode_list[1][1]
    return mode


numbers, n = getInput()
result = []
median = numbers[n//2]
mean = abs(int(round(sum(numbers)/n, 0))) if int(round(sum(numbers)/n, 0)
                                                 ) == -0 else int(round(sum(numbers)/n, 0))
mode = getMode(numbers, n)
range = abs(numbers[-1]-numbers[0]) if len(numbers) > 1 else 0
print(mean)
print(median)
print(mode)
print(range)
