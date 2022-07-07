from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))
robot = [0]*n
base = [[0]*n for i in range(2)]

q = deque()
for i in nums:
    q.append(i)
result = 0
while True:

    result += 1
    # step1 : 벨트회전(로봇과함께)
    q.appendleft(q.pop())
    for i in range(len(robot)-2, -1, -1):
        if robot[i] == 1:
            robot[i] = 0
            robot[i+1] = 1

    robot[-1] = 0
    #step2 : 로봇이동
    for i in range(len(robot)-2, -1, -1):
        if robot[i] == 1:
            # 로봇이 내리는칸에 도달했을 때 로봇없애기
            # 로봇앞에 로봇이 없고 내구도가 1이상인경우 경우 로봇앞으로이동
            if robot[i+1] == 0 and q[i+1] >= 1:
                if i+1 == len(robot)-1:
                    robot[i] = 0
                    q[i+1] -= 1
                else:
                    robot[i] = 0
                    robot[i+1] = 1
                    q[i+1] -= 1

    # step 3 : 로봇올리기
    if q[0] > 0:
        robot[0] = 1
        q[0] -= 1

    # step 4 : 종료하기

    count = 0
    for i in q:
        if i == 0:
            count += 1
    if count >= k:
        break

print(result)
