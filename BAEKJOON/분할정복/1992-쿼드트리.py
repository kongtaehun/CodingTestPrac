n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, list(input()))))

result = []


def dc(start, n, depth):
    color = board[start[0]][start[1]]

    for i in range(start[0], start[0]+n):
        for j in range(start[1], start[1]+n):
            if color != board[i][j]:
                result.append('(')
                # 이 순서 중요!! 이순서에 맞춰서 재귀
                dc([start[0], start[1]], n//2, depth+1)

                dc([start[0], start[1]+n//2], n//2, depth+1)
                dc([start[0]+n//2, start[1]], n//2, depth+1)
                dc([start[0]+n//2, start[1]+n//2], n//2, depth+1)
                result.append(')')
                # 이 리턴이 중요
                # 리턴을 하지 않으면 for 문돌고 color에 추가하게 됨
                return
    if color == 0:
        result.append('0')

    else:
        result.append('1')


dc([0, 0], n, 1)

print(''.join(result))
