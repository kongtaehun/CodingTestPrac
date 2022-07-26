# 문자열구현

# = -> 전의 요소가 c,dz,s,z
# - -> 전의 요소가 c,d
# j -> 전의 요소가 l,n인지


string = input()
result = len(string)
i = 0
while i < len(string):

    if string[i] == '=':
        if i > 1 and string[i-1] == 'z' and string[i-2] == 'd':
            result -= 2
        elif string[i-1] == 'c' or string[i-1] == 's' or string[i-1] == 'z':
            result -= 1

    elif string[i] == 'j':
        if string[i-1] == 'l' or string[i-1] == 'n':
            result -= 1

    elif string[i] == '-':
        if string[i-1] == 'c' or string[i-1] == 'd':
            result -= 1

    i += 1


print(result)
