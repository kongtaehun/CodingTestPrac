n, k = map(int, input().split())
lis = []
A = list(sorted(list(map(int, input().split()))))
B = list(sorted(list(map(int, input().split())), reverse=True))

for i in range(k):
    if A[i] <= B[i]:
        A[i] = B[i]
print(sum(A))
