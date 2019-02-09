firstLine = input()
matchAmount, length, width = map(int,firstLine.split(" "))
l2 = length * length
w2 = width * width
hyp = l2 + w2 + 0.01
for i in range(matchAmount):
    currMatch = int(input())
    c2 = currMatch*currMatch
    if(c2<hyp):
        print("DA")
    else:
        print("NE")
