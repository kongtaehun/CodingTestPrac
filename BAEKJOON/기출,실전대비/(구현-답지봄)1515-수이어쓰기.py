strr = list(map(str, list(input())))
i = 0
while True:
    i += 1
    # 현재의 숫자
    num = str(i)
    # 현재의 숫자로 얼만큼 strr을 없앨수 있는지
    while len(num) > 0 and len(strr) > 0:
        if num[0] == strr[0]:
            strr = strr[1:]
        num = num[1:]

    if len(strr) == 0:
        break
print(i)
