a, b, c = map(int, input().split())


def dc(a, b, c):
    # 나누는 횟수가 1일때
    if b == 1:
        return a % c
    # 짝수일 떄
    elif b % 2 == 0:
        return (dc(a, b//2, c)**2) % c
    else:
        return (dc(a, b//2, c)**2)*a % c


print(dc(a, b, c))
