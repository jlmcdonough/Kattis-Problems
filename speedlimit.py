setAmount = int(input())
mileList = []
while setAmount!= -1:
    mileCount = 0
    currMile = 0
    totalDist = 0
    for i in range(setAmount):
        temp = input()
        val1,val2 = map(int,temp.split(" "))
        currMile = val2-mileCount
        totalDist+=currMile*val1 
        mileCount=val2
    mileList.append(totalDist)
    setAmount = int(input())

for i in mileList:
    print(i, "miles")
