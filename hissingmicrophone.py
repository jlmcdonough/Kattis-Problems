userIn = input()
ans = False
for i in range(len(userIn)-1):
    if(userIn[i]=="s" and userIn[i+1]=="s"):
        ans = True
        break
if(ans):
    print("hiss")
else:
    print("no hiss")
