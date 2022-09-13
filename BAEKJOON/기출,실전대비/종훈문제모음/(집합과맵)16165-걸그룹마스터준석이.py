if __name__ == '__main__':
    n, m = map(int, input().split())
    group = {}
    for _ in range(n):
        g_name = input()
        group[g_name] = set()
        cnt = int(input())
        for i in range(cnt):
            group[g_name].add(input())

    for _ in range(m):
        a = input()
        type = int(input())
        if type == 0:

            for i in sorted(list(group[a])):
                print(i)
        else:
            for i in group.keys():
                if a in group[i]:
                    print(i)
