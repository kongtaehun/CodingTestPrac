# 없는 부분 완전 제외가능?

# target없이 진행한다
def binary_search(start, end, array):
    if start > end:
        return None
    mid = (end+start)//2
    # target은 중앙 인덱스
    target = mid
    # target이 array[mid]보다 크면
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(mid+1, end, array)
    else:
        return binary_search(start, mid-1, array)


result = binary_search(0, 7-1, [-15, -4, 3, 8, 9, 13, 15])
if result is None:
    print(-1)
else:
    print(result)
