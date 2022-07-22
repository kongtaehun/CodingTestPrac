n, k = map(int, input().split())
medals = [list(map(int, input().split())) for i in range(n)]
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank = [[0] for i in range(n)]

rank_val = 1
now_medal_idx = 0
rank[0] = 1
for i in range(1, n):
    if medals[now_medal_idx][1:] == medals[i][1:]:
        rank[i] = rank[now_medal_idx]
        rank_val += 1
    else:
        rank[i] = rank[now_medal_idx]+rank_val
        now_medal_idx = i
        rank_val = 1

for i in range(n):
    if medals[i][0] == k:
        print(rank[i])
