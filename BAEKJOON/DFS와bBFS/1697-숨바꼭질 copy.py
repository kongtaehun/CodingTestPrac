# bfs
from collections import deque


def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        move = [now+1, now-1, now*2]
        for i in move:
            if 0 <= i < 100001:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[now]+1


if __name__ == '__main__':
    n, k = map(int, input().split())
    road = [0]*(100001)
    bfs(n, road)
    print(road[k]-1)
