from collections import deque


def toString(stk):
    strr = ''
    for i in stk:
        strr += i
    return strr


def solution(number, k):

    stk = deque()
    for i in number:
        # stk검사(마지막 수와 비교하기)
        while k > 0 and len(stk) > 0 and stk[-1] < i:
            stk.pop()
            k -= 1
        stk.append(i)
    if k >= 1:
        strr = toString(stk)
        strr = strr[:-k]
        return strr

    return toString(stk)
