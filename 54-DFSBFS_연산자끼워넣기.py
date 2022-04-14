# DFS를 이용한 방법이 모범답안이다.
n = 3
num = [3, 4, 5]
cal = [1, 0, 1, 0]

min_value = 1e9
max_value = -1e9

# dfs정의


def dfs(i, now):  # 다음 인덱스 값, 현재 계산 누적값
    global min_value, max_value, cal
    if i == n:  # 다음 인덱스가 마지막일경우(재귀에서 i+1계산이 되고 재귀호출이기 떄문에 n-1이아닌 n이다.)
        min_value = min(min_value, now)  # 현재 계산한 값과 저장된 min_value중 낮은걸 할당
        max_value = max(max_value, now)  # 현재 계산한 값과 저장된 min_value중 낮은걸 할당
    else:
        if cal[0] > 0:
            cal[0] -= 1
            dfs(i+1, now+num[i])
            cal[0] += 1  # 다시 더해줘야 모든 경우의 수를 계산가능
        if cal[1] > 0:
            cal[1] -= 1
            dfs(i+1, now-num[i])
            cal[1] += 1  # 다시 더해줘야 모든 경우의 수를 계산가능
        if cal[2] > 0:
            cal[2] -= 1
            dfs(i+1, now*num[i])
            cal[2] += 1  # 다시 더해줘야 모든 경우의 수를 계산가능
        if cal[3] > 0:
            cal[3] -= 1
            dfs(i+1, now//num[i])
            cal[3] += 1  # 다시 더해줘야 모든 경우의 수를 계산가능


dfs(1, num[0])

print(max_value)
