def getScore(scores):
    p1,p2,p3,p4 = map(int,scores.split(" "))
    res = p1+p2+p3+p4
    return res
    
person1 = getScore(input())
person2 = getScore(input())
person3 = getScore(input())
person4 = getScore(input())
person5 = getScore(input())

scoreDict = {1:person1, 2:person2, 3:person3, 4:person4, 5:person5}
maxScore = -1
winner = 0
for k,v in scoreDict.items():
    if(v>maxScore):
        maxScore=v
        winner = k
print(winner, maxScore)
        
