# 아이디어! : 거꾸로 완성된 문자에서 시작문자로 바꿀 수 있는지!

from collections import deque
import sys
input = sys.stdin.readline

flag = 0


def bt(T):
    global flag

    if len(T) == len(s):
        if T == s:
            flag = 1
        return

    # 첫글자가 라는 것은 뒤집기연산을 한것이다.
    if T[0] == 'B':
        T.pop(0)
        T.reverse()
        bt(T)
        T.append('B')
        T.reverse()

    # 마지막글자가 A라는 것은 A추가연한을 한것이다.
    if T[-1] == 'A':
        T.pop()
        bt(T)
        T.append('A')


if __name__ == '__main__':
    s = input()
    s = list(s[:-1])
    t = input()
    t = list(t[:-1])
    bt(t)
    print(flag)
