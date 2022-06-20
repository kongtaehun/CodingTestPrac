import sys
input = sys.stdin.readline
n, m = map(int, input().split())

pokedict_num = {}
pokedict_name = {}

for i in range(n):
    name = input()
    pokedict_name[name[-1]] = i+1
    pokedict_num[i+1] = name[-1]

print(pokedict_name)
result = []
for i in range(m):
    question = input()
    if question.isdigit():
        result.append(pokedict_num[question[-1]])
    else:
        result.append(pokedict_name[question[-1]])
for i in range(m):
    print(result[i])
