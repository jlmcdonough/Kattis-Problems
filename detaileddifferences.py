cases = int(input())
for i in range(cases):
    ans = ""
    t1 = input()
    t2 = input()
    for j in range(len(t1)):
        if(t1[j]==t2[j]):
            ans+="."
        else:
            ans+="*"
    print(t1)
    print(t2)
    print(ans)
    print()
