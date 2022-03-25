# 큐를 이용한다.
from collections import deque

# 노드, 간선정보 입력
n, m = map(int, input().split())
# 진입차수 선언
indegree = [0 for i in range(n+1)]
# 간선 정보 선언
graph = [[] for i in range(n+1)]

# ㅂ간선정보 입력받고 진입차수 늘리기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬


def topology_sort():
    # 큐에서 뺄때마다 추가한다
    result = []
    q = deque()
    # 진입차수가 0 인 것을 찾아서 큐에 입력
    for i in range(n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 결과 리스트에 저장하기
        result.append(now)
        # 꺼낸 노드와 연결된 모든 노드의 진입차수를 1낮춤
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수 0 이 되었을경우 큐삽입
            if indegree[i] == 0:
                q.append(i)
    return result


result = topology_sort()
for i in result[1:]:
    print(i, end=' ')
