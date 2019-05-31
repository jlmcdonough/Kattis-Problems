entry = input()
whiteSpace = 0
lowercase = 0
uppercase = 0
symbol = 0
for i in entry:
    if(i=="_"):
        whiteSpace = whiteSpace + 1
    elif(ord(i)>=65 and ord(i)<=90):
        uppercase = uppercase + 1
    elif(ord(i)>=97 and ord(i)<=122):
        lowercase = lowercase + 1
    else:
        symbol = symbol + 1
print(whiteSpace/len(entry))
print(lowercase/len(entry))
print(uppercase/len(entry))
print(symbol/len(entry))
