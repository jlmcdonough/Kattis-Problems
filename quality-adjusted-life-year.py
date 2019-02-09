periods = int(input())
sum = 0
for i in range(periods):
    val1,val2 = input().split(" ",1)
    val1 = float(val1)
    val2 = float(val2)
    res = val1*val2
    sum += res
print(sum)
