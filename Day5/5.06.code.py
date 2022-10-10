n=int(input("enter the number of rows : "))
m=int(input("enter the row number : "))
p=1
s=0
if(n>0):
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end='')
        for k in range(0,i+1):
            if(k==0 or i==0):
                p=1
                if(i==m):
                    s=s+p
            else:
                p=p*(i-k+1)//k
                if(i==m):
                    s=s+p
            print(p,end=' ')
        print()
    if(m<n and n>0):        
        print("Sum of elements in",m," row : ",s//2)
    else:
        print("enter the valid row number greatre than 0 and less than no.of rows")

else:
    print("give the valid no.of rows ")
