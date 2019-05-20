def howMany(cityCount):
    for i in range(len(cityCount)-1,-1,-1):
        try:        
            for j in range(i):
                if(cityCount[i]==cityCount[j]):
                    del cityCount[j]
                    
        except:
            pass
    return len(cityCount)
    
totalTrips = int(input())
for i in range(totalTrips):
    cityCount = []
    for j in range(int(input())):
        cityCount.append(input())
    print(howMany(cityCount))
    
    
