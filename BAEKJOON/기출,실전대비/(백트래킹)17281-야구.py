
from collections import deque

answer = -int(1e9)


def bt(depth, visited, result, nums, inings):
    global answer
    if depth == 8:
        answer = max(gameStart(result, nums, inings), answer)
        return
    for i in range(1, 9):
        if visited[i] == 0:
            visited[i] = 1
            result[depth] = i
            bt(depth+1, visited, result, nums, inings)
            result[depth] = -1
            visited[i] = 0


def gameStart(order, nums, inings):
    order = order[:3] + [0] + order[3:]
    now_striker = 0
    grade = 0
    for ining in range(inings):
        b1 = 0
        b2 = 0
        b3 = 0
        out_cnt = 0
        while out_cnt <= 2:
            if nums[ining][order[now_striker]] == 0:
                out_cnt += 1
            elif nums[ining][order[now_striker]] == 1:
                grade += b3
                b3 = b2
                b2 = b1
                b1 = 1

            elif nums[ining][order[now_striker]] == 2:
                grade += b3+b2
                b3 = b1
                b1 = 0
                b2 = 1

            elif nums[ining][order[now_striker]] == 3:
                grade += b3+b2+b1
                b1 = 0
                b2 = 0
                b3 = 1
            else:
                grade += b1+b2+b3+1
                b1 = 0
                b2 = 0
                b3 = 0
            now_striker += 1
            now_striker %= 9

    return grade


def solutions():
    global answer
    nums = []
    inings = int(input())
    for _ in range(inings):
        nums.append(list(map(int, input().split())))

    visited = [0 for i in range(9)]

    result = [-1, -1, -1, -1, -1, -1, -1, -1]
    bt(0, visited, result, nums, inings)
    print(answer)


solutions()
