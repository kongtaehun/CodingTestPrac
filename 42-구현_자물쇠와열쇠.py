key_arr = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_arr = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# 리스트 회전


def rotate(arr):
    new = [[0]*(len(arr[0])) for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new[j][i] = arr[len(arr[i])-i-1][j]
    return new


# 패딩추가 - lock_arr주변으로 key_arr-1씩
new_lock = [[0]*(len(lock_arr)+2*(len(key_arr)-1))
            for i in range(len(lock_arr)+2*(len(key_arr)-1))]

# 중앙에 lock위치
for i in range(len(lock_arr)):
    for j in range(len(lock_arr)):
        new_lock[(len(key_arr)-1)+i][(len(key_arr)-1)+j] = lock_arr[i][j]

for k in range(4):
    new_lock = rotate(new_lock)

    for i in range(0, (len(key_arr)-1)+len(lock_arr)):
        for j in range(0, (len(key_arr)-1)+len(lock_arr)):

            # 열쇠넣기
            for ii in range(0, len(key_arr)):
                for jj in range(0, len(key_arr)):
                    new_lock[i+ii][j+jj] = new_lock[i+ii][j+jj]+key_arr[ii][jj]

            sum = 0
            # 중앙 검사
            for iii in range(len(key_arr)-1, (len(key_arr)-1)+len(lock_arr)):
                for jjj in range(len(key_arr)-1, (len(key_arr)-1)+len(lock_arr)):
                    if new_lock[iii][jjj] == 1:
                        sum += 1

            if sum == 9:
                print('true')

            # 열쇠빼게
            for ii in range(0, len(key_arr)):
                for jj in range(0, len(key_arr)):
                    new_lock[i+ii][j+jj] = new_lock[i+ii][j+jj]-key_arr[ii][jj]
