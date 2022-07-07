# 1일 떄 예외

from collections import Counter
import sys
input = sys.stdin.readline
Non = int(1e9)


def getLength(w, k):
    minLength = Non
    maxLength = 0
    counts = dict(Counter(w))
    selected_chr = []
    for i in counts.keys():
        if counts[i] >= k:
            # i의 인덱스를 합치기
            temp = []
            for idx, c in enumerate(w):
                if c == i:
                    temp.append(idx)
            selected_chr.append(temp)
    for i in selected_chr:
        for j in range(len(i)-k+1):
            maxLength = max(maxLength, i[j+k-1] - i[j])
            minLength = min(minLength, i[j+k-1] - i[j])

    return minLength+1, maxLength+1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        w = list(input())
        k = int(input())
        min_val, max_val = getLength(w, k)
        if min_val == Non+1 and max_val == 1:
            print(-1)
        else:

            print(min_val, max_val)
