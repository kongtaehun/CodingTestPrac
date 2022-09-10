
def gameResult(MS, TK):
    if MS == 'R' and TK == 'S':
        return 0
    if MS == 'S' and TK == 'R':
        return 1
    if MS == 'S' and TK == 'P':
        return 0
    if MS == 'P' and TK == 'S':
        return 1
    if MS == 'P' and TK == 'R':
        return 0
    if MS == 'R' and TK == 'P':
        return 1
    else:
        return -1


M_l, M_r, T_l, T_r = map(str, input().split())
# 민성이 이기는경우(한손이 둘다 이길 때)
a = gameResult(M_l, T_l)
b = gameResult(M_l, T_r)
c = gameResult(M_r, T_l)
d = gameResult(M_r, T_r)

if a == 0 and b == 0:
    print('MS')
elif c == 0 and d == 0:
    print('MS')
elif a == 1 and c == 1:
    print('TK')
elif b == 1 and d == 1:
    print('TK')
else:
    print('?')
