def delchar(s,c):
    if(len(c)>1):
        return s
    else:
        w=''
        for i in s:
            if(i!=c):
                w=w+i
        return w
s=input("enter the string : ")
c=input("enter the charecter to remove : ")
print("string after removing charecter :",delchar(s,c))
