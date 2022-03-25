n, m = map(int, input().split())
parant = [0 for i in range(n+1)]


def find_parant(parant, x):
    if parant[x] != x:
        parant[x] = find_parant(parant, parant[x])
    return parant[x]


def unuin_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a < b:
        parant[b] = a
    else:
        parant[a] = b


for i in range(len(parant)):
    parant[i] = i


cycle = False
for i in range(m):
    a, b = map(int, input().split())
    if find_parant(parant, a) == find_parant(parant, b):
        cycle = True
        break
    else:
        unuin_parant(parant, a, b)
print("사이클발생"if cycle == True else "사이클안발생")
