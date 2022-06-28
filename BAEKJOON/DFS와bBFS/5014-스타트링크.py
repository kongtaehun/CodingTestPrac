from collections import deque


def bfs(start, visited):
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        now = q.popleft()
        nx = [now+u, now-d]
        for i in nx:
            if 0 < i <= f:
                if visited[i] > visited[now]+1:
                    q.append(i)
                    visited[i] = visited[now]+1


Non = int(1e9)
f, s, g, u, d = map(int, input().split())
visited = [Non]*(f+1)
bfs(s, visited)

print(visited[g]-1 if visited[g] != Non else 'use the stairs')
