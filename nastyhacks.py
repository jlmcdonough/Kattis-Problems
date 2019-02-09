trials = int(input())
ans = []
for i in range(trials):
    case = input()
    r,e,c = map(int,case.split(" "))
    if(r+c <e):
        ans.append("advertise")
    elif(r+c==e):
        ans.append("does not matter")
    elif(r+c >e):
        ans.append("do not advertise")
for j in ans:
    print(j)
