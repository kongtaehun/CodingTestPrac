

p, m = map(int, input().split())  # 플레이어수, 방의 정원
rooms = []  # 첫번째 요소 = 방의 레벨기준, 두번째요소 = 방에 포함된 인원 리스트
result_started = []
result_waiting = []
for i in range(p):
    a, b = map(str, input().split())

    # 방이 하나도 없을 경우
    if len(rooms) == 0:
        rooms.append([int(a), [(int(a), b)]])
        continue

    # 기존 방 검색
    # 방입잘 flag
    flag = 0
    for i, v in enumerate(rooms):
        if v[0]-10 <= int(a) <= v[0]+10 and len(rooms[i][1]) < m:
            rooms[i][1].append((int(a), b))
            flag = 1
            break

    # 방에 입장 하지 않았다면 방만들기
    if flag == 0:
        rooms.append([int(a), [(int(a), b)]])

for room in rooms:
    room[1].sort(key=lambda x: x[1])
    if len(room[1]) == m:
        print("Started!")
        for i in room[1]:
            print(i[0], i[1])
    else:
        print("Waiting!")
        for i in room[1]:
            print(i[0], i[1])
