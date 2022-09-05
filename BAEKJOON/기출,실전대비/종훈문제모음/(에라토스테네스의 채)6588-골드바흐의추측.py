def getPrimes(n):
    a = [False, False]+[True]*(n-1)  # 0과 1은 소수가 아니다!
    for i in range(2, n+1):
        if a[i]:
            for j in range(2*i, n+1, i):  # i의 두배부터 n+1까지 i씩 늘어나면서
                a[j] = False
    return a


# 미리구해놓기
primes = getPrimes(1000000)
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, len(primes)):
        # i와 n-i가 소수일 경우 정답출력하고 break
        if primes[i] and primes[n-i]:
            print(str(n) + ' = '+str(i)+' + '+str(n-i))
            break
