from itertools import permutations
n = 3
num = [3, 4, 5]
cal = [1, 0, 1, 0]

new_cal = []
for i in range(4):
    for j in range(cal[i]):
        new_cal.append(i)

all_case_cal = list(permutations(new_cal, n-1))


min_result = -1e9
max_result = +1e9

# 두개의값과 연산종류 --> 연산


def calculate(a, b, cal_type):
    if cal_type == 0:
        return a+b
    elif cal_type == 1:
        return a-b
    elif cal_type == 2:
        return a*b
    else:
        if a < 0:
            return -(-a//b)
        else:
            return a//b


all_result = []
for i in all_case_cal:
    result = num[0]
    num_idx = 0
    cal_idx = 0
    while num_idx <= len(num)-2:
        result = calculate(result, num[num_idx+1], i[cal_idx])
        num_idx += 1
        cal_idx += 1
    all_result.append(result)

print(all_result)
