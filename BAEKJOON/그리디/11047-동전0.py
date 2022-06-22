n, k = map(int, input().split())
coinList = []
for i in range(n):
    coinList.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
    answer = k//coinList[i]
    retain = k % coinList[i]
    if answer >= 1:
        k = retain
        result += answer

print(result)
