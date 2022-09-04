def bt(depth):
    global result, answer
    if depth == 3:
        if result <= m:
            answer = max(result, answer)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                result += nums[i]
                bt(depth+1)
                visited[i] = 0
                result -= nums[i]


n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
answer = 0
visited = [0]*(n)
bt(0)
print(answer)
