INF = int(1e9)
result = 0

n = int(input())
nums = list(map(int, input().split()))
#오른쪽으로, 왼쪽으로
for i in range(n):
    # 기울기가 커져야함
    now_m = -INF
    r_count = 0
    for r in range(i+1, n):
        m = (nums[r]-nums[i])/(r-i)
        if m <= now_m:
            continue
        else:
            now_m = m
            r_count += 1

    now_m = INF
    l_count = 0
    for l in range(i-1, -1, -1):
        m = (nums[l]-nums[i])/(l-i)
        if m >= now_m:
            continue
        else:
            now_m = m
            l_count += 1
    result = max(result, l_count+r_count)
print(result)
