trials = int(input())
for i in range(trials):
    msg = input()
    squareSize = int(len(msg))**.5
    squareSize = int(squareSize)
    ans = [ [ 0 for r in range(squareSize) ] for s in range(squareSize) ]
    j=x=y= squareSize-1
    #x = squareSize-1
    #y = squareSize-1
    z = 0
    result = ""
    while j >=0:
        for k in range(squareSize):
            ans[k][j] = msg[z:z+1]
            z = z+1
        j = j - 1
    while x>=0:
        while y>=0:
            result = result + ans[x][y]
            y =  y - 1
        x = x-1
        y = squareSize-1
    print(result)
