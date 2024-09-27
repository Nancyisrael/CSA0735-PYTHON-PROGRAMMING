n=100
c=0
y=[]
for i in range(1,n+1):
        if n%i==0:
            c+=1
            y.append(i)
print(y)
print("number of factors: ",c)
N=4
print("first ",N,"factors are:")
for i in range(N):
    print(y[i],end=" ")
