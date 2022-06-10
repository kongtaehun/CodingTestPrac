def solution(m, n, puddles):
    # 격자 초기화
    board = [[-1]*m for i in range(n)]
    # 웅덩이 초기화
    for i in puddles:
        board[i[1]-1][i[0]-1] = 0
    # 끝값 초기화
    hasPuddles = 0
    for i in range(m-1, -1, -1):
        if board[n-1][i] == 0:
            hasPuddles = 1
        if hasPuddles == 1:
            board[n-1][i] = 0
        else:
            board[n-1][i] = 1

    hasPuddles = 0
    for i in range(n-1, 0-1, -1):
        if board[i][m-1] == 0:
            hasPuddles = 1
        if hasPuddles == 1:
            board[i][m-1] = 0
        else:
            board[i][m-1] = 1

    print(board)

    #
    for m_ in range(m-2, -1, -1):
        for n_ in range(n-2, -1, -1):
            if board[n_][m_] == 0:
                board[n_][m_] = 0
            else:
                board[n_][m_] = board[n_+1][m_]+board[n_][m_+1]

    return board[0][0] % 1000000007
