given = input().upper()
days = 0
for i in range(len(given)):
    if(i%3 == 0 and given[i:i+1]!="P"):
        days = days + 1
    if(i%3 == 1 and given[i:i+1]!="E"):
        days = days + 1
    if(i%3 == 2 and given[i:i+1]!="R"):
        days = days + 1
print(days)
