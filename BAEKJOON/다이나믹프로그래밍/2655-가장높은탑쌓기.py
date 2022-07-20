# 냅색알고리즘???
# 증가하는 수열??


# 1. 밑면넓이기준으로 역순 정렬
# 2. 무게를 기준으로 순회하며 나보다 앞에있는 것들을 다시탐색
# 3. 나보다 앞에있으면서 큰값중에 dp값의 MAX와 자신의 합을 자신의 dp
# 4. 이때 dp값이 더해지면 dp_idx에 참여한 벽돌들의 번호가 추가됨


n = int(input())  # 벽돌의 개수
bricks = [list(map(int, input().split()))+[i]
          for i in range(n)]  # 밑면,높이, 무게, 인덱스
bricks.sort(reverse=True)


# dp : i번째까지 벽돌에서 쌓을수있는 경우의 수에서 높이 최대값
dp = [0]*(n)
dp[0] = bricks[0][1]
# dp : i에서 참여한 벽돌의 인덱스들
dp_idx = [[] for i in range(n)]


for i in range(n):
    # 나보다 앞에 있는 것들 중에서 나보다 높이가 큰값의 max와 자신의 합 취함
    max_val = 0
    max_idx = 0
    for j, elements in enumerate(bricks[:i]):
        # 자기자신보다 높이가 클경우
        if elements[2] > bricks[i][2]:
            if max_val < dp[j]:
                max_val = dp[j]
                max_idx = j

    # 자신보다 큰값이 없으면 자기자신으로 초기화
    if max_val == 0:
        dp[i] = bricks[i][1]
        dp_idx[i].append(bricks[i][3])
    # 자신보다 큰 값이 있으면
    else:
        # 자기자신+앞의 벽들들 중 높이가 큰거중에 최대값과 자기자신의 높이를 더함
        dp[i] = max_val+bricks[i][1]
        # 그때의 dp_idx들과 자기자신의 인덱스를 합쳐서 저장
        dp_idx[i] += dp_idx[max_idx] + [bricks[i][3]]

# dp값의 최댓값이 높이의 최댓값임
# 높이가 최대일 때 참여한 벽돌들의 번호들을 찾음
result = dp_idx[dp.index(max(dp))]
print(len(result))
for i in reversed(dp_idx[dp.index(max(dp))]):
    print(i+1)
