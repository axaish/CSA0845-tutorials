n=int(input("enter the number of elements:"))
j=[]
for u in range(n):
    m=int(input())
    j.append(m)
print(j)
sum=0
for i in range(1,n):
    if(j[i-1]<j[i]):
        l=j[i]-j[i-1]
        sum=sum+l
print(sum)
