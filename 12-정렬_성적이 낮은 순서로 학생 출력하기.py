a = int(input())
student = []
for i in range(a):
    x, y = input().split()
    student.append([x, int(y)])

#
for i in range(len(student)):
    min_idx = i
    for k in range(i+1, len(student)):
        if student[min_idx][1] > student[k][1]:
            min_idx = k
    student[i], student[min_idx] = student[min_idx], student[i]
print(student)

for i in range(len(student)):
    print(student[i][0], end=' ')
