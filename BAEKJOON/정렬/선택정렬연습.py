array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    minIdx = i
    for j in range(i, len(array)):
        if array[minIdx] > array[j]:
            minIdx = j
    array[i], array[minIdx] = array[minIdx], array[i]
print(array)
