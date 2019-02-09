cards = input()
c1,c2,c3,c4,c5 = cards.split(" ")
t1 = c1[0]
t2 = c2[0]
t3 = c3[0]
t4 = c4[0]
t5 = c5[0]
cardList = [t1,t2,t3,t4,t5]
card = {"A":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0,
"9":0, "T":0, "J":0, "Q":0, "K":0}
for i in range(5):
    for j in card:
        if(j==cardList[i]):
            card[j] = card[j] + 1
largeVal = -1
largeType = ""
for k,v in card.items():
    if(v>largeVal):
        largeType = k
        largeVal = v
print(largeVal)
    
