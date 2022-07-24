import copy
# 자연수 n이 충분히 작기때문에 완전탐색으로 해도될듯!
# 백트래킹? bfs??


def bt(depth):
    global answer
    if depth == len(nums)-1:
        if check(nums, operator) == 0:
            answer.append(copy.deepcopy(operator))
    else:
        for i in ['+', '-', ' ']:
            operator.append(i)
            bt(depth+1)
            operator.pop()


def check(nums, operator):
    new = []
    new_operator = []
    num_i = 0
    oper_i = 0
    for i in range(len(operator)+len(nums)):
        if i % 2 == 0:
            new.append(str(nums[num_i]))
            num_i += 1
        else:
            if operator[oper_i] != ' ':
                new.append(";")
                new_operator.append(operator[oper_i])
                oper_i += 1
            else:
                oper_i += 1

    string = ''.join(new)

    str_list = list(map(int, string.split(";")))

    result = str_list[0]
    for i in range(len(new_operator)):
        if new_operator[i] == '+':
            result += str_list[i+1]
        else:
            result -= str_list[i+1]
    return result


if __name__ == '__main__':
    for i in range(int(input())):
        nums = [i+1 for i in range(int(input()))]
        operator = []
        answer = []
        bt(0)
        answer.sort()

        for i in range(len(answer)):
            for j in range(len(answer[i])):
                print(nums[j], end='')
                print(answer[i][j], end='')
            print(nums[-1])
        print()
