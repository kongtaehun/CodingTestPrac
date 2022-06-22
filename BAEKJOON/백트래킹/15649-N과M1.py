from itertools import permutations
n, m = map(int, input().split())
temp = list(permutations([i+1 for i in range(n)], m))

for x in temp:
    for i in x:
        print(i, end=' ')
    print()
