from collections import deque
import sys
input = sys.stdin.readline
# deque를 이용한 슬라이딩 윈도우 같은디?
# 핵심2 : 윈도우의 크기만큼 길이 늘려서 계싼!!!


def two_pointer(sushi, c):
    count = [0]*(d+1)
    answer = 0

    for i in sushi[:k]:
        count[i] += 1
        if count[i] == 1:
            answer += 1

    count[c] += 1
    if count[c] == 1:
        answer += 1

    reresult = answer
    lis = deque(sushi[:k])
    for i in range(k, len(sushi)):

        lis.append(sushi[i])
        count[sushi[i]] += 1
        if count[sushi[i]] == 1:
            answer += 1
        pop_idx = lis.popleft()
        count[pop_idx] -= 1
        if count[pop_idx] == 0:
            answer -= 1
        reresult = max(reresult, answer)
    return reresult


if __name__ == '__main__':
    n, d, k, c = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(int(input()))
    sushi = sushi+sushi[:k+1]
    print(two_pointer(sushi, c))
