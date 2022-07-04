from collections import deque


def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        now = q.popleft()
        dx = [now+1, now-1]
        for i in dx:
            if 0 <= i < 100001 and (visited[i] == -1 or visited[i] > visited[now]+1):
                visited[i] = visited[now]+1
                q.append(i)
        if 0 <= now*2 < 100001 and (visited[now*2] == -1 or visited[now*2] > visited[now]):
            q.append(now*2)
            visited[now*2] = visited[now]


if __name__ == '__main__':
    n, k = map(int, input().split())
    visited = [-1]*100001
    bfs(n, visited)
    print(visited[k])
