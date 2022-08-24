
import math


def binary_search(start, end, dungeon, atk):
    while start <= end:
        mid = (start+end)//2
        if gameStart2(dungeon, atk, mid):
            end = mid-1
        else:
            start = mid+1
    print(start)

# while로 구현


def gameStart2(dungeon, my_atk, mx_HP):
    cur_HP = mx_HP
    for d_type, d_atk, d_hp in dungeon:
        if d_type == 1:
            while True:
                d_hp -= my_atk
                if d_hp <= 0:
                    break
                cur_HP -= d_atk
                if cur_HP <= 0:
                    return False
        else:
            cur_HP += d_hp
            if cur_HP > mx_HP:
                cur_HP = mx_HP
            my_atk += d_atk
    return True


def gameStart(dungeon, my_atk, mx_HP):
    cur_HP = mx_HP
    for d_type, d_atk, d_hp in dungeon:
        if d_type == 1:
            # 올림한 다음에 -1한다!(원래는 0일때만 -1하는 식으로 코드가 길었음)
            temp = math.ceil(d_hp/my_atk)-1
            cur_HP -= temp*d_atk
            if cur_HP <= 0:
                return False
        else:
            cur_HP += d_hp
            if cur_HP > mx_HP:
                cur_HP = mx_HP
            my_atk += d_atk
    return True


if __name__ == '__main__':
    n, atk = map(int, input().split())
    dungeon = []
    end = int(9e18)
    start = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        # end = max(b*c, end)
        dungeon.append([a, b, c])
    binary_search(start, end, dungeon, atk)
