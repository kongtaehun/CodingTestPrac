def reverseStr(str):
    str.reverse()
    return ''.join(str)


def tagStart(str, idx):

    end_idx = 0
    for i in range(idx+1, len(str)):
        if str[i] == '>':
            end_idx = i
            break
    return str[idx:end_idx+1], end_idx+1


if __name__ == '__main__':
    a = input()
    result = []
    str_stk = []
    now = 0
    while now < len(a):
        # print(now)
        if a[now] == '<':
            if str_stk:
                result.append(reverseStr(str_stk))
                str_stk = []
            tag_str, now = tagStart(a, now)
            result.append(tag_str)
        elif a[now] == ' ':
            result.append(reverseStr(str_stk))
            str_stk = []
            now += 1
        else:
            str_stk.append(a[now])
            now += 1
    if str_stk:
        result.append(reverseStr(str_stk))

    print(result[0], end='')
    for i in range(1, len(result)):
        if result[i-1][-1] == '>':
            print(result[i], end='')
        else:
            if result[i][0] == '<':
                print(result[i], end='')
            else:
                print(' '+str(result[i]), end='')
