import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = [0]+list(map(int, input().split()))
sumList = [0]*(n+1)
sumList[1] = nums[1]
maxVal = -int(1e9)
for i in range(2, n+1):
    sumList[i] = sumList[i-1]+nums[i]


for i in range(1, n-k+2):
    temp = sumList[i+k-1] - sumList[i-1]
    maxVal = max(maxVal, temp)


print(maxVal)
