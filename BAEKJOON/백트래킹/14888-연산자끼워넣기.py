
def dfs(idx, now):
    global minV, maxV
    if idx == n:
        if minV > now:
            minV = now
        if maxV < now:
            maxV = now
        return

        #todo : 저장
    else:
        for i, v in enumerate(new_oper):
            if oper_visited[i] == 0:
                next = nums[idx]
                oper_visited[i] = 1
                now_origin = now
                now = cal(now, next, v)

                dfs(idx+1, now)
                # 연산방문, 현재값 복구
                oper_visited[i] = 0
                now = now_origin


def cal(now, next, i):
    if i == 0:
        return now + next
    elif i == 1:
        return now - next
    elif i == 2:
        return now * next
    elif i == 3:
        if now < 0:
            now = -now
            return -int(now/next)
        else:
            return int(now/next)


if __name__ == '__main__':
    maxV = -int(1e9)
    minV = int(1e9)
    n = int(input())
    nums = list(map(int, input().split()))
    oper = list(map(int, input().split()))
    new_oper = []
    oper_visited = []
    for i, v in enumerate(oper):
        for j in range(v):
            new_oper.append(i)
            oper_visited.append(0)

    dfs(1, nums[0])
    print(maxV)
    print(minV)
