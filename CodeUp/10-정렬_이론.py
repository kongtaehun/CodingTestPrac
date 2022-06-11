# 1~10무작위의 숫자를 오름차순으로 정렬하기ㅏ
# 선택정렬방법으로 정렬하기
from numpy import array


arr = [1, 8, 5, 6, 2, 4, 3, 7, 9, 10]
for i in range(len(arr)):
    # 가장 작은 값의 인덱스를 찾는다.
    min_idx = i
    # 앞에서 부터 n+1부터끝까지의 값중 최솟값과 자기자신을 바꾼다.
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    # temp = arr[i]
    # temp2 = arr[min_idx]
    # arr[i] = temp2
    # arr[min_idx] = temp
    # 스와프이용하기
    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr)


# ================================================
# 삽입정렬방법으로 정렬하기
arr = [8, 1, 5, 6, 2, 4, 3, 7, 9, 10]

for i in range(1, len(arr)):
    for k in range(i, 0, -1):
        if arr[k] > arr[k-1]:
            break
        else:
            arr[k], arr[k-1] = arr[k-1], arr[k]
print(arr)

# ================================================
# 퀵정렬 이용하기
# 첫번째 요소를 피봇으로 하기떄문에
#   왼쪽으로 가는것은 end부터 -1        --> 작은 것을 찾음
#   오른쪽으로 가는것 start+1 부터 +1   --> 큰 것을 찾음
#   left가 right보다 커졌얼 때 엇갈리 것
#       엇갈리면 오른쪽이 가장 작은 값임
#       엇갈리면 왼쪽, 오른쪽 부붙을 다시 정렬
#       arr의 크기가 1이면 종료


def quicksort(arr, start, end):
    # arr의 크기가 1이면 종료조건
    if end-start <= 0:
        return
    # 인덱스 정의
    pivot = start
    right = start+1
    left = end
    while (left >= right):

        # ---------------탐색------------------
        # 오른쪽으로 가는것 --> 오른쪽이 피봇보다 작을 때까지 이동
        while (right <= end and arr[pivot] >= arr[right]):
            right = right+1
        # 왼쪽으로 가는것 --> 왼쪽이 피봇보다 클때까지 이동
        while (left > start and arr[pivot] <= arr[left]):
            left = left-1
        # ---------------교체------------------
        # left, right 인덱스가 각각 피봇보다 작거나 커서 조건에 만족함
        # left가 right보다 작거나 같으면 엇갈린것이다 --> 피봇과 가장작은 것 교체
        if left < right:
            arr[left], arr[pivot] = arr[pivot], arr[left]
        # 안 엇갈렸을 경우 right와  left 교체
        else:
            arr[right], arr[left] = arr[left], arr[right]
            # 왼쪽부붙, 오른쪽부분에서 다시 실행
            # arr[right]가 이제 피봇이 있는 기준 요소가 됨
    quicksort(arr, start, left-1)  # 왼쪽
    quicksort(arr, left+1, end)  # 오른쪽


arr = [8, 1, 5, 6, 2, 4, 3, 7, 9, 10]
quicksort(arr, 0, len(arr)-1)
print(arr)
# ====================================================
# 파이썬의 장점을 살린 퀵정렬 소스


def quick_sort_py(arr):
    if len(arr) <= 1:
        return arr
    # 피봇을 첫번째 데이터로 선정
    pivot = arr[0]
    # 피봇을 제외한 나머지 데이터 배열
    tail = arr[1:]
    # 피벗보다 크기가 작거나 같으면 왼쪽, 크면 오른쪽 따로따로 리스트저장
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort_py(left)+[pivot]+quick_sort_py(right)


arr = [8, 1, 5, 6, 2, 4, 3, 7, 9, 10]
print(quick_sort_py(arr))
# ==================================================
# 계수정렬(내가 한거)


def const_sort(arr):
    maxx = max(arr)
    minn = min(arr)
    lis = []
    for i in range(minn, maxx+1):
        lis.append([i, arr.count(i)])
    return lis


arr = [8, 1, 1, 5, 6, 2, 4, 3, 7, 9, 10]
lis = const_sort(arr)
for i in range(len(lis)):
    print((str(lis[i][0])+' ')*lis[i][1], end=' ')
# ===================================================
# 정석 --> 숫자가 0부터 시작한다고 하는게 짜기 편함
count = [0]*(max(arr)+1)  # 값이 0이고 크기가 최댓값+1인 리스트
for i in range(len(arr)):
    count[arr[i]] = +1
# c출력하기
for i in range(len(arr)):
    for j in range(count[i]):
        print(i, end=' ')
