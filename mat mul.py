a=[[1,2],[5,3]]
b=[[2,3],[4,1]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print("resultant matrix : :")
for row in c:
    print(row)
            
