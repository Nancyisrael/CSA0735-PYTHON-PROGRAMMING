arr=[14,16,87,36,25,89,34]
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
M=1
N=3
max=arr[n-M]
min=arr[N-1]
print(M,"st maximum :",max)
print(N,"rd minimum :",min)
add=max+min
sub=max-min
print("SUM :",add)
print("DIFFERENCE :",sub)


