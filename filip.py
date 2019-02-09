def flip(val):
    ans=""
    val = str(val)
    for i in range(1,4):
        ans+=val[-i]
    ans = int(ans)
    return ans
    
x = input()
val1,val2 = map(int,x.split(" ",1))
num1 = flip(val1)
num2 = flip(val2)
if(num1>num2):
    print(num1)
else:
    print(num2)
