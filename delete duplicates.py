a=[15,14,25,14,32,14,31]
n=len(a)
y=[]
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for num in a:
    if num not in y:
        y.append(num)
print(y)
        
