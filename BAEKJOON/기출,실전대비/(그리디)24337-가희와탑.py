# 사이에 넣는 예외가 존재
# 예외 :
# 입력 - 5 1 3
# 정답 - 3 1 1 2 1


n, g, d = map(int, input().split())
if d > g:
    temp = [i for i in range(d, 0, -1)]
    temp2 = [i for i in range(1, g)]
    temp = temp2 + temp

else:
    temp = [i for i in range(1, g+1)]
    temp2 = [i for i in range(d-1, 0, -1)]
    temp = temp+temp2


fail_flag = 0
# 1의 위치가 양쪽이면 왼쪽에 글자수 맞게 1을 붙힘
if temp[0] == temp[-1] == 1 or temp[0] == 1:
    if (n-len(temp)) < 0:
        fail_flag = 1
    one_temp = [1]*(n-len(temp))
    temp = one_temp+temp
# 오른쪽만 1이면 => 두번째에 1삽입
elif temp[-1] == 1:
    if (n-len(temp)) < 0:
        fail_flag = 1
    one_temp = [1]*(n-len(temp))
    temp = [temp[0]]+one_temp+temp[1:]

if fail_flag == 1:
    print(-1)
else:
    for i in temp:
        print(i, end=' ')
