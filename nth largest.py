list=[14,67,48,23,5,62]
m=len(list)
for i in range(m):
    for j in range(i+1,m):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
n=4
max=list[m-n]
print(n,"th largest number is :",max)

