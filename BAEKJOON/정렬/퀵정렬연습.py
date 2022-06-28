array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quiksort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:

        while left <= end and array[pivot] < array[left]:
            left += 1
        while right > start and array[pivot] > array[right]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quiksort(array, start, right-1)
    quiksort(array, right+1, end)


quiksort(array, 0, len(array)-1)
print(array)
