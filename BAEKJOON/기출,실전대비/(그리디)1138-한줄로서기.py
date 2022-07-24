# 앞에 개수만큼 +
n = int(input())
result = [0]*(n)
nums = list(map(int, input().split()))
for i in range(n):
    # 0의 개수를 기준으로 ㄱ!
    zero_cnt = 0
    for j in range(n):
        if zero_cnt == nums[i] and result[j] == 0:
            result[j] = i+1
            break
        if result[j] == 0:
            zero_cnt += 1

for i in result:
    print(i, end=' ')
