import copy
from collections import deque

# 위상정렬로 풀어볼거임


def topology_sort(graph, q):
    while q:
        now, step, root = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, step+1, root))
                # 부모를 트래킹한다(now와 i를 이용하여)
                result[root].append((i, step+1, now))


# 중복이름 x
if __name__ == '__main__':
    n = int(input())
    names = list(map(str, input().split()))
    idx = {}
    for i in range(n):
        idx[names[i]] = i
    graph = [[] for i in range(n)]
    indegree = [0]*(n)
    for i in range(int(input())):
        a, b = map(str, input().split())
        graph[idx[b]].append(idx[a])
        indegree[idx[a]] += 1
    q = deque()
    root_id = 0
    result = []
    for i in range(n):
        if indegree[i] == 0:
            q.append((i, 1, root_id))
            result.append([])
            result[root_id].append((i, 1, -1))
            root_id += 1

    topology_sort(graph, q)

    # 가문수 출력
    print(len(result))
    # 가문최초조상들 출력
    temp = []
    for i in result:
        temp.append(names[i[0][0]])
    temp.sort()
    print(' '.join(temp))
    # 사람들자식들 출력
    temp = [[] for i in range(n)]
    for i in range(len(result)):
        for j in range(len(result[i])):
            now_step = result[i][j][1]
            now = result[i][j][0]
            for k in range(j+1, len(result[i])):
                if result[i][k][1]-now_step == 1 and result[i][k][2] == now:  # 의심1
                    temp[now].append(result[i][k][0])
    answer = []
    for i in range(n):
        string = names[i] + ' ' + str(len(temp[i])) + ' '
        childs = []
        for j in temp[i]:
            childs.append(names[j])
        childs.sort()
        string += ' '.join(childs)
        answer.append(string)
    answer.sort()
    for i in answer:
        print(i)
