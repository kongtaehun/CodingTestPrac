from itertools import combinations
n, m = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] != a[j]:
            count += 1

print(count)


# 모범답안
n, m = map(int, input().split())
a = list(map(int, input().split()))
# 0부터 10까지 무게를 담을 수 있는 리스트
arr = [0] * 11

#각 무게에 해당하는 볼링공 개수
for i in a:
    arr[i] += 1

# 무게가 1일때부터 m일떄까지 선택할 수 있는 경우의 수 세기
# 무게가 i일때 선택할 수 있는 경우의 수
result = 0
for i in range(1, m+1):
    # 현재 A가 무게 i를 선택할 수 있는 경우의 수를 빼고 곱한다.
    #전체 공의 개수에서A가 선택한 경우의 수 빼고 곱함
    n = n-arr[i]
    #남은 공과 A가 선택한 공의 곱이 경우의수
    result += arr[i]*(n)
print(result)


#

a = [1, 3, 2, 3, 2]
b = list(combinations(a, 2))
result = []
for i in range(len(b)):
    if b[i][0] != b[i][1]:
        result.append(b[i])
print(len(result))
