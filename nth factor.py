n=int(input("enter the number : "))
y=[]
for i in range(1,n+1):
    if(n%i==0):
        y.append(i)
print(y,end=" ")
print()
m=int(input("enter the m value : "))
print()
print(m,"th factor : ",y[m-1])
