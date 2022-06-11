g = int(input())
p = int(input())
p_list = []
for i in range(p):
    p_list.append(int(input()))


def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]


def union_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a > b:
        parant[a] = b
    else:
        parant[b] = a


parant = [i for i in range(g+1)]
dock_cnt = 0
for i in range(p):
    par = find_parant(parant, p_list[i])
    if par != 0:
        print("현재 부모는"+str(find_parant(parant, p_list[i])))
        # p[i]와 p[i]-1루트노드 p[-1]fh
        union_parant(parant, par, par-1)
        dock_cnt += 1
    else:
        break
print(parant)
print(dock_cnt)
