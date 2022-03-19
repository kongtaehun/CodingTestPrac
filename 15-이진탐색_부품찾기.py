# 이진탐색
import sys
n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(arr, start, end, target):
    if start > end:
        return -1
    mid = (start+end)//2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, mid+1, end, target)
    elif target < arr[mid]:
        return binary_search(arr, start, mid-1, target)


n_list.sort()
for i in m_list:
    idx = binary_search(n_list, 0, n-1, i)
    if idx == -1:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 계수정렬
lis = [0 for x in range(max(n_list)+1)]
for i in n_list:
    lis[i] = 1
for i in m_list:
    if lis[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 집합이용
for i in m_list:
    if i in n_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')
