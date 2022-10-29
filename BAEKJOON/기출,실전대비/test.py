arr = [1, 3, 5, 2, 1]

for i in range(len(arr)-1):  # i번째 자리의 값을 찾는다.
    min_idx = arr[i+1:].index(min(arr[i+1:])) + i
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
