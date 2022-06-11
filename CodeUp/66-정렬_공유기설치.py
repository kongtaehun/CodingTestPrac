# 거리를 2진탐색한다.
# c개의 공유기를 설치가능한지
n = 5
c = 3
list = [1, 2, 8, 4, 9]
list.sort()
start = 1  # 최소갑차이
end = list[-1]-list[0]  # 최대 값차이
result = 0
while start <= end:
    mid = (start+end)//2

    count = 0
    value = list[0]
    # 공유기 설치해보기
    for i in range(1, n):
        # 만약, 전의 공유기 위치 + mid보다 크거나 같은 값이 있을경우
        # 공유기설치 (value는 전공유기의 거리)
        if list[i] >= value+mid:
            count += 1
            value = list[i]

    if count >= c:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)
