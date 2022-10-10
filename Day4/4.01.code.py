n=int(input("n = "))
l=[]
for i in range(n+1):
    if(i%3==0 and i%5==0):
        l.append("fizzbuzz")
    elif(i%3==0):
        l.append("fizz")
    elif(i%5==0):
        l.append("buzz")
    else:
        l.append(i)
print(l[1:])
