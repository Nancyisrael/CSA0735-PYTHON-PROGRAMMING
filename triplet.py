limit=int(input("enter limit:"))
for a in range(1,limit):
    for b in range(a,limit):
        c=(a*a+b*b)**0.5
        if c<=limit and c==int(c):
           print(a,b,int(c))
