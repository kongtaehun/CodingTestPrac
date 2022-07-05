from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))
robot = []
base = [[0]*3 for i in range(2)]

q = deque()
for i in nums:
    q.append(i)

for i in range(3):
    # 벨트회전
    print(q)
    q.appendleft(q.pop())
    print(q)

    for i in range(len(robot)):
        next = robot[i]+1
        if next == n-1:
            robot.pop()
        elif q[next] >= 1 and next not in robot:
            robot[i] += 1
            q[next] -= 1

    if q[0] != 0:
        robot.append(0)
        q[0] -= 1
    print(robot)
