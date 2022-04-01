a = input()
b = []
sum = 0
for i in range(len(a)):
    if ord(a[i]) >= 65:
        b.append(a[i])
    else:
        sum = sum+int(a[i])
b.sort()
string = ''.join(b)
string = string + str(sum)
print(string)
