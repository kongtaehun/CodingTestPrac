while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    temp = [a, b, c]
    temp.sort()
    if temp[-1] >= sum(temp[:2]):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
