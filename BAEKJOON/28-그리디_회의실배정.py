n = int(input())
# 가장 시간이 작은 거부터 정렬하고 배치한다.
schedule = [0 for i in range(n+1)]
time = []

for i in range(n):
    time.append(list(map(int, input().split())))
# 시작시간정렬 -> 종료시간 정렬
time.sort(key=lambda x: x[0])
print(time)
