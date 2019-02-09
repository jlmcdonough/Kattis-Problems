cards = input()
T=0
C=0
G=0
for i in range(len(cards)):
    if(cards[i]=="T"):
        T+=1
    if(cards[i]=="C"):
        C+=1
    if(cards[i]=="G"):
        G+=1
total = (T*T) + (C*C) + (G*G)
if(T<C and T<G and T!=0):
    for i in range(T):
        total+=7
elif(C<T and C<G and C!=0):
    for i in range(C):
        total+=7
elif(G<T and G<C and G!=0):
    for i in range(G):
        total+=7
elif(T==C and C==G and T!=0):
    for i in range(T):
        total+=7
elif(T>=1 and C>=1 and G>=1):
    total+=7
print(total)
