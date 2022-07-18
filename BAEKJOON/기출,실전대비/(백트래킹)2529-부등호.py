INF = int(1e10)


def bt(depth):
    global max_answer, min_answer, max_answer_str, min_answer_str
    if depth == n+1:
        temp = int(''.join(map(str, result)))
        if max_answer < temp:
            max_answer = temp
            max_answer_str = ''.join(map(str, result))
        if min_answer > temp:
            min_answer = temp
            min_answer_str = ''.join(map(str, result))

    else:
        for i in range(10):
            now_sign = arr[depth-1]
            if visited[i] == 0:
                if now_sign == '<' and i > result[depth-1]:
                    visited[i] = 1
                    result[depth] = i
                    bt(depth+1)
                    visited[i] = 0
                    result[depth] = 0
                if now_sign == '>' and i < result[depth-1]:
                    visited[i] = 1
                    result[depth] = i
                    bt(depth+1)
                    visited[i] = 0
                    result[depth] = 0


# 백트래킹 개삘
if __name__ == '__main__':
    n = int(input())
    result = [0]*(n+1)
    max_answer = -INF
    max_answer_str = ''
    min_answer = INF
    min_answer_str = ''
    visited = [0]*(10)
    arr = list(map(str, input().split()))
    for j in range(10):
        visited = [0]*(10)
        result[0] = j
        visited[j] = 1
        bt(1)
        result[0] = 0
        visited[j] = 0

    print(max_answer_str)
    print(min_answer_str)
