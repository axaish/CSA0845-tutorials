n=int(input("total users : "))
if(n>0):
    m=int(input("staff users : "))
    if(n<=m):
        print("student users : 0")
    else:
        s=n-m-m//3
        print("student users : ",s)
else:
    print("enter valid total user")
