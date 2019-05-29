atBats = int(input())
dataString = input().split()
data = []
for i in range(atBats):
    data.append(int(dataString[i]))
sum = 0
officialAB = 0
for j in data:
    if(j!=-1):
        sum = sum + j
        officialAB = officialAB + 1
print(sum/officialAB)
