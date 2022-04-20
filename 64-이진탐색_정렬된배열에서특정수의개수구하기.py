import bisect

n = 7
x = 2
list = [1, 1, 2, 2, 2, 2, 3]

a = bisect.bisect_left(list, 2)  # 2
b = bisect.bisect_right(list, 2)  # 6
result = b-a
if result == 0:
    print(-1)
else:
    print(result)
