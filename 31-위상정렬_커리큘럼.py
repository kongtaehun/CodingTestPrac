'''https://devmath.tistory.com/83'''

from collections import deque
import copy

n = int(input())
indegree = [0 for i in range(n+1)]
graph = [[] for i in range(n+1)]
# 걸리는 시간
time = [0 for i in range(n+1)]
for i in range(1, n+1):
    a = list(map(int, input().split()))
    time[i] = a[0]
    for j in a[1:-1]:
        indegree[i] += 1
        # 선수과목이 현재과목으로 진입하는 것이다
        # 간선의 방향에 유의
        graph[j].append(i)


def topology_sort():
    # 객체를 복사하여 다른 객체로만듬
    # 참조형 변수이므로
    result = copy.deepcopy(time)
    q = deque()  # 큐 선언

    # indegree가 0인것을 찾아서 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌떄까지 반복
    while q:
        # 큐에 있는 원소를 꺼내 현재 인덱스
        now = q.popleft()
        # 현재노드오 ㅏ연결되어있는 노드를 선택(다음과목)
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])


topology_sort()
