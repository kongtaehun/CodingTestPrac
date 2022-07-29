import math
w, h, n, m = map(int, input().split())
print((math.ceil(w/(n+1)))*(math.ceil(h/(m+1))))
