# 주어진 동전으로 만들 수 없는 양의 정수금액의 최솟값
n = int(input())
a = list(map(int, input().split()))
a.sort()

target = 1
for i in a:
    if target <= i:
        break
    target += i
print(target)
