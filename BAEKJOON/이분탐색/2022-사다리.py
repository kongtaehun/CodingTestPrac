import math


def f(x, y, w):
    h1 = math.sqrt(y**2-w**2)
    h2 = math.sqrt(x**2-w**2)
    c = h1*h2/(h1+h2)
    return c


def binarySearch(start, end, target):
    while end-start > 0.000001:
        #mid = w
        mid = (start+end)/2
        c = f(x, y, mid)
        if c >= target:
            start = mid
        else:
            end = mid
    return start


x, y, c = map(float, input().split())
print(binarySearch(0, min(x, y), c))
