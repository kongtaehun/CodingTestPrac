# 폭발문자열의 길이만큼 검사
string = list(input())
bomb_str = list(input())
stk = []

for chr in string:

    stk.append(chr)
    if len(stk) >= len(bomb_str) and stk[-len(bomb_str):] == bomb_str:
        for i in range(len(bomb_str)):
            stk.pop()
if len(stk) == 0:
    print("FRULA")
else:
    print(''.join(stk))
