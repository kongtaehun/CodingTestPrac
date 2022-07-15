from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
titles_val = []
titles_name = []
peoples = []
for i in range(n):
    a, b = map(str, input().split())
    titles_val.append(int(b))
    titles_name.append(a)
for i in range(m):
    peoples.append(int(input()))
for i in peoples:
    print(titles_name[bisect_left(titles_val, i)])
