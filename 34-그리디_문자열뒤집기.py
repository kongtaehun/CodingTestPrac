a = input()

# 0으로 맞추는 경우와 1로 맞추는 경우 나눠서


# 0그룹
group_zero = 0
group_one = 0

i = 0
while i < len(a):
    while a[i] == '0':
        i = i+1
        if i >= len(a):
            break
    group_zero += 1
    if i >= len(a):
        break
    while a[i] == '1':
        i = i+1
    group_one += 1
    if i >= len(a):
        break

print(group_zero if group_zero < group_one else group_one)
