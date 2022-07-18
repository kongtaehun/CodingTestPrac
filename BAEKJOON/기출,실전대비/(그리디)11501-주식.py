
import sys
input = sys.stdin.readline


for i in range(int(input())):
    total = 0
    n = int(input())
    nums = list(map(int, input().split()))
    # 뒤에서 부터 검사하는 것이 힌트다.
    mx = nums[-1]
    for j in range(n-2, -1, -1):
        if nums[j] > mx:
            mx = nums[j]
        else:
            total += mx - nums[j]
    print(total)

