from collections import deque
#순서대로 DP로 해결

if __name__ == '__main__':
    n = int(input())
    indegree = [0]*(n+1)
    graph = [[] for i in range(n+1)]
    cost = [0]*(n+1)
    results = []
    for i in range(1, n+1):
        temp = list(map(int, input().split()))
        cost[i] = temp[0]
        indegree[i] = temp[1]
        for j in range(2, len(temp)):
            graph[i].append(temp[j])

    #순서대로 해당과목을 듣는데 필요한 시간을 갱신해줌(Max)
    for i in range(1, n+1):
        time = 0
        for j in graph[i]:
            time = max(time, cost[j])
        cost[i] += time
    print(max(cost))
