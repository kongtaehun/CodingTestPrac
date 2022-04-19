# 나는 처음에 완전탐색을 생각했지만 이건 중간값!!!
n = 4
list = [5, 1, 7, 9]
result = 1e9
idx = 1e9
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(list[i] - list[j])
    if sum < result:
        result = sum
        idx = i
    elif sum == result:
        idx = min(i, idx)

print(idx)

# 중간값!
n = 4
list = [5, 1, 7, 9]
max = max(list)
min = min(list)
mid = max-min+1
# 중간값과 가장 가까운 값
idx = 0
result = 1e9
for i in range(4):
    check = list[i]-mid
    if check < result:
        idx = i
    elif check == result:
        idx = min(idx, i)

print(idx)


# 더 효율적으로 중간값을 출력
#
n = 4
list = [5, 1, 7, 9]
list.sort
list[(n-1)//2]
