INF = int(1e9)
# 중위순회~!
# 시작노드가 ㅈ정해지지않음 -> 부모노드가 -1인 노드 찾기


def inorder(tree, root, step):
    global cnt, x_coor
    if root != -1:
        inorder(tree, tree[root][0], step+1)
        x_coor[root][0] = cnt
        x_coor[root][1] = step
        cnt += 1
        inorder(tree, tree[root][1], step+1)


if __name__ == '__main__':
    n = int(input())
    cnt = 1
    tree = [[-1, -1, -1] for i in range(n+1)]
    for i in range(n):
        a, b, c = map(int, input().split())
        tree[a][0] = b
        tree[a][1] = c
        if b != -1:
            tree[b][2] = a
        if c != -1:
            tree[c][2] = a
    x_coor = [[0, 0] for i in range(n+1)]

    # 시작노드찾기 (부모노드가 -1인 것)

    for i in range(1, n+1):
        if tree[i][2] == -1:
            start = i

    inorder(tree, start, 1)

    x_coor.sort(key=lambda x: x[1])
    # print(x_coor[1:])
    temp = 0
    for i in range(1, len(x_coor)):
        temp = max(x_coor[i][1], temp)
    levels = [[INF, -INF] for i in range(temp+1)]

    for i in range(1, len(x_coor)):
        levels[x_coor[i][1]][0] = min(levels[x_coor[i][1]][0], x_coor[i][0])
        levels[x_coor[i][1]][1] = max(levels[x_coor[i][1]][1], x_coor[i][0])
    answer = 0
    answer_level = 0
    # print(levels)
    for i in range(1, temp+1):
        if answer < levels[i][1]-levels[i][0] + 1:
            answer = levels[i][1]-levels[i][0] + 1
            answer_level = i
    print(answer_level, answer)
