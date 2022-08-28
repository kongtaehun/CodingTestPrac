INF = int(1e9)


def bt(depth, before, START):
    global result, answer
    if depth == n-1:
        # 마지막에서 출발점 돌아오는 거도 길이 없을 수도 있음!
        if graph[before][START] == 0:
            return
        result += graph[before][START]
        answer = min(result, answer)
        result -= graph[before][START]
    else:
        for next in range(n):
            if visited[next] == 0 and graph[before][next] != 0:
                result += graph[before][next]
                visited[next] = 1
                bt(depth+1, next, START)
                result -= graph[before][next]
                visited[next] = 0


if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input().split()))for i in range(n)]
    # 백트래킹(경우의수)
    result = 0
    answer = INF
    for i in range(n):
        visited = [0]*(n)
        visited[i] = 1
        bt(0, i, i)
    print(answer)
