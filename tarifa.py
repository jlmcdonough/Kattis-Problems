megabyteAllowed = int(input())
monthTotal = int(input())
megabyteTotal = megabyteAllowed
for i in range(monthTotal):
    megabyteSpent=int(input())
    remainder=megabyteAllowed-megabyteSpent
    megabyteTotal+=remainder
print(megabyteTotal)
