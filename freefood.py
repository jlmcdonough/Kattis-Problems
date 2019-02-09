days = int(input())
listOfDays = []
finalList = []
for i in range(days):
    temp = input()
    a,b = map(int,temp.split(" ",1))
    dayCount = b-a
    for j in range(dayCount+1):
        listOfDays.append(b-j)
for elem in listOfDays:
    if(elem not in finalList):
        finalList.append(elem)
print(len(finalList))
