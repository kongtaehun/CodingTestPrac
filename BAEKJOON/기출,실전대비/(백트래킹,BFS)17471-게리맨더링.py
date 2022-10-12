from collections import deque
# n개를 뽑고 나머지

answer = int(1e9)


def bt(depth, start, mx, teams, n, graph, population):
    global answer
    if depth == mx:

        if check(teams, graph):
            answer = min(getGrade(teams, population), answer)
        return
    else:
        for i in range(start, n):
            if teams[i] == 0:
                teams[i] = 1
                bt(depth+1, i, mx, teams, n, graph, population)
                teams[i] = 0


def getGrade(teams, population):
    team_grade = [0, 0]
    for i in range(len(teams)):
        team_grade[teams[i]] += population[i]
    return abs(team_grade[1] - team_grade[0])


def check(teams, graph):
    zero_flag = 0
    one_flag = 0
    for i in range(len(teams)):
        if teams[i] == 0:

            if bfs(i, graph, teams):
                zero_flag = 1
            break
    for i in range(len(teams)):
        if teams[i] == 1:
            if bfs(i, graph, teams):
                one_flag = 1
            break
    if zero_flag == 1 and one_flag == 1:
        return True
    else:
        return False


def bfs(start, graph, teams):
    v = [0]*(len(teams))
    team = teams[start]
    q = deque()
    v[start] = 1
    q.append(start)
    while q:
        now = q.popleft()
        for e in graph[now]:
            if v[e] == 0 and teams[e] == team:
                q.append(e)
                v[e] = 1

    for i in range(len(teams)):
        if teams[i] == team:
            if v[i] == 0:
                return False
    return True

# 같은 선거구끼리 연결이 되어있는지 확인(bfs)


def solution():
    global answer
    n = int(input())
    population = list(map(int, input().split()))
    graph = [[] for i in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(temp[0]):
            graph[i].append(temp[j+1]-1)
            graph[temp[j+1]-1].append(i)

    teams = [0]*(n)
    # 1개부터 n개까지 for
    # n=2ㅇ일떼 포함될때 반복문이 아예시작이 안댐
    for mx in range(1, n):
        bt(0, 0, mx, teams, n, graph, population)
    if answer == int(1e9):
        print(-1)
    else:
        print(answer)


solution()
