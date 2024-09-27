n=5
N=5
y=[]
for i in range(1,50):
    if i>1:
        for j in range(2,i):
            if i%j==0:
               break;
        else:
             y.append(i)
print(n,"th prime number :",y[n-1])
print(N," non composite numbers after ",n," th prime number ")
for i in range(n,n+N):
    print(y[i])
    
    

        
   
