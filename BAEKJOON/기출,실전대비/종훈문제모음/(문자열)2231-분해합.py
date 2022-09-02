n = int(input())
flag = 0
for i in range(1, n+1):
    result = i
    str_num = str(i)
    for j in str_num:
        result += int(j)

    if result == n:
        flag = 1
        print(i)
        break
if flag == 0:
    print(0)
