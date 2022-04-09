# 아이디어! : 2배로 늘린다.
from itertools import permutations
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]


# 틀림! 친구의 조합을 고려하지 않음
# 틀림! 시간 초과
# 틀림! 모든 지점을 포함하는 리스트를 만들지 말고 weak의 숫자만 포함시켜 반복의 횟수 줄이기


def solution(n, weak, dist):
    # 2배리스트에 weak을 배치한다.(+12)
    board = [0 for i in range(2*n)]
    temp = []
    for i in weak:
        temp.append(i+n)
    new_weak = weak+temp
    for i in new_weak:
        board[i] = 1

    # 아이디어! : 하나의 취약점을 시작
        # 친구한명이 확인할때
        # 친구두명이 확인할때
        # 친구세명이 확인
        # 다음취약점도 같은방법으로
    new_dist = list(permutations(dist, len(dist)))

    result = []
    for distt in new_dist:
        print(distt)
        for i in range(len(new_weak)-len(distt)):
            check = []
            count = 0
            for d in distt:
                check.append(board[new_weak[i+count]:new_weak[i+count]+d+1])
                if sum(sum(check, [])) == len(weak):
                    result.append(len(check))
                count += 1

    if len(result) < 1:
        return -1
    print(result)
    answer = min(result)
    return answer


print(solution(n, weak, dist))
