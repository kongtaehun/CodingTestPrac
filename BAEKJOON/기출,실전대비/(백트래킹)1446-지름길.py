def bt(depth, end):
    global result, save_cost
    result = max(save_cost, result)
    for i in range(len(new_short_cut)):
        if new_short_cut[i][0] >= end:
            save_cost += new_short_cut[i][2]
            bt(depth+1, new_short_cut[i][1])
            save_cost -= new_short_cut[i][2]


if __name__ == '__main__':
    n, d = map(int, input().split())
    short_cut = []

    for i in range(n):
        a, b, c = list(map(int, input().split()))
        # 아낄수 있는 비용
        short_cut.append((a, b, b-a-c))
    short_cut.sort(key=lambda x: (x[0], -x[2]))
    new_short_cut = []
    for i in short_cut:
        if i[2] < 0 or i[1] > d:
            continue
        new_short_cut.append(i)

    result = 0
    save_cost = 0
    bt(1, 0)
    print(d-result)
    # 지름길도착이 목적지 이상일 때 예외
    # 지름길아끼는 비용이 음수일 떄 예외
    # 지름길이용하는 것이 안이용하는 거보다 손해일 예외(위랑 같은 예외네)
