s1 = input()
lst = s1[0]
for i in range(len(s1)):
    if(s1[i]=="-"):
        lst+=(s1[i+1])
print(lst)
