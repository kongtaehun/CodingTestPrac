n = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0

for i in range(n):
    result += sum(P[:i+1])
    

print(result)
