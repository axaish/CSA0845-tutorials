n=int(input("n="))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j*j==i):
            count=count+1
print(count)
