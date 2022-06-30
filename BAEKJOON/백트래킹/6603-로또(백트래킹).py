S = 6


def printArr(arr):
    for i in range(len(arr)):
        for j in range(S):
            print(arr[i][j], end=' ')
        print()
    print()


def bt(depth, arr):
    if depth == S:
        printArr(result)
    else:
        for i in arr:
            if visited[i] == 0:
                visited[i] = 1
                result[depth] = i
                bt(depth+1, arr)
                result[depth] = 0
                visited[i] = 0


while True:
    nums = list(map(int, input().split()))
    k = nums.pop(0)
    visited = [0]*(k+1)
    result = [0]*S
    if k == 0:
        break
    else:
        bt(0, nums)
