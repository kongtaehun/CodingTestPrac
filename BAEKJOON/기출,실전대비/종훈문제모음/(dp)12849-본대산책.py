d = int(input())
buildings = [0, 1, 1, 0, 0, 0, 0, 0]  # 1분후일 때
graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5],
         [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]
for i in range(d-1):
    temp = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(len(buildings)):
        cases = 0
        for next in graph[j]:
            cases += buildings[next]
        temp[j] = cases
    buildings = temp
if d == 1:
    print(1)
else:
    print(buildings[0] % 1000000007)
