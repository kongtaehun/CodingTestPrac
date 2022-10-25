# 조합으로 만들 수 없는 수
target = 1
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
for i in nums:
    if target < i:
        break
    else:
        target += i
print(target)
