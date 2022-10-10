n=int(input("enter the no.of elements:"))
l=[]
o=[]
for i in range(n):
    m=int(input())
    l.append(m)
print("nums=",l)
for k in range(n):
    count=0
    for j in range(n):
        if(l[k]>l[j]):
            count=count+1
    o.append(count)
print("Output:",o)
