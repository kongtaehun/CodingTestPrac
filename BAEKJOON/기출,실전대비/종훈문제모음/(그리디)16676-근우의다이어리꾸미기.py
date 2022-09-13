# 같은 숫자가 포함되어있는 최대값 만큼 팩이 필요
# -> 일의 자리면 1팩 (0~10)
# -> 십의 자리면 2팩 (11~110)
# -> 백의 자리먄 3팩 (111~1110)
# -> 천의 자리면 4팩(1111~11110)

# 1. 자리수를 안다
n = input()
SIZE = len(n)
n = int(n)
# 2.기본적으로 자리수만큼이 필요
temp = ['1']*(SIZE)
if n == 0:
    print(1)
elif n < int(''.join(temp)):
    print(SIZE-1)
else:
    print(SIZE)
