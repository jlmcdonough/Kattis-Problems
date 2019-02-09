n = input()
x, y = n.split(" ",1)
hours = int(x)
mins = int(y)
for i in range(45):
    if(int(mins)>0):
        mins-=1
    elif(int(hours)==0 and int(mins)==0):
        hours=23
        mins=59
    else:
        hours-=1
        mins=59
print(str(hours) + " " + str(mins))
