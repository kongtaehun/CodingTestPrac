import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemons = []
pokemons_dict = {}
for i in range(n):
    temp = input()[:-1]
    pokemons.append(temp)
    pokemons_dict[temp] = i+1

answers = []
for i in range(m):
    temp = input()[:-1]
    if temp.isdigit():
        answers.append(pokemons[int(temp)-1])
    else:
        answers.append(pokemons_dict[temp])

for i in answers:
    print(i)
