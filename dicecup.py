def findHighest(aList):
    maxCount = 0
    theCount = 0
    finalList = []
    for i in range(len(aList)-1):
        if(aList[i] == aList[i+1]):
            theCount+=1
        else:
            theCount = 1
        if(theCount>maxCount):
            maxCount = theCount
    for i in range(len(aList)-1):
        if(aList[i] == aList[i+1]):
            theCount+=1
        else:
            theCount = 1
        if(theCount==maxCount):
            finalList.append(aList[i])
    return finalList

theDie = input()
outcomes = []
d1, d2 = map(int,theDie.split(" "))
for i in range(1,d1+1):
    for j in range(1,d2+1):
        outcomes.append(i+j)
outcomes.sort()
ans = findHighest(outcomes)
for i in ans:
    print(i)
