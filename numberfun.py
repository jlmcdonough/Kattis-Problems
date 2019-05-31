def add(a,b,c):
    if(a+b==c):
        return True
    elif(b+a==c):
        return True
    else:
        return False
        
def subtract(a,b,c):
    if(a-b==c):
        return True
    elif(b-a==c):
        return True
    else:
        return False

def multi(a,b,c):
    if(a*b==c):
        return True
    elif(b*a==c):
        return True
    else:
        return False

def divi(a,b,c):
    if(a/b==c):
        return True
    elif(b/a==c):
        return True
    else:
        return False
        
count = int(input())
for i in range(count):
    num1,num2,num3 = map(int,input().split(" ",2))
    if(add(num1,num2,num3)):
        print("Possible")
    elif(subtract(num1,num2,num3)):
        print("Possible")
    elif(multi(num1,num2,num3)):
        print("Possible")
    elif(divi(num1,num2,num3)):
        print("Possible")
    else:
        print("Impossible")
