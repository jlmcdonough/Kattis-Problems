info = input()
m,y = info.split(" ")
if(m=="OCT" or m=="DEC"):
    y = int(y)
    if(y==31 and m=="OCT"):
        print("yup")
    elif(y==25 and m=="DEC"):
        print("yup")
    else:
        print("nope")
else:
    print("nope")
