#백트래킹 실패

import sys
sys.setrecursionlimit(10**6)
from itertools import combinations
# 배열의 요소개수가 8이고 M은 3일 경어
# 1~8까지의 수중에서 3을 중복없이 뽑는것


def countMaxDiff(arrs):
    max_val = 0
    for arr in arrs:
        if arr:
            part_grade = max(arr)-min(arr)
            max_val = max(max_val, part_grade)
    return max_val
# m개로 나눈다. -> 가림막의 위치를 뽑는다.


def divideArr(depth, arr, m, start):
    global val
    if len(screens) == m-1:
        # print(screens)
        temp = []
        temp.append(arr[:screens[0]])
        for i in range(1, len(screens)):
            temp.append(arr[screens[i-1]:screens[i]])
        temp.append(arr[screens[-1]:])
        # print(temp)
        val = min(countMaxDiff(temp), val)
        # print(val)
    else:
        for i in range(start, len(arr)):
            if visited[i] == 0:
                screens.append(i)
                visited[i] = 1
                divideArr(depth+1, arr, m, i)
                screens.pop()
                visited[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if m == 1:
        print(max(arr)-min(arr))
    else:
        screens = []
        visited = [0]*(n)
        val = int(1e9)
        divideArr(0, arr, m, 1)
        print(val)
