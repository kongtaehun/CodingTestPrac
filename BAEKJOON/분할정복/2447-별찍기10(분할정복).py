n = int(input())


def start(n):
    if n == 3:
        return ['***', '* *', '***']
    arr = start(n//3)
    stars = []

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars


for i in start(n):
    print(i)
