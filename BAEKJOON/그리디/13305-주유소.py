n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost = cost[:-1]
min_idx = n-1
result = 0
while min_idx != 0:
    min_cost = min(cost)
    min_idx = cost.index(min_cost)
    result += min_cost*sum(distance[min_idx:])
    distance = distance[:min_idx]
    cost = cost[:min_idx]
    print(result)
