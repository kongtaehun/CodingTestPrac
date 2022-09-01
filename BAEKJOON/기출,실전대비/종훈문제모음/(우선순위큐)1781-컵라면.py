import heapq

if __name__ == '__main__':
    n = int(input())
    probs = []
    for i in range(n):
        dead, noodle = map(int, input().split())
        probs.append((dead, noodle))
    probs.sort(key=lambda x: (x[0], -x[1]))
    print(probs)
    # 현재 방문할 수 있는것중 가장 보상이 큰것을 방문하면 된다?
    solved_probs = []
    for dead, noodles in probs:
        # 푼 문제에 넣는다
        heapq.heappush(solved_probs, noodles)
        # 푼 문제가 dead보다 클경우(하나를 빼야한다.)
        # 가장 작은 문제를 뺀다.
        if len(solved_probs) > dead:
            heapq.heappop(solved_probs)
    print(sum(solved_probs))
