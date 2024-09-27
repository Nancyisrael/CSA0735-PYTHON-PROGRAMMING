arr=[16,18,27,16,23,21,19]
s=sum(arr)
n=len(arr)
m=s/n
print("Mean :",m)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
median=arr[n//2]
print("Median :",median)
c=1
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            c+=1
            if c>1:
                print("Mode :",arr[i])
    
