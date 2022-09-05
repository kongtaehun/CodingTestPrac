from itertools import combinations


def getGCD(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


if __name__ == '__main__':
    for _ in range(int(input())):
        temp = list(map(int, input().split()))
        result = 0
        for i in list(combinations(temp[1:], 2)):
            result += getGCD(i[0], i[1])
        print(result)
