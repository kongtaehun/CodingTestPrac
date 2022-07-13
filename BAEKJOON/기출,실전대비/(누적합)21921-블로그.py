
import sys
input = sys.stdin.readline
n, x = map(int, input().split())
nums = [0]+list(map(int, input().split()))
sum_list = [0]*(n-x+1)
for i in range(1, n+1):
    nums[i] += nums[i-1]


count = 0
max_val = 0
for i in range(x, n+1):
    temp = nums[i] - nums[i-x]
    
    if temp > max_val:
        max_val = temp
        count = 1
    elif temp == max_val:
        count += 1
if max_val == 0:
    print("SAD")
else:
        
    print(max_val)
    print(count)
