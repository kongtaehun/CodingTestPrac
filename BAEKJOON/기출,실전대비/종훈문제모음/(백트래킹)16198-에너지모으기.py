# 브루트포스가능

def bt(energy):

    global result, answer
    if len(energy) <= 2:
        # 저장하기
        answer = max(result, answer)
    else:
        for i in range(1, len(energy)-1):
            energy_val = energy[i]
            energy_get = energy[i-1]*energy[i+1]
            energy = energy[:i]+energy[i+1:]
            result += energy_get
            bt(energy)
            result -= energy_get
            energy = energy[:i]+[energy_val]+energy[i:]

# x번째 에너지구슬을 선택했을 때 얻을 수 있는 에너지의 양


if __name__ == '__main__':
    n = int(input())
    energy = list(map(int, input().split()))
    result = 0
    answer = 0
    bt(energy)
    print(answer)
