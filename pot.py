def getPow(b,p):
    initial = b
    if(p==0):
        return 1
    elif(p==1):
        return b
    else:
        for i in range(1,p):
            b*=initial
    return b

trial = int(input())
sum = 0
for i in range(trial):
    val = input()
    power = val[-1]
    power = int(power)
    base = val[:-1]
    base = int(base)
    res = getPow(base,power)
    sum+=res
print(sum)
