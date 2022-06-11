
# 균형잡힌 문자열 분리
def split_proper(idx):
    count = 0
    for i in range(len(str)):
        if str[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
    return 0

# 균형잡힌 문자열 분리


def check_proper(idx):
    count = 0
    for i in range(len(str)):
        if str[i] == '(':
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    else:
        return False


# 올바른 문자열 판단함수
def check_right(str):
    if str[0] == '(':
        check_count = 1
    elif str == "":
        return True
    else:
        return False
    for i in range(1, len(str)):

        if str[i] == '(':
            check_count += 1
        else:
            check_count -= 1
    if check_count == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    # 빈문자열일경우 빈문자열 반환
    if p == answer:
        return p
    # 올바른괄호문자열일경우그대로 반환
    if check_proper(p):
        return p

    # 문자열 분리
    idx = split_proper(p)
    u = p[:idx+1]
    v = p[idx+1:]

    # u가 올바른 문자열이면
    if check_right(u):
        solution(v)
    else:
        result = "("
        result += solution(v)
        result += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        result += "".join(u)
        return result+u

    return answer
