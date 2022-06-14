n, m = map(int, input().split())
noSee = set()
noHear = set()
for i in range(n):
    noHear.add(input())

for i in range(m):
    noSee.add(input())

noSeeHear = noSee & noHear
noSeeHear = list(noSeeHear)
noSeeHear.sort()
print(len(noSeeHear))
for i in noSeeHear:
    print(i)
