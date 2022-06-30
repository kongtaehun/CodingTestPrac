from itertools import combinations
S = 6


def printArr(arr):
    for i in range(len(arr)):
        for j in range(S):
            print(arr[i][j], end=' ')
        print()
    print()


while True:
    nums = list(map(int, input().split()))
    k = nums.pop(0)
    if k == 0:
        break
    else:
        printArr(list(combinations(nums, S)))
