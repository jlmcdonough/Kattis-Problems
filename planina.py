iterations = int(input())
lineDot = 2
for i in range(iterations):
    lineDot*=2
    lineDot-=1
totalDots = lineDot*lineDot
print(totalDots)
