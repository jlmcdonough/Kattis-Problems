mile = float(input())
ROMAN_MILE = ((5280/4854)*1000)
mile = ROMAN_MILE * mile
print(int(mile-0.5)+1)
