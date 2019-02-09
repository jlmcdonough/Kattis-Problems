loc = 1
moves = input()
moveList = []
for i in range(len(moves)):
    moveList.append(moves[i])
for elem in moveList:
    if(elem=="A" and loc==1):
        loc=2
    elif(elem=="A" and loc==2):
        loc=1
    elif(elem=="B" and loc==2):
        loc=3
    elif(elem=="B" and loc==3):
        loc=2
    elif(elem=="C" and loc==3):
        loc=1
    elif(elem=="C" and loc==1):
        loc=3
print(loc)
