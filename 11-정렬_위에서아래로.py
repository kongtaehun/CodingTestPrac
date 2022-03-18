# 퀵정렬, 계수정렬이용할 예정
a = int(input())
n = []
for i in range(a):
    n.append(int(input()))

# 1. 퀵정렬
# 파이썬 형태로 표현할 것이며


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lis = arr[1:]
    left = [x for x in lis if x <= pivot]
    right = [x for x in lis if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


new = list(reversed(quicksort(n)))
for i in range(len(n)):
    print(new[i], end=' ')


# 2. 계수 정렬


def constsort(arr):
    count = [0 for i in range(max(arr)+1)]
    for i in range(len(arr)):
        count[arr[i]] += 1
    return count


new_n = constsort(n)
result = []
for i in range(len(new_n)):
    for j in range(new_n[i]):
        result.append(i)


# 3. 라이브러리 이용
new_n = sorted(n, reverse=True)
print(new_n)
