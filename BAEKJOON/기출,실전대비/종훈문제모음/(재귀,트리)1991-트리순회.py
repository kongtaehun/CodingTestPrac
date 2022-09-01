# 전위순휘
def front(root):
    print(root, end='')
    left, right = dic[root][1], dic[root][2]
    if left != '.':
        front(left)
    if right != '.':
        front(right)


def middle(root):
    left, right = dic[root][1], dic[root][2]
    if left != '.':
        middle(left)
    print(root, end='')
    if right != '.':
        middle(right)


def back(root):
    left, right = dic[root][1], dic[root][2]
    if left != '.':
        back(left)
    if right != '.':
        back(right)
    print(root, end='')


if __name__ == '__main__':
    n = int(input())
    dic = {}
    for i in range(n):
        a, b, c = map(str, input().split())
        dic[a] = [b, c]

    front('A')
    print()
    middle('A')
    print()
    back('A')
