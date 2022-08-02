# 끼워 맞추기(들어간 인덱스 기억하기)
# 1. 랭킹리스트가 꽉차있고 새점수 bisect가 0이면 -1
# 2. 랭킹리스트가 꽉차있고 새점수 bisect가 0이 아니면
#- now[:bisect] + new +now[bisect:]
# 등수 채점하기
from bisect import bisect_left


def grading(grades):
    grades.reverse()
    ranks = [0]*(len(grades))
    ranks[0] = 1
    now_rank = 2

    for i in range(1, len(grades)):
        if grades[i] == grades[i-1]:
            ranks[i] = ranks[i-1]
            now_rank += 1
        else:
            ranks[i] = now_rank
            now_rank += 1
    ranks.reverse()
    return ranks


n, new_grade, p = map(int, input().split())
if n != 0:
    now = list(map(int, input().split()))
    now.sort()
    new_idx = bisect_left(now, new_grade)
    if len(now) == p and new_idx == 0:
        print(-1)
    else:
        now = now[:new_idx] + [new_grade] + now[new_idx:]

        ranks = grading(now)
        # print(ranks)
        print(ranks[new_idx])
else:
    print(1)
