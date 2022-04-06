# 풀이하지 못함 !
# 매번 전체의 구조물을 확인하는게 더 효율적이고 빠르다.
# 실패

# 하나씩 넣고 추가하기
n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
               [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


# 1. 보
# 양끝이 보
# 한쪽 끝이 기둥
# 2. 기둥
# 바닥에 붙어있거나()
# 보의 한쪽과 연결되어 있거나
# 기둥과 연결되어있어야함


def check(result):
    for x, y, stuff in result:
        # 기둥일 경우
        if stuff == 0:
            # 바닥에 붙어있거나()
            # 시작지점이 보에 연결
            # 기둥과 연결되어있어야함
            if y != 0 and [x, y-1, 0] not in result and [x, y, 1] not in result and [x-1, y, 1] not in result:
                return False
        elif stuff == 1:
            # 양끝이 보(자기자신의 보가 있거나 -1에서 보가 있어야함)
            # 한쪽 끝이 기둥
            if [x-1, y, 1] in result and [x, y, 1] in result:
                pass
            elif [x+1, y-1, 0] in result or [x, y-1, 1] in result:
                pass
            else:
                return False
        return True


result = []
for frame in build_frame:
    x, y, stuff, operate = frame
    # 삭제하는 경우
    if operate == 0:
        result.remove([x, y, stuff])
        if check(result) == False:
            result.append([x, y, stuff])
    # 삽입하는 경우
    elif operate == 1:
        result.append([x, y, stuff])
        if check(result) == False:
            result.remove([x, y, stuff])
print(sorted(result))
