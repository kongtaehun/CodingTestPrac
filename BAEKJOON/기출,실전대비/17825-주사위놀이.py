def move(start, dist):
    if len(graph[start]) >= 2:
        start = graph[start][1]
        dist -= 1
    # 파란색
    # 두번째 길을 선택해야한다.
    for _ in range(dist):
        if start >= 32:
            return 32
        start = graph[start][0]

    return start


def bt(depth):
    global result, answer

    if depth == 10:
        print(result)
        answer = max(result, answer)

    else:
        for j in range(4):
            dist = nums.pop()
            origin = horse[j]
            arrived = move(horse[j], dist)
            if arrived in horse:  # 속도느려짐
                nums.append(dist)
                continue
            result += cost[arrived]
            horse[j] = arrived
            bt(depth+1)
            nums.append(dist)
            horse[j] = origin
            result -= cost[arrived]


if __name__ == '__main__':
    horse = [0, 0, 0, 0]  # 말의 위치를 나타내는 변수
    graph = [[] for i in range(33)]
    cost = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30,
            32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
    for i in range(20):
        graph[i].append(i+1)
    graph[20].append(32)
    graph[5].append(21)
    graph[21].append(22)
    graph[22].append(23)
    graph[23].append(29)

    graph[10].append(24)
    graph[24].append(25)
    graph[25].append(29)

    graph[15].append(26)
    graph[26].append(27)
    graph[27].append(28)
    graph[28].append(29)

    graph[29].append(30)
    graph[30].append(31)
    graph[31].append(20)

    nums = list(map(int, input().split()))
    visited = [0]*(10)
    result = 0
    answer = 0
    bt(0)
    print(answer)
