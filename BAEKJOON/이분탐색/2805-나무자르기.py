# ============config===========
import sys
input = sys.stdin.readline

# ============method===========


def getRmainTree(val, tree):
    remains = 0
    for i in tree:
        if i > val:
            remains += i-val
    return remains


# ============input===========
n, m = map(int, input().split())
tree = list(map(int, input().split()))
target = m
start = 1
end = max(tree)

# ============main===========
while start <= end:
    mid = (start+end)//2
    check = getRmainTree(mid, tree)
    if target > check:
        end = mid-1
    else:
        start = mid+1
print(start-1)
