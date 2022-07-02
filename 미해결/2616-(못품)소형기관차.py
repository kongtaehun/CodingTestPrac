
# 크기가 s인 부분수열의 합중에 최대가 되는 합
n = int(input())
nums = [0] + list(map(int, input().split()))
s = int(input())

sum_list = []
summ = 0
for i in range(len(nums)):
    summ += nums[i]
    sum_list.append(summ)

print(sum_list)

dp = [[0]*(n+1) for i in range(3)]
