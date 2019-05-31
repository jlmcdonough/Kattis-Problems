count = int(input())
winners = []
winnerCount = 0
for i in range(count):
    contestant = input()
    uni,team = contestant.split(" ")
    if (winnerCount<12):
        if any(uni in s for s in winners):
            pass
        else:
            winners.append(contestant)
            winnerCount = winnerCount + 1
    else:
        break
for j in winners:
    print(j)
