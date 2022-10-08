n=int(input("T="))
l=[]
m=[]
if(n>0):
    for i in range(n):
        m2=int(input("E="))
        l.append(m2)
    print(l)
    for j in range(n):
        m3=int(input("L="))
        m.append(m3)
    print(m)
    k=0
    i=0
    g=[]
    while(i<n):
        k=k+l[i]-m[i]
        g.append(k)
        i=i+1
    print(g)
    print(max(g))
else:
    print("enter the poisitive numbers")
