def bt(depth, start):
    global count
    if depth == limit:
        if sum(result) == S:
            count += 1

    else:
        for i in range(start, n):
            if visited[i] == 0:
                visited[i] = 1
                result[depth] = nums[i]
                bt(depth+1, i)
                visited[i] = 0
                result[depth] = 0


if __name__ == '__main__':
    n, S = map(int, input().split())
    visited = [0]*(n)
    nums = list(map(int, input().split()))
    count = 0

    for limit in range(1, n+1):
        result = [0]*(limit)
        bt(0, 0)
    print(count)
