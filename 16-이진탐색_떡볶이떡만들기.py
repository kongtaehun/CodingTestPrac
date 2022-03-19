n, d = map(int, input().split())
lis = list(map(int, input().split()))

# 내방법으로 풀었을 때! --> 순차탐색
ex = max(lis)
while ex >= 0:
    temp_lis = []
    for i in lis:
        if i <= ex:
            temp_lis.append(0)
        else:
            temp_lis.append(i - ex)
    if sum(temp_lis) >= d:
        break
    else:
        ex = ex-1
print(ex)

# 이진탐색 풀이법
# 1. 자를 길이의 범위를 지정한다.
# 2. 처음, 끝, 중간값을 지졍하여 이진탐색한다
# 3. 탐색할 때마다 반복문을 돌리며 남은 떡의 길이를 계산한다.


# 절단기의 길이
ex = [x for x in range(max(lis)+1)]
start = 0
end = len(ex)-1
target = d
while start <= end:
    mid = (start+end)//2
    temp_lis = []
    for i in lis:
        if i <= mid:
            temp_lis.append(0)
        else:
            temp_lis.append(i - mid)
    if sum(temp_lis) == target:
        break
    elif sum(temp_lis) > target:
        start = mid+1
    elif sum(temp_lis) < target:
        end = mid-1
print(mid)
