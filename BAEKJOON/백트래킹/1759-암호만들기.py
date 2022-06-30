LOW = ['a', 'e', 'i', 'o', 'u']


def printArr(lists):
    # 모음수
    low_count = 0
    for i in LOW:
        if i in lists:
            low_count += 1
    # 자음수
    upper_count = len(lists) - low_count
    if low_count > 0 and upper_count > 1:
        print(''.join(lists))


def bt(depth, start):
    if depth == l:
        printArr(result)
    else:
        for i in range(start, c):
            if visited[i] == 0:
                visited[i] = 1
                result[depth] = chars[i]
                bt(depth+1, i)
                visited[i] = 0
                result[depth] = 0


if __name__ == '__main__':
    l, c = map(int, input().split())
    chars = list(map(str, input().split()))
    visited = [0]*(c)
    result = [0]*l
    chars.sort()
    bt(0, 0)
