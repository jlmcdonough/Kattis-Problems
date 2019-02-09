cost = float(input())
lawns = int(input())
sum = 0.0
for i in range(lawns):
    x = input()
    val1,val2 = map(float,x.split(" "))
    sum += (val1*val2)*cost
print(sum)
