# 남학생은 자신번호의 배수
# 여학생은 최대 대칭의 수 범위를 전부 다 반전(반전아니면 받은 수의 스위치만)


def forMan(switchs, num):
    for i in range(1, len(switchs)):
        if i % num == 0:
            switchs[i] = abs(switchs[i]-1)


def forWoman(switchs, num):
    switchs[num] = abs(switchs[num]-1)
    # 예외1
    if num <= 1 or num == len(switchs)-1:
        return

    l = num - 1
    r = num + 1
    while True:
        # 예외1

        if switchs[l] == switchs[r]:
            switchs[l] = abs(switchs[l]-1)
            switchs[r] = abs(switchs[r]-1)
            l -= 1
            r += 1
        else:
            break
        if l < 1 or r > len(switchs)-1:
            break


if __name__ == '__main__':
    switch_n = int(input())
    switchs = [-1]+list(map(int, input().split()))
    student_n = int(input())
    for i in range(student_n):
        sex, num = map(int, input().split())
        if sex == 1:
            forMan(switchs, num)
        else:
            forWoman(switchs, num)
    order = 1
    for i in switchs[1:]:
        print(i, end=' ')
        if order % 20 == 0:
            print()
        order += 1
    # 출력형식에 주의
