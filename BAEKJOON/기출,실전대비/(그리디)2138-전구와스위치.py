# 완전탐색실패
import sys
from collections import deque
import copy
input = sys.stdin.readline


def flip(a, i):
    a[i-1] = abs(a[i-1]-1)
    a[i] = abs(a[i]-1)

    if i != n-1:
        a[i+1] = abs(a[i+1]-1)


def greedy(a):
    temp = copy.deepcopy(a)
    cnt = 0
    for i in range(1, n):
        if a[i-1] != b[i-1]:
            cnt += 1
            flip(a, i)

    if a == b:
        return cnt

    else:
        cnt = 1
        temp[0] = abs(temp[0]-1)
        temp[1] = abs(temp[1]-1)
        for i in range(1, n):
            if temp[i-1] != b[i-1]:
                cnt += 1
                flip(temp, i)

        if temp == b:
            return cnt
    return -1


def bfs(visited, a, b):
    q = deque()
    visited.add(''.join(list(map(str, a))))
    q.append((''.join(list(map(str, a))), 0))
    while q:
        now, step = q.popleft()

        if now == b:

            return step
        now = list(map(int, now))
        for i in range(n):
            now_copy = copy.deepcopy(now)
            if i != n-1:
                now_copy[i+1] = abs(now[i+1]-1)
            now_copy[i] = abs(now[i]-1)
            if i != 0:
                now_copy[i-1] = abs(now[i-1]-1)
            temp = ''.join(list(map(str, now_copy)))

            if temp not in visited:
                visited.add(temp)
                q.append((temp, step+1))

    return -1


if __name__ == '__main__':
    n = int(input().rstrip())
    a = list(map(int, list(input().rstrip())))
    b = list(map(int, list(input().rstrip())))
    visited = set()

    print(greedy(a))
