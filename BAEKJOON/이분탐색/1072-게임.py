#예외조건 실수 : 99퍼이면 예외임 - 한번이라도 졌었기 때문에 절대 100%가 될 수 없다.
#             100 퍼일 경우 더이상 오를 승률이 없다.
#부동소수점 실수

def binary_search(x, y):
    origin = int((y*100/x))
    start = 1
    end = x
    while start <= end:
        mid = (start+end)//2
        percent = int((y+mid)*100/(x+mid))
        # print("값의 범위 : " + str(start) + ", " + str(end) +
        #       "    mid : " + str(mid)+"     승률 : "+str(percent) + "     원래승률 : "+str(origin))
        if origin < percent:
            end = mid-1
        else:
            start = mid+1

    return start, percent


x, y = map(int, input().split())
z = (y*100)//x
if z>=99:
    print(-1)
else:
    start = binary_search(x, y)

    print(start[0])
