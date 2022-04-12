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


#
n = 5
a = [3,2,1,1,9]

#아이디어! 직접조합해보면서 규칙찾기

a.sort()

sum = 0
result = 0
for i in range(len(a)-1):
    sum+=a[i]
    if sum<a[i+1]:
        result = sum+1
        break

if result ==0:
    print(a[len[a]-1]+1)
else: 
    print(result)