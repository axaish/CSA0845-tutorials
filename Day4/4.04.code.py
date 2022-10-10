n=input("s=")
p=n.lower()
s=''
for i in p:
    if(i.isalpha()):
        s=s+i
if(s==s[::-1]):
    print("true")
else:
    print("false")
