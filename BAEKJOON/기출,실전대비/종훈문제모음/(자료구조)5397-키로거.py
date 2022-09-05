from collections import deque
if __name__ == '__main__':
    for i in range(int(input())):
        left = deque()
        right = deque()
        codes = list(input())
        for code in codes:
            if code == '<':
                if left:
                    right.appendleft(left.pop())
            elif code == '>':
                if right:
                    left.append(right.popleft())
            elif code == '-':
                if left:
                    left.pop()
            else:
                left.append(code)
        print(''.join(list(left)+list(right)))
