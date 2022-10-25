# 모음하나
# 모음 or 자음 연속세개x

def solution(pw):
    moem = set(['a', 'e', 'i', 'o', 'u'])
    jaem = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
               'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    condition_1 = False
    condition_2 = True
    condition_3 = True
    for i in range(len(pw)):
        if pw[i] in moem:
            condition_1 = True

    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            if pw[i] == 'o' or pw[i] == 'e':
                continue
            else:
                condition_3 = False

    for i in range(len(pw)-2):
        if pw[i] in jaem and pw[i+1] in jaem and pw[i+2] in jaem:
            condition_2 = False
        if pw[i] in moem and pw[i+1] in moem and pw[i+2] in moem:
            condition_2 = False

    if condition_1 and condition_2 and condition_3:
        return 'is acceptable'
    else:
        return 'is not acceptable'


while True:
    pw = input()
    if pw == 'end':
        break
    print('<'+str(pw)+'>', end=' ')
    print(solution(pw), end='.')
    print()
