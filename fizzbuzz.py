xYN = input()
x, y, n = map(int,xYN.split(" "))
for i in range(1,n+1):
    if(((i/x).is_integer()) and ((i/y).is_integer())):
        print("FizzBuzz")
    elif((i/x).is_integer()):
        print("Fizz")
    elif((i/y).is_integer()):
        print("Buzz")
    else:
        print(i)
