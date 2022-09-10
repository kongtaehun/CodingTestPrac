INF = int(1e9)
# 백트래킹


def bt(depth):
    global result, answer
    if depth == 3:
        # print(result)
        answer = min(answer, result)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if visited[i][j] == visited[i-1][j] == visited[i][j-1] == visited[i+1][j] == visited[i][j+1] == 0:
                    visited[i][j] = 1
                    visited[i-1][j] = 1
                    visited[i][j-1] = 1
                    visited[i+1][j] = 1
                    visited[i][j+1] = 1
                    result += board[i][j]
                    result += board[i-1][j]
                    result += board[i][j-1]
                    result += board[i+1][j]
                    result += board[i][j+1]
                    bt(depth+1)
                    visited[i][j] = 0
                    visited[i-1][j] = 0
                    visited[i][j-1] = 0
                    visited[i+1][j] = 0
                    visited[i][j+1] = 0
                    result -= board[i][j]
                    result -= board[i-1][j]
                    result -= board[i][j-1]
                    result -= board[i+1][j]
                    result -= board[i][j+1]


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    visited = [[0]*(n) for i in range(n)]
    result = 0
    answer = INF
    bt(0)
    print(answer)
