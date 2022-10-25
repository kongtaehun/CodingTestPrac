
target = int(input())
now = 1
diff = 0
while True:
    now += 6*(diff)
    if now < target:
        diff += 1
    else:
        print(diff+1)
        break
