n={'2':'[a,b,c]','3':'[d,e,f]','4':'[g,h,i]','5':'[j,k,l]','6':'[m,n,o]','7':'[p,q,r,s]','8':'[t,u,v]','9':'[w,x,y,z]'}
m=input("enter the number : ")
i=0
while(i<len(m)):
    g=n[m[i]]
    print(g)
    i=i+1

if(len(m)==0):
    print("[]")
elif(len(m)==1):
    q=[]
    for b in m:
        f=n[b]
        for c in range (len(f)):
            if(c%2!=0):
                q.append(f[c])
    print(q)
else:   
    i=0
    p=[]
    g=n[m[i]]
    h=n[m[i+1]]
    for j in range(len(g)):
        for k in range(len(h)):
            if(j%2!=0 and k%2!=0):
                a=g[j]+h[k]
                p.append(a)
    print(p)
