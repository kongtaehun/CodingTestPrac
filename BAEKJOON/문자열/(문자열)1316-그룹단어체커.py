def check(str):
    temp = set()
    temp.add(str[0])
    for i in range(1, len(str)):

        if str[i-1] == str[i]:
            continue
        elif str[i] in temp:
            return 0

        temp.add(str[i])
    return 1


if __name__ == '__main__':
    result = 0
    for i in range(int(input())):
        str = input()
        result += check(str)
    print(result)
