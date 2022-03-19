n, target = map(int, input().split())
lis = list(map(int, input().split()))


# 이진탐색 - 재귀함수를 이용한다.
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)


idx = binary_search(lis, target, 0, n-1)
print(idx)


# 반복문으로 구현
start = 0
end = n-1
while start <= end:
    mid = (start+end)//2
    if target == lis[mid]:
        break
    elif target > lis[mid]:
        start = mid+1
    elif target < lis[mid]:
        end = mid-1

print(mid)
