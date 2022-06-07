def solution(clothes):
    type = [y for x,y in clothes]
    count = [type.count(y) for y in set(type)] #중복제거
    answer = 1
    for i in count:
        answer *= i+1
    return answer-1