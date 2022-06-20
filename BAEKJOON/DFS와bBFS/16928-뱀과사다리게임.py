from collections import deque
# 1. 사다리,뱀의 도착지점은 한점에 여러개가 있을 수 있다
# -> 도착지점의 board[]가 0인지 아닌지 고려해줘야한다.


def bfs(start, board, ladderSnake):
    q = deque()
    q.append(start)
    board[start] = 1
    while q:
        now = q.popleft()
        dx = [now+1, now+2, now+3, now+4, now+5, now+6]
        for i in dx:
            if i < 101 and i > 0:
                if ladderSnake[i] != 0:
                    i = ladderSnake[i]
                if board[i] == 0 or board[i] > board[now]+1:
                    q.append(i)
                    board[i] = board[now]+1


n, m = map(int, input().split())
board = [0 for i in range(101)]
ladderSnake = [0 for i in range(101)]
for i in range(n):
    a, b = map(int, input().split())
    ladderSnake[a] = b

for i in range(m):
    a, b = map(int, input().split())
    ladderSnake[a] = b
bfs(1, board, ladderSnake)
print(board[100]-1)
