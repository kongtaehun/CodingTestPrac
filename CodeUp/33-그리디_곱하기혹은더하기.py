import plistlib


a = input()
result = int(a[0])
for i in range(1, len(a)):
    plus = result+int(a[i])
    multi = result*int(a[i])
    if plus > multi:
        result = plus
    else:
        result = multi
print(result)
