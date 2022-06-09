# 가장 높은 수와 낮은수부터 결합
# 투포인터 알고리즘 이용
# 구명 보트가 타는 인원이 2명으로 제한되어 있었다!!!!
def solution(people, limit):
    people.sort()
    l = 0  # 포인터 1(왼쪽)
    r = len(people)-1  # 포인터 2(오른쪽)
    answer = 0
    boat = 0
    while r >= l:
        # 보트하나추가
        answer += 1
        # 무거운사람 + 가벼운 사람 조합
        if people[r]+people[l] <= limit:
            l += 1
        r -= 1
    return answer
