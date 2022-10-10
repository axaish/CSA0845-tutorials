n=input("s=")
s=''
g=''
for i in n:
    s=s+i
    if(i==' '):
        g=s+g
        s=''
print(g)
