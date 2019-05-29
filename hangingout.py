max, trials = map(int,input().split(" "))
notAllowed = 0
balcTotal = 0
for i in range(trials):
    status,count = input().split(" ")
    count = int(count)
    if(status=="enter"):
        temp = balcTotal + count
        if(temp>max):
            notAllowed = notAllowed + 1
        else:
            balcTotal = balcTotal + count
    if(status=="leave"):
        balcTotal = balcTotal-count
print(notAllowed)
