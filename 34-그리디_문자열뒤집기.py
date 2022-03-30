a = input()
#내 방법
# 2중반복문으로 하나하나 연속된 원소들을 카운트한다.
# 2중 반복문이 비효율적이다
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


#정답
#0에서 1로  바뀔때 카운트,
#1에서 0으로 바뀔때 카운트
data = input()
count0 = 0
count1 = 0

if data[0] =='1':
    count1 +=1
else:
    count0+=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count1 +=1
        else:
            count0+=1
