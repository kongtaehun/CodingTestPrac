# 입력
n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    # 스테이지별 실패율
    fail_rate_list = []

    현재인원 = len(stages)
    for i in range(N):
        도전count = stages.count(i+1)
        if 도전count == 0:
            fail = 0
        else:
            fail = 도전count/현재인원

        fail_rate_list.append([fail, i+1])
        현재인원 = 현재인원 - 도전count

    fail_rate_list.sort(key=lambda x: (-x[0], x[1]))
    answer = [i[1] for i in fail_rate_list]

    return answer


# 입력
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
