# 1을 2로 바꾸는 비용 board[1][2]
REVERSE_COST = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
                [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
                [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
                [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
                [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
                [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
                [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
                [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
                [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
                [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
                ]


def roadReverseNumbers(n, k, x):
    # k자리 수에 맞는 수(1은 01로 표현)
    numbers = []
    for i in range(1, n+1):
        temp = list(map(int, list(str(i))))
        if len(temp) < k:
            temp2 = [0]*(k-len(temp))
            temp2 = temp2+temp
            numbers.append(temp2)
        else:
            numbers.append(temp)
    # 자기자신 삭제
    del numbers[x-1]
    return numbers


def isReversable(reverseNum, originNum, MaxCost):
    totalCost = 0
    for i in range(len(reverseNum)):
        totalCost += REVERSE_COST[reverseNum[i]][originNum[i]]
    if totalCost <= MaxCost:
        return True
    return False


# 1~n까지 p의 횟수로 변경이 가능한가?
if __name__ == '__main__':
    n, k, p, x = map(int, input().split())
    # 원래수를 자리수로 나눠진 리스트로 변환
    originNumber = list(map(int, list(str(x))))
    if len(originNumber) < k:
        temp2 = [0]*(k-len(originNumber))
        temp2 = temp2+originNumber
        originNumber = temp2
    # 바꾸기 가능한 수들을 불러옴
    reverseNumbers = roadReverseNumbers(n, k, x)

    answer = 0
    for reverseNum in reverseNumbers:
        if isReversable(reverseNum, originNumber, p):
            answer += 1

    print(answer)
