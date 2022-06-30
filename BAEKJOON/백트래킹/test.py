def bt(arr, depth):
    if depth == m:
        for i in result:
            print(i, end=' ')
        print()
    else:
        for i in range(n):
            if arr[i] in result:
                continue
            result[depth] = arr[i]
            bt(arr, depth+1)
            result[depth] = 0


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = [0]*m
bt(nums, 0)
