n = 7
board = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
dp = [0]*n


# 상담시간이 길어 퇴사이후까지 이어지는 경우 board에서 없앤다.
def deleteimpossible(board):
    imposible_idx = []
    for i in range(n):
        if (i + board[i][0]) > n:
            imposible_idx.append(i)
    return imposible_idx


def makelink(board, imposible_idx):
    link = [[] for i in range(n)]
    # 현재날짜 + T 이상인 날짜는 선택가능
    for i in range(n):
        temp = []
        if (i+board[i][0] >= n):
            continue
        for j in range(i+board[i][0], n):
            if j in imposible_idx:
                continue
            temp.append(j)
        link[i] = temp
    return link

# 해당날의 선택할 수 있는 것들중 가장 높은 금액
def setMaxDp(board,link):
    for i in link:
        for j in i:
            dp[j][1] = max(dp[j][1],board[i][1]+board[j][1])

# 상담수행이 불가능한 날짜의 인덱스를 구한다
impossIdx = deleteimpossible(board)
# 연결된 링크 리스트 만들기
link = makelink(board, impossIdx)
print(link)
# DP테이블 초기화
