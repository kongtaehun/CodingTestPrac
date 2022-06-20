from collections import deque
n, m = map(int, input().split())
board = [0 for i in range(100001)]


def bfs(start, board):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        graph = [now+1, now-1, now*2]
        for i in graph:
            if i >= 0 and i < 100001 and board[i] == 0:
                q.append(i)
                board[i] = board[now]+1


bfs(n, board)
print(board[m])
