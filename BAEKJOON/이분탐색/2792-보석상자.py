import math
import sys
input = sys.stdin.readline


def distribute(maxSize, arr):
    student_count = 0
    for i in arr:
        student_count += math.ceil(i/maxSize)
    return student_count


def binary_search(arr, target):
    end = max(arr)
    start = 1
    while start <= end:
        mid = (start+end)//2
        temp = distribute(mid, arr)
        if temp > target:
            start = mid+1
        else:
            end = mid - 1
    return start


if __name__ == '__main__':
    n, m = map(int, input().split())
    stone = []
    for i in range(m):
        stone.append(int(input()))
    stone.sort()
    print(binary_search(stone, n))
