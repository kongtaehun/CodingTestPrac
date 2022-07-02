import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
broken = []
for i in range(b):
    broken.append(int(input()))

broken.sort()
broken_diff = []
if broken[0] != 1:
    broken_diff.append(broken[0]-1)

for i in range(1, len(broken)):
    broken_diff.append(broken[i]-broken[i-1])
if broken[-1] != n:

    broken_diff.append(n-broken[-1])

result = int(1e9)
for i in range(len(broken_diff)):
    temp = 0
    count = 0
    for j in range(i, len(broken_diff)):
        temp += broken_diff[j]
        count += 1
        if temp >= k:
            result = min(result, count)
print(0 if result == int(1e9) else result-1)
