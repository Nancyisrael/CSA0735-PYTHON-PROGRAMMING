n=int(input("enter the n value: "))
y=[]
for i in range(1,500):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        y.append(i)
    if len(y)==n:
        break
for k in range(n):
    print(y[k],end=" ")



