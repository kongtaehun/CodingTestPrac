
# 모든칸이 한번 방문했는지
# 시작점으로 돌아왔는지
# 매 이동이 합당한지
def unitValidater(a, b):  # a에서 b로 이동하는 것이 맞는지
    temp1 = abs(a[0]-b[0])
    temp2 = abs(a[1]-b[1])
    if (temp1 == 1 and temp2 == 2) or (temp1 == 2 and temp2 == 1):
        return True
    else:
        return False


def totalValidator(moves):
    visited = [[0]*6 for i in range(6)]
    # 매 이동마다 검사하기
    for i in range(len(moves)-1):
        visited[moves[i][0]][moves[i][1]] += 1
        if not unitValidater(moves[i], moves[i+1]):
            return False
    visited[moves[-1][0]][moves[-1][1]] = 1
    # 모두 한번씩 방문했는지 확인
    for i in range(6):
        for j in range(6):
            if visited[i][j] != 1:
                return False
    # 시작이량 끝이 이동가능한지
    if unitValidater(moves[-1], moves[0]):
        return True
    else:
        return False


def solution():
    moves = []
    for i in range(36):
        temp = input()
        a = ord(temp[0])-65
        b = int(temp[1])-1
        moves.append((a, b))
    print("Valid" if totalValidator(moves) else "Invalid")


solution()
