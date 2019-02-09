def sumOf(num):
    res = 0
    while num:
        res+= num%10
        num//=10
    return res

original = int(input())
while True:
    ans = original/sumOf(original)
    if(ans.is_integer()):
         print(original)
         break
    else:
        original+=1
