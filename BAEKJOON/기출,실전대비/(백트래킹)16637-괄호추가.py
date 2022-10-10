def bt(depth, start):
    global answer
    # print(visited)
    temp = convertStr(visited)
    answer = max(answer, temp)
    for i in range(start, n-2):
        if i % 2 == 0 and visited[i] == 0 and visited[i+1] == 0 and visited[i+2] == 0:
            visited[i] = 1
            visited[i+1] = 1
            visited[i+2] = 1
            bt(depth+1, i)
            visited[i] = 0
            visited[i+1] = 0
            visited[i+2] = 0


def convertStr(visited):
    # 괄호먼저 다 계산
    result = []
    i = 0
    while i < n:
        # print(visited)
        if i % 2 == 0 and i+2 < n and i+1 < n and visited[i] == 1 and visited[i+1] == 1 and visited[i+2] == 1:

            if strr[i+1] == '+':
                result.append(str(int(strr[i])+int(strr[i+2])))
            elif strr[i+1] == '-':
                result.append(str(int(strr[i])-int(strr[i+2])))
            elif strr[i+1] == '*':
                result.append(str(int(strr[i])*int(strr[i+2])))
            i += 3
        else:

            result.append(strr[i])
            i += 1

    return calculate(result)


def calculate(a):
    now = int(a[0])
    for i in range(1, len(a)):
        if i % 2 != 0:
            if a[i] == '*':
                now = now*int(a[i+1])
            elif a[i] == '-':
                now = now-int(a[i+1])
            elif a[i] == '+':
                now = now+int(a[i+1])
    return now


if __name__ == '__main__':
    # 괄호없을 때가 제일 최대일 가능성존재
    n = int(input())
    strr = input()
    answer = -int(1e9)
    # 괄호가 가능한 위치 - (0,1,2), (2,3,4), (4,5,6)
    visited = [0]*(n)
    result = []
    # n = 7
    # visited = [0, 0, 0, 0, 1, 1, 1]
    # strr = '8*3+5+2'
    # print(convertStr(visited))
    bt(0, 0)
    print(answer)
