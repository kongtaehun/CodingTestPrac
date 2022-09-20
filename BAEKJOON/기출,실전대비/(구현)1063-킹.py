
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]


def move(direc, k, s):

    kx = k[0] + dx[direc]
    ky = k[1] + dy[direc]
    if kx < 1 or kx > 8 or ky < 1 or ky > 8:
        return
    if kx == s[0] and ky == s[1]:
        sx = s[0] + dx[direc]
        sy = s[1] + dy[direc]
        if sx < 1 or sx > 8 or sy < 1 or sy > 8:
            return
        s[0] = sx
        s[1] = sy
    k[0] = kx
    k[1] = ky


if __name__ == '__main__':

    king, stone, m = map(str, input().split())

    king = list(king)
    king[0] = ord(king[0])-64
    king[1] = int(king[1])
    stone = list(stone)
    stone[0] = ord(stone[0])-64
    stone[1] = int(stone[1])

    MOVES = {}
    MOVES['R'] = 0
    MOVES['L'] = 1
    MOVES['B'] = 2
    MOVES['T'] = 3
    MOVES['RT'] = 4
    MOVES['LT'] = 5
    MOVES['RB'] = 6
    MOVES['LB'] = 7

    for _ in range(int(m)):

        move(MOVES[input()], king, stone)

    print(str(chr(king[0]+64))+str(king[1]))
    print(str(chr(stone[0]+64))+str(stone[1]))
