
# 두개의 배열을 서로 비교할 때 순차적으로 인덱스가 동시에 움직이지 않음
# 예외케이스
def move(crane, box):
    box_idx = 0
    crane_idx = 0
    while box_idx < len(box) and crane_idx < len(crane):
        # 가장 논높은 수를 비교
        if box[box_idx] <= crane[crane_idx]:
            crane_idx += 1
            box = box[:box_idx]+box[box_idx+1:]
        else:
            box_idx += 1
        if len(box) == 0:
            break
    return box


def movingStart(crane, box):
    if crane[0] < box[0]:
        return -1
    minute = 0
    while True:
        if len(box) <= 0:
            break
        box = move(crane, box)
        minute += 1

    return minute


if __name__ == '__main__':
    n = int(input())
    crane = list(map(int, input().split()))
    m = int(input())
    box = list(map(int, input().split()))
    crane.sort(reverse=True)
    box.sort(reverse=True)

    print(movingStart(crane, box))
