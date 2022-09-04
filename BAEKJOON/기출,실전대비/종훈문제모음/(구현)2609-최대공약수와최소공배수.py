a, b = map(int, input().split())
mx = max(a, b)
mn = min(a, b)
for i in range(mn, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
temp = mx
while True:
    if temp % mn == 0:
        print(temp)
        break
    temp += mx
