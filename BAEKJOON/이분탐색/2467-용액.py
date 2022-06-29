from collections import deque
import sys
input = sys.stdin.readline


def bfs(s, graph, mid, e):
    visited = [0]*(n+1)
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        now = q.popleft()

        if now == e:
            return True
        for i, c in graph[now]:
            if c >= mid and visited[i] == 0:
                q.append(i)
                visited[i] = 1
    return False


def binary_search(max_weight, min_weight, graph, s, e):
    start = min_weight
    end = max_weight

    while start <= end:
        mid = (start+end)//2
        # mid일 떄 통행이 가능한지
        canPass = bfs(s, graph, mid, e)
        # print("가능 cost가" + str(mid)+"일 떄 " + str(canPass))
        if canPass:
            start = mid+1
        else:
            end = mid-1
    return end


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    min_weight = 1
    max_weight = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        max_weight = max(max_weight, c)
    s, e = map(int, input().split())
    print(binary_search(max_weight, min_weight, graph, s, e))
