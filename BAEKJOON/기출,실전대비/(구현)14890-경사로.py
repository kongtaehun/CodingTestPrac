

def lineCheck(arr, l):
    # 경사도 차이가 1이어야함
    # l만큼의 여유평지가 있어야함
    # 내리막방향으로만 체크한다.
    flag = 0
    runway = [0]*(len(arr))
    reverse_arr = list(reversed(arr))

    if check(arr, l, runway):

        flag += 1
    reverse_runway = list(reversed(runway))
    if check(reverse_arr, l, reverse_runway):
        flag += 1
    if flag == 2:
        return True
    else:
        return False


def check(arr, l, runway):
    i = 0
    while i+1 < len(arr):
        # 내리막일 경우
        if arr[i] > arr[i+1]:
            if abs(arr[i]-arr[i+1]) >= 2:
                return False
            # 경사로 설치
            for j in range(i+1, i+1+l):
                # print(runway)
                if j < len(arr) and runway[j] == 0 and arr[i+1] == arr[j]:
                    runway[j] = 1
                else:
                    return False
            i += l
        # 둘이 같을경우(평지)
        else:
            i += 1
    return True


if __name__ == '__main__':
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    temp_board = [[] for i in range(n)]
    cnt = 0
    for i in range(n):
        if lineCheck(board[i], l):
            # print("가로" + str(i+1) + "번째줄" + "True")
            cnt += 1
        # else:
        #     print("가로" + str(i+1) + "번째줄" + "False")
        temp_arr = []
        for j in range(n):
            temp_arr.append(board[j][i])

        if lineCheck(temp_arr, l):
            # print("새로" + str(i+1) + "번째줄" + "True")
            cnt += 1
        # else:
        #     print("세로" + str(i+1) + "번째줄" + "False")

    print(cnt)
