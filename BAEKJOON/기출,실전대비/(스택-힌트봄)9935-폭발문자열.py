from collections import deque
import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    strr = input().rstrip()
    bumb = input().rstrip()

    idx = 0
    stk = []
    for i in range(len(bumb)):
        stk.append(strr[i])
        idx += 1

    while True:

        if idx == len(strr):
            break
        if ''.join(stk[-len(bumb):]) == bumb:
            for i in range(len(bumb)):
                stk.pop()
        stk.append(strr[idx])
        idx += 1
    if ''.join(stk[-len(bumb):]) == bumb:
        for i in range(len(bumb)):
            stk.pop()
    print("FRULA") if len(stk) == 0 else print(''.join(stk))
