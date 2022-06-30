def bt(arr, depth, me):
    if depth == m:
        print(result)
    else:
        for i in range(n):
            if i == me:
                continue
            result[depth] = arr[i]
            bt(arr, depth+1, i)
            result[depth] = 0


n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = [0]*m
bt(nums, 0, 0)
