count = int(input())
for i in range(count):
    try:
        num1,num2 = map(int,input().split("+"))
        print(num1+num2)
    except:
        print("skipped")
