import sys
from bisect import bisect_right
input = sys.stdin.readline


def longest_ascending_binary(arr):
    lis = []
    lis.append(arr[0])
    for i in range(1, n):
        idx = bisect_right(lis, arr[i])
        if idx > len(lis)-1:
            lis.append(arr[i])
        else:
            lis[idx] = arr[i]
    return len(lis)


def longest_ascending_for(arr):
    length = [0]*n
    for k in range(n):
        length[k] = 1
        for i in range(k):
            if arr[i] < arr[k]:
                length[k] = max(length[k], length[i]+1)

    return max(length)


def longest_ascending_bt(depth, start):
    global longest
    if depth > longest:
        longest = depth

    for i in range(start, n):
        if (depth == 0) or (visited[i] == 0 and result[-1] < nums[i]):
            visited[i] = 1
            result.append(nums[i])
            longest_ascending_bt(depth+1, i)
            visited[i] = 0
            result.pop()


if __name__ == '__main__':
    n = int(input())
    nums = [int(input()) for i in range(n)]
    visited = [0]*(n)
    result = []

    longest = longest_ascending_binary(nums)

    print(n-longest)
    # 최장 증가하는 수열
