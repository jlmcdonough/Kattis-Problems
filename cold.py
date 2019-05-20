subZeroCount=0
count = int(input())
temps = input()
numTemps = [int(x) for x in temps.split()]
for i in range(count):
    if(numTemps[i]<0):
        subZeroCount+=1
print(subZeroCount)
