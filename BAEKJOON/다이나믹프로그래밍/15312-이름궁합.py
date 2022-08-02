A = list(input())
B = list(input())
STROKES = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1,
           2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
stroke = []
for i in range(len(A)):
    stroke.append(STROKES[ord(A[i]) - 65])
    stroke.append(STROKES[ord(B[i]) - 65])


while True:

    ans = []
    for i in range(len(stroke)-1):
        ans.append((stroke[i]*stroke[i+1]) % 10)
    stroke = ans

    if len(stroke) == 2:
        break

print(''.join(list(map(str, stroke))))
