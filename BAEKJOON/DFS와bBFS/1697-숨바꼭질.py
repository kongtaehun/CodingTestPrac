from collections import deque
n, k = map(int, input().split())
end = 100000
board = [0 for i in range(end+1)]
# bfs로 최대값으로 초기화 없이 한다.


def bfs(start, board):
    q = deque()
    q.append(start)
    board[start] = 1
    while q:
        now = q.popleft()
        link = [now+1, now-1, now*2]
        for i in link:
            if i >= 0 and i < end+1:
                if board[i] == 0:
                    q.append(i)
                    board[i] = board[now]+1


bfs(n, board)
print(board[k]-1)
