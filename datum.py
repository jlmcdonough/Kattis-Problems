given = input()
day, month = map(int,given.split(" "))
totalDays = 0
i=0
while(i!=month):
    if (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10):
       totalDays = totalDays + 31
    elif(i == 4 or i == 6 or i == 9 or i == 11):
        totalDays = totalDays + 30
    elif(i == 2):
        totaDays = totalDays + 28
    i = i+1
totalDays = totalDays + day
ans = totalDays%7
if(ans==1):
    print("Thursday")
if(ans==2):
    print("Friday")
if(ans==3):
    print("Saturday")
if(ans==4):
    print("Sunday")
if(ans==5):
    print("Monday")
if(ans==6):
    print("Tuesday")
if(ans==0):
    print("Wednesday")
