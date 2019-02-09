userInput = input()
number, value = userInput.split(" ",1)
limit = int(number) *4
total=0
for i in range(limit):
    inputted = input()
    num=inputted[0]
    hand=inputted[1]
    if(str(num)=="A"):
        total+=11
    elif(str(num)=="K"):
        total+=4
    elif(str(num)=="Q"):
        total+=3
    elif(str(num)=="J"):
        if(value==hand):
            total+=20
        else:
            total+=2
    elif(str(num)=="T"):
        total+=10
    elif(str(num)=="9" and value==hand):
        total+=14
    else:
        total+=0
print(total)
