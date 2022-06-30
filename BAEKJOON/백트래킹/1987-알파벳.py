import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bt(depth, x, y):
    global results
    if depth > results:
        results = depth
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in known_alp:
                known_alp.add(board[nx][ny])
                bt(depth+1, nx, ny)
                known_alp.remove(board[nx][ny])


if __name__ == '__main__':
    r, c = map(int, input().split())
    board = []
    for i in range(r):
        board.append(list(input()))
    known_alp = set()
    known_alp.add(board[0][0])
    results = -int(1e9)

    bt(1, 0, 0)
    print(results)
