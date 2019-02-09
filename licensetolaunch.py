days = int(input())
amountJunk = input()
spaceJunk = amountJunk.split(" ")
for i in range(len(spaceJunk)):
    spaceJunk[i] = int(spaceJunk[i])
min = 99999
for i in range(days):
    if (spaceJunk[i]<min):
        min = spaceJunk[i]
        ans = i
print(ans)
