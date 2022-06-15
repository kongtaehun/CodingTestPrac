# key -> 각 공유기들 간의 간격이
# 동일하면 동일할수록 넓게 퍼지는 것
# 기준 -> 간격!
# 판단기준 -> 공유기 설치개수


# =========method============
def setRouter(house, val):
    count = 1
    now = house[0]
    for i in range(1, len(house)):
        if house[i]-now >= val:
            count += 1
            now = house[i]
    return count


# =========config============
n, m = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))


house.sort()
start = 1
end = house[-1]-house[0]  # 최대 간격
target = m
result = 0
while start <= end:
    mid = (start+end)//2
    check = setRouter(house, mid)

    if check < target:
        end = mid-1
    else:
        start = mid+1
        result = mid
print(result)
