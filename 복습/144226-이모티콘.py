from collections import deque
# 클립보드를 구현해야함


def bfs(s):
    q = deque()
    visited = [[-1]*(s+1) for i in range(s+1)]
    q.append((1, 0))
    # 현재이모티콘수는 1이고 복사된 클립보드의 이모티콘수는 0(클립보드가 없다)
    visited[1][0] = 0
    while q:
        now, clip = q.popleft()  # 현재 클립보드
        if visited[now][now] == -1:
            # 현재이모티콘수, 복사해서 클립보드가 현재이모티콘
            visited[now][now] = visited[now][clip]+1
            q.append((now, now))  # 현재이모티콘수그대로, 클립보드는 현재이모티콘수로
        # 붙혀넣기 로직
        if now+clip <= s and visited[now+clip][clip] == -1:
            visited[now+clip][clip] = visited[now][clip]+1
            q.append((now+clip, clip))
        if now - 1 >= 0 and visited[now-1][clip] == -1:
            visited[now-1][clip] = visited[now][clip]+1
            q.append((now-1, clip))
    return visited


def solution():
    s = int(input())
    # 행은 현재 이모티콘수
    # 열은 현재 클립보드
    # 이모티콘 == 클립보드 -> 클립보드 없는 것

    visited = bfs(s)
    answer = int(1e9)
    for i in range(s+1):
        if visited[s][i] != -1:
            answer = min(answer, visited[s][i])
    print(answer)


solution()
