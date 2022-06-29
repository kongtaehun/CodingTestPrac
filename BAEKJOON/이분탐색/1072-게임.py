

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
if x == y:
    print(-1)
else:
    start = binary_search(x, y)

    print(start[0])
