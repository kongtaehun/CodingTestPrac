def bt(depth, start):
    if depth == m:
        for i in result:
            print(i, end=' ')
        print()
    else:
        for i in range(start, n):
            result[depth] = nums[i]
            bt(depth+1, i)
            result[depth] = 0


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = [0]*m
bt(0, 0)
