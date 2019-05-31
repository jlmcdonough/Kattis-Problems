active = True
while(active):
    try:
        n1,n2 = map(int,input().split(" "))
        if(n1>n2):
            print(n1-n2)
        else:
            print(n2-n1)
    except:
        active = False
