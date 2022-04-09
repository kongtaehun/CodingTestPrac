h, m = map(int, input().split())
mm = h*60+m
resiult = mm-45

hh = resiult//60
if hh < 0:
    hh = 24+hh
mmm = resiult % 60
print(str(hh)+' '+str(mmm))
