s=input("s=")
k=int(input("k="))
count=1
r=[]
t=0
for i in range (len(s)):
    count=0
    for j in range(len(s)):
        if(s[i]==s[j]):
            count+=1
    r.append(count)
for e in r:
    if(k<=e):
        t=t+1
print(t)
