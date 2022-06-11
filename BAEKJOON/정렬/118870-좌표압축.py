n = int(input())
list = list(map(int, input().split()))
new_list = []
for i, v in enumerate(list):
    new_list.append((v, i))
new_list.sort()


comp_list = [0]
before = new_list[0]
serial = 0
for i in range(1, n):
    if before[0] != new_list[i][0]:
        serial += 1
    comp_list.append(serial)
    before = new_list[i]


# 재정렬
new_comp_list = [0 for i in range(n)]
for i, v in enumerate(new_list):
    new_comp_list[v[1]] = comp_list[i]

# 출력
for i in new_comp_list:
    print(i, end=' ')
