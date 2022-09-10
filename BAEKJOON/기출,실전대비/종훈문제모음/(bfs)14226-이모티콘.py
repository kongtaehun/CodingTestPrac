from collections import deque
# bfs로 최단거리를 찾는거다!


def bfs(visited):  # 소수의 순서대로 번호가 1씩 증가하,자:
    q = deque()
    visited[1][1] = 1
    q.append((1, 1))
    while q:
        now, clipboard = q.popleft()
        # clipboard의 이모티콘 개수
        moves = [[now-1, clipboard],
                 [now+clipboard, clipboard],
                 [now, now]]
        for i, clip in moves:
            if 1 <= i < SIZE+1 and 1 <= clip < SIZE+1 and visited[i][clip] == INF:
                visited[i][clip] = visited[now][clipboard]+1
                q.append((i, clip))


if __name__ == '__main__':
    SIZE = 1000
    INF = int(1e9)
    n = int(input())
    # visited[현재이모티콘수][현재클립보드]
    visited = [[INF]*(1001) for i in range(1001)]
    bfs(visited)
    # print(visited)
    print(min(visited[n]))
