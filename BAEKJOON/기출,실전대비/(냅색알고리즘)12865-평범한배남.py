
n, k = map(int, input().split())

# 1. 비용과 가치를 입력받는다
meterial = [[0, 0]]  # 0번째 인덱스에 값을 넣는다.
for i in range(n):
    meterial.append(list(map(int, input().split())))
meterial.sort()  # 정렬한다.

# 행 -> 물건의종류를 늘려감
# 열 -> 최대무게제한을 늘려감
dp = [[0]*(k+1) for i in range(n+1)]
for i in range(1, n+1):
    weight = meterial[i][0]
    value = meterial[i][1]
    for max_weight in range(1, k+1):
        # 최대무게보다 물건의 무게가 클 경우, 그물건만 없을 경우 같은 최대무게의 값을 가져옴
        if weight > max_weight:
            dp[i][max_weight] = dp[i-1][max_weight]
        else:
            dp[i][max_weight] = max(dp[i-1][max_weight-weight] +
                                    value, dp[i-1][max_weight])
print(dp[-1][-1])
