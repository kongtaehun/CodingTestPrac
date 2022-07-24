n = int(input())
peoples = []
for i in range(n):
    peoples.append(list(map(int, input().split())))

# # peoples.sort(key=lambda x: (-x[1], -x[2]))


# result = [0]*(n)
# now_count = 1
# result[peoples[0][0]] = 1
# for i in range(1, n):
#     if peoples[i][2] < peoples[i-1][2] and peoples[i][1] < peoples[i-1][1]:
#         now_count += 1
#         result[peoples[i][0]] = now_count
#     else:
#         now_count += 1
#         result[peoples[i][0]] = result[peoples[i-1][0]]

# for i in result:
#     print(i, end=' ')


for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j:
            if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
                cnt += 1
    print(cnt, end=' ')
