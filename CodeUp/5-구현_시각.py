a = int(input())
count = 0
for i in range(0, a+1):
    if "3" in str(i):
        count = count+60*60
    else:
        for j in range(0, 60):
            if "3" in str(j):
                count = count+60
            else:
                for j in range(0, 60):
                    if "3" in str(j):
                        count = count+1


print(count)
