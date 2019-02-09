def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
ans = []        
inp = int(input())
for i in range(inp):
    x = int(input())
    fact = (factorial(x))
    if(fact>10):
        temp = str(fact)
        ans.append(temp[-1])
    else:
        ans.append(fact)

for y in ans:
    print(y)
