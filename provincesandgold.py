gSC = input()
gold,silver,copper = map(int,gSC.split(" "))
buyPower = ((gold*3) + (silver*2) + (copper*1))
victory = ""
treasure = ""
if(buyPower>=8):
    victory = "Province or "
elif(buyPower>=5):
    victory = "Duchy or "
elif(buyPower>=2):
    victory = "Estate or "
else:
    victory = ""
if(buyPower>=6):
    treasure = "Gold"
elif(buyPower>=3):
    treasure = "Silver"
else:
    treasure = "Copper"
print(victory + treasure)
