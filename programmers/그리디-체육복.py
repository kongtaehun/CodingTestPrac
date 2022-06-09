# 수업에 참여 가능한 인원 Count
def classCount(reserveList):
    count = 0
    for i in reserveList:
        if i >= 1:
            count += 1
    return count


# 체육복 빌려주기
def rent(n, reservedList):
    for i in range(n):
        if reservedList[i] == 2:

            if i > 0 and reservedList[i-1] == 0:
                reservedList[i-1] += 1
                reservedList[i] -= 1
            elif i < n-1 and reservedList[i+1] == 0:
                reservedList[i+1] += 1
                reservedList[i] -= 1
    return reservedList


def solution(n, lost, reserve):
    # 전체 학생이 가지고 있는 체육복 리스트
    reserveList = [1 for i in range(n)]
    for i in reserve:
        reserveList[i-1] += 1
    for i in lost:
        reserveList[i-1] -= 1

    reserveList = rent(n, reserveList)
    print(reserveList)
    answer = classCount(reserveList)

    return answer
