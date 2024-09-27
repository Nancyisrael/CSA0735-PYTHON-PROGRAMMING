a=[[1,2],[5,3]]
b=[[2,3],[4,1]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j]=a[i][j]+b[i][j]
for i in range(len(a)):
    for j in range(len(a)):    
        print(c[i][j],end=" ")                 
    print()
