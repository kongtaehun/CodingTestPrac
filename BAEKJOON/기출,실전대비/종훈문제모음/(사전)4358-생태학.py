import sys
input = sys.stdin.readline
all_animals = {}
while True:
    temp = input().rstrip()
    if not temp:
        break
    if temp not in all_animals:
        all_animals[temp] = 1
    else:
        all_animals[temp] += 1
sum_val = sum(all_animals.values())
for key in sorted(all_animals.keys()):
    print(key, end=' ')
    print('%0.4f' % round((all_animals[key]/sum_val)*100, 4))
