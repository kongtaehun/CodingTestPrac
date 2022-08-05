from collections import Counter
# 백트래킹
# 투포인터


def tp(l):
    global result
    visited = set()

    for i in range(l, n):
        if nums[i] in visited:
            return i-l
        visited.add(nums[l])
    return n-l


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0
    for i in range(n):
        # print(tp(i))
        result += tp(i)
    print(result)
