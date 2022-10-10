n=int(input("Enter the number of elements:"))
j=[]
for i in range(n):
    m=int(input(""))
    j.append(m)
print(j)
y=max(j)
for d in range(n):
    if(y==j[d]):
        print(d)
