import copy
from collections import deque

skylines = []
for i in range(int(input())):
    skylines.append(list(map(int, input().split())))

skylines.sort()
height = []
height.append(0)
for i in skylines:
    height.append(i[1])
height.append(0)
# 슬라이딩 윈도우로 3개씩 검사해서
# 중간값이 최댓값일 때 중간값을 없애버림
# 양없에 0을 추가
# 양옆값이 값이 같을경우 왼쪽거로 통일

count = 0


while len(height) > 2:
    q = deque()
    now_idx = 0
    temp = []
    while True:

        if len(q) < 3:
            if now_idx < len(height):
                q.append(height[now_idx])
                now_idx += 1
            else:
                if not q:
                    break
                temp.append(q.popleft())
        else:
            # q의 중간값이 가장 클떄

            if q[1] > q[2] and q[1] > q[0]:
                # 양옆값이 동일할 때
                if q[0] == q[2]:
                    q.popleft()
                    q.popleft()
                    count += 1
                # 양옆값이 다를때
                else:
                    q = deque([q[0], q[2]])
                    count += 1
            # q의 중간값이 가장 크기 않을 때
            elif q[1] == q[2] or q[0] == q[1]:
                if q[1] == [2]:
                    q = deque([q[0], q[1]])
                elif q[1] == q[0]:
                    q = deque([q[0], q[2]])
            else:
                temp.append(q.popleft())

        # print(q, temp)

    for i in q:
        temp.append(i)
    height = copy.deepcopy(temp)
    # print("중간결과 : " + str(temp))
print(count)
