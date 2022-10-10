n=int(input("enter the number of elements of l1: "))
s=[]
for i in range(n):
    m=int(input("enter the element: "))
    s.append(m)
p=int(input("enter the number of elements of 12: "))
f=[]
for j in range(p):
    u=int(input("enter the element : "))
    f.append(u)
if(n<=p):
    y=0
    o=[]
    while(y<len(s)):
        o.append(s[y])
        o.append(f[y])
        y=y+1
    for q in range(y,len(f)):
        o.append(f[q])
    print(o)
elif(n<0 or p<0 or (p==0 and n==0)):
    print("invalid and enter the valid value")
elif(n>=p):
    y=0
    o=[]
    while(y<len(f)):
        o.append(s[y])
        o.append(f[y])
        y=y+1
    for q in range(y,len(s)):
        o.append(s[q])
    print(o)
