# N M K - 중복가능
# N : 자연수의 개수
# M : 최댓값을 더할 개수
# k : 연속 몇번까지만 더할지
a = list(map(int, input().split()))
lis = list(map(int, input().split()))


maxx = max(lis)
# 리스트안에서 해당값을 갖는 하나를 지워줌
lis.remove(maxx)
maxx2 = max(lis)

# 최댓값더하기가 몇번 반복되는지
count_roop = a[1]//(a[2]+1)
count_mod = a[1] % (a[2]+1)

sum = count_roop*(a[2]*maxx+maxx2)+count_mod*maxx
print(sum)
# ---------------------------------------------
# 아래처럼 데이터받을 수도 ㅣㅆ다/
n, m, k = map(int, input().split())
lis = list(map(int, input().split()))

# 아래와 같이 최댓값 그 다음 최댓값구할 수 있다.
lis.sort(reverse=True)
maxx = lis[0]
maxx2 = lis[1]


# 아래와 같이도 구현 가능
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result = result + maxx
        m = m-1
    if m == 0:
        break
    result += maxx2
    m -= 1
