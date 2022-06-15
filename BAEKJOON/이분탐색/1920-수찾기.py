# ============config================
import sys
input = sys.stdin.readline
# ============method================


def binary_search(target, start, end, num):
    while True:
        if start > end:
            return 0
        mid = (start+end)//2
        if target == num[mid]:
            return 1
        if target > num[mid]:
            start = mid+1
        else:
            end = mid-1


# ============input================
n = int(input())
num = list(map(int, input().split()))
m = int(input())
answersNum = list(map(int, input().split()))

# ============main================
num.sort()
result = []
for i in answersNum:
    start = 0
    end = len(num)-1
    target = i
    result.append(binary_search(target, start, end, num))

for i in result:
    print(result)
