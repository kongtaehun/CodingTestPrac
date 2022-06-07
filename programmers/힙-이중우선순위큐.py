# Bisect를 사용하여 리스트에 값을 입력할 때마다 정렬되게 유지
# 리스트 하나에 대하여 list.pop(), list.pop(0) 로 최소,최대 pop 구현

from bisect import bisect_left, bisect_right
from collections import deque


def getMaxMin(heap):
    if len(heap) > 1:
        max = heap.pop()
        min = heap.popleft()
        return [max, min]
    elif len(heap) == 1:
        val = heap.pop()
        return [val, val]
    else:
        return [0, 0]


def solution(operations):
    #최대힙, 최소힙
    heap = deque()
    for i in operations:
        key, value = i.split(" ")
        value = int(value)
        if key == "I":
            heap.insert(bisect_left(heap, value), value)
        elif key == "D":
            if value == 1:
                if heap:
                    heap.pop()
            else:
                if heap:
                    heap.popleft()

    answer = getMaxMin(heap)

    return answer
