# 이분탐색??
def check(board, now):
    st = set()
    for j in range(c):
        temp = ''
        for i in range(now, r):
            temp += board[i][j]
        if temp in st:
            return False
        else:
            st.add(temp)
    return True


def binary_serch():
    start = 0
    end = r
    while start <= end:
        mid = (start+end)//2
        if check(board, mid):
            start = mid+1
        else:
            end = mid-1
    return start


if __name__ == '__main__':

    r, c = map(int, input().split())
    board = [list(input()) for i in range(r)]

    print(binary_serch()-1)
