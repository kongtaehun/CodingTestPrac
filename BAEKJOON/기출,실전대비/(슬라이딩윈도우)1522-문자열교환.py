
a = list(input())
# 1. a,b를 1과0으로
a_count = 0
for i in range(len(a)):
    if a[i] == 'a':
        a_count += 1
# a의 크기 size만큼의 윈도우 안에 b의 개수가 최소가 되는 값
result = int(1e9)
for i in range(len(a)):
    # 윈도우 내의 b의 개수 확인
    b_count = 0
    for i in a[0:a_count]:
        if i == 'b':
            b_count += 1
    result = min(result, b_count)

    # 리스트 회전
    a.append(a.pop(0))

print(result)
