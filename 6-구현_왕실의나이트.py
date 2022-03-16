# 값 입력하기
a = input()
# 입력된 값을 인덱스로 바꿔주기
x = int(a[1])-1
y = ord(a[0])-97
# 첫번째 이동하는 경우의 수에 대하여
# 최대 8개의 경우의 수
c = []
c.append([y+2, x-1])
c.append([y+2, x+1])
c.append([y-2, x-1])
c.append([y-2, x+1])
c.append([y+1, x+2])
c.append([y-1, x+2])
c.append([y+1, x-2])
c.append([y-1, x-2])

count = 0
for i in c:
    if (i[0] >= 0 and i[0] <= 7) and (i[1] >= 0 and i[1] <= 7):
        count = count+1
print(count)
