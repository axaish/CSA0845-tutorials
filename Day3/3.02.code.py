def comb(l):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(l[i]!=l[j] and l[j]!=l[k] and l[i]!=l[k]):
                    print(l[i],l[j],l[k])
l=input("enter the number:")
if(len(l)!=3 or l[0]=='-'):
    print("enter the positive integer having three letters")
else:
    comb(l)
