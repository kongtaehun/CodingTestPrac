import copy


def flip(a, i):
    global cnt
    if a[i-1] != b[i-1]:
        a[i-1] = abs(a[i-1]-1)
        a[i] = abs(a[i]-1)
        if len(a) > i+1:
            a[i+1] = abs(a[i+1]-1)
        cnt += 1


# 그리디 알고리즘으로
# 처음부터 맨앞의 전구만 신경쓰며 스위치를 누른다
# 2번쨰전구부터 끝까지했을 때 안됬을 경우 맨처음2개 누른상태로 다시 돌리기
n = int(input())
a = list(map(int, list(input())))
a_ = copy.deepcopy(a)
b = list(map(int, list(input())))
cnt = 0
for i in range(1, n):
    flip(a, i)
if a == b:
    print(cnt)
else:
    cnt = 1
    a_[0] = abs(a_[0]-1)
    a_[1] = abs(a_[1]-1)
    for i in range(1, n):
        flip(a_, i)
    if a_ == b:
        print(cnt)
    else:
        print(-1)
