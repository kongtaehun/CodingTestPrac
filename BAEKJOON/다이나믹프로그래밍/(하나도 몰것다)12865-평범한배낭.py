# 백트래킹, 조합 시간초과 실패
# DP 답지봄
if __name__ == '__main__':

    n, k = map(int, input().split())
    meterial = [[0, 0]]+[list(map(int, input().split())) for i in range(n)]
    dp = [[0]*(k+1) for i in range(n+1)]

    for i in range(1, n+1):
        # 배낭의 무게별 탐색(배낭의 무게가 1일떄부터 k일때까지)
        for bag_weight in range(1, k+1):
            weight = meterial[i][0]
            value = meterial[i][1]

            # 현재 물건은 담지않고 전의 물건의 같은 가방무게일 때의 값을 가져옴
            if weight > bag_weight:
                dp[i][bag_weight] = dp[i-1][bag_weight]
            # 가방에 무게를 넣을 수 있다면
            else:
                # 전물체의 무게, 같은 가방무게일 때의 가치 or 전물체의 (가방무게 - 현재물건무게)일 때 가치아 현재물건가치의 합
                #
                dp[i][bag_weight] = max(
                    dp[i-1][bag_weight], dp[i-1][bag_weight-weight]+value)
    print(dp[n][k])
