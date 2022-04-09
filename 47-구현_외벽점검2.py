# 아이디어! : 2배로 늘린다.
from itertools import permutations
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]


def solution(n, weak, dist):
    temp = []

    # weak2배 늘리기
    for i in weak:
        temp.append(i+n)
    new_weak = weak + temp

    # 친구 순서의 모든 조합
    all_case_dist = list(permutations(dist, len(dist)))
    answer = len(dist)+1

    for start in range(len(weak)):
        for dis in all_case_dist:
            # 친구가 점검할 수 있는 위치
            count = 1
            end = new_weak[start]+dis[count-1]
            # 기준시작지점부터 취약점개수만큼의 크기만큼 확인

            for i in range(start, start+len(weak)):
                # 현재친구가 다음 취약점까지 도달할 수 없다면
                if end < new_weak[i]:
                    count += 1  # 다음취약점부터는 친구투입
                    if count > len(dis):
                        break  # 현재시작취약점에서는 확인 못함
                    # 다음친구가 점검할수있는 길이
                    end = new_weak[i]+dis[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer


print(solution(n, weak, dist))
