# ============config============
import sys
input = sys.stdin.readline
# ============method============


def getAllLen(val, reserved):
    count = 0
    for i in reserved:
        count += i//val
    return count


def binarySearch(target, start, end, reserved):
    # print("==============")
    while start <= end:
        mid = (start+end)//2
        # print("mid : ", mid)

        check = getAllLen(mid, reserved)
        # print("check : ", check)
        if check < target:
            end = mid - 1
        else:
            start = mid + 1
    # print("==============")
    return start


# ============input=============
k, n = map(int, input().split())
reserved = []
for i in range(k):
    reserved.append(int(input()))
# ============main==============
start, end = 1, max(reserved)
val = binarySearch(n, start, end, reserved)

print(val)
