a, b, c = list(map(int, input().split()))
# 같은눈세개
if a == b and b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
elif a == c:
    print(1000+c*100)
else:
    print(max([a, b, c])*100)
