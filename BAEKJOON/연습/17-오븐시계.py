h, m = map(int, input().split())
a = int(input())
mmm = h*60+m
resiult = mmm+a

hh = resiult//60
if hh > 23:
    hh = hh-24
mm = resiult % 60

print(str(hh)+' '+str(mm))
