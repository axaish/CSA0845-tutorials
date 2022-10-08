n=float(input("enter the year:"))
if(n>0 and n.is_integer()):
    if(n%4==0 or n%400==0):
        print('it is a leap year\n',n+4)
    else:
        print("it is not a leap year\n",n-n%4)
else:
    print("not a valid input")
